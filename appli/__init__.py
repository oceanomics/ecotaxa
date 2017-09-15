# -*- coding: utf-8 -*-
# This file is part of Ecotaxa, see license.md in the application root directory for license informations.
# Copyright (C) 2015-2016  Picheral, Colin, Irisson (UPMC-CNRS)

import os,sys,pathlib
# Permet de traiter le probleme de l'execution dans un virtualenv sous windows de mathplotlib qui requiert TCL
if sys.platform.startswith('win32'):
    virtualprefix = sys.base_prefix
    if hasattr(sys, 'real_prefix'):
        sys.base_prefix = sys.real_prefix
    from tkinter import _fix
    if "TCL_LIBRARY" not in os.environ:
        # reload module, so that sys.real_prefix be used
        from imp import reload
        reload(_fix)
    sys.base_prefix = virtualprefix

VaultRootDir=os.path.join(os.path.dirname(os.path.realpath(__file__)), "..","vault")
if not os.path.exists(VaultRootDir):
    os.mkdir(VaultRootDir)
TempTaskDir=os.path.join(os.path.dirname(os.path.realpath(__file__)), "..","temptask")
if not os.path.exists(TempTaskDir):
    os.mkdir(TempTaskDir)

from flask import Flask,render_template,request,g
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security
import inspect,html,math,threading,time,traceback
import appli.securitycachedstore

app = Flask("appli")
app.config.from_pyfile('config.cfg')

if 'PYTHONEXECUTABLE' in app.config:
    app.PythonExecutable=app.config['PYTHONEXECUTABLE']
else:
    app.PythonExecutable="TBD"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app,session_options={'expire_on_commit':True}) # expire_on_commit évite d'avoir des select quand on manipule les objets aprés un commit.

import appli.database
# Setup Flask-Security
user_datastore = appli.securitycachedstore.SQLAlchemyUserDatastoreCACHED(db, database.users, database.roles)
security = Security(app, user_datastore)

app.MRUClassif = {} # Dictionnaire des valeurs recement utilisé par les classifications
app.MRUClassif_lock = threading.Lock()

def ObjectToStr(o):
#    return str([(n, v) for n, v in inspect.getmembers(o) if((not inspect.ismethod(v))and  (not inspect.isfunction(v))and  (n!='__module__')and  (n!='__doc__') and  (n!='__dict__') and  (n!='__dir__')and  (n!='__delattr__')and  (n!='__dir__')and  (n!='__dir__') )])
    return str([(n, v) for n, v in inspect.getmembers(o) if(('method' not in str(v))and  (not inspect.isfunction(v))and  (n!='__module__')and  (n!='__doc__') and  (n!='__dict__') and  (n!='__dir__') and  (n!='__weakref__') )])

def PrintInCharte(txt):
    """
    Permet d'afficher un texte (qui ne sera pas echapé dans la charte graphique
    :param txt: Texte à affiche
    :return: Texte rendu
    """
    AddTaskSummaryForTemplate()
    return render_template('layout.html',bodycontent=txt)

def ErrorFormat(txt):
    return """
<div class='cell panel ' style='background-color: #f2dede; margin: 15px;'><div class='body' >
				<table style='background-color: #f2dede'><tr><td width='50px' style='color: red;font-size: larger'> <span class='glyphicon glyphicon-exclamation-sign'></span></td>
				<td style='color: red;font-size: larger;vertical-align: middle;'><B>%s</B></td>
				</tr></table></div></div>
    """%(txt)

def AddTaskSummaryForTemplate():
    from flask_login import current_user
    if getattr(current_user, 'id', -1) > 0:
        g.tasksummary = appli.database.GetAssoc2Col(
            "SELECT taskstate,count(*) from temp_tasks WHERE owner_id=%(owner_id)s group by taskstate"
            , {'owner_id': current_user.id})
    g.google_analytics_id = app.config.get('GOOGLE_ANALYTICS_ID', '')


def gvg(varname,defvalue=''):
    """
    Permet de récuperer une variable dans la Chaine GET ou de retourner une valeur par defaut
    :param varname: Variable à récuperer
    :param defvalue: Valeur par default
    :return: Chaine de la variable ou valeur par default si elle n'existe pas
    """
    return request.args.get(varname, defvalue)

def gvp(varname,defvalue=''):
    """
    Permet de récuperer une variable dans la Chaine POST ou de retourner une valeur par defaut
    :param varname: Variable à récuperer
    :param defvalue: Valeur par default
    :return: Chaine de la variable ou valeur par default si elle n'existe pas
    """
    return request.form.get(varname, defvalue)

def ntcv(v):
    """
    Permet de récuperer une chaine que la source soit une chaine ou un None issue d'une DB
    :param v: Chaine potentiellement None
    :return: V ou chaine vide
    """
    if v is None:
        return ""
    return v

def nonetoformat(v,fmt :str):
    """
    Permet de faire un formatage qui n'aura lieu que si la donnée n'est pas nulle et permet récuperer une chaine que la source soit une données ou un None issue d'une DB
    :param v: Chaine potentiellement None
    :param fmt: clause de formatage qui va etre générée par {0:fmt}
    :return: V ou chaine vide
    """
    if v is None:
        return ""
    return ("{0:"+fmt+"}").format(v)

def DecodeEqualList(txt):
    res={}
    for l in str(txt).splitlines():
        ls=l.split('=',1)
        if len(ls)==2:
            res[ls[0].strip().lower()]=ls[1].strip().lower()
    return res
def EncodeEqualList(map):
    l=["%s=%s"%(k,v) for k,v in map.items()]
    l.sort()
    return "\n".join(l)

def ScaleForDisplay(v):
    """
    Permet de supprimer les decimales supplementaires des flottant en fonctions de la valeur et de ne rien faire au reste
    :param v: valeur à ajuste
    :return: Texte formaté
    """
    if isinstance(v, (float)):
        if(abs(v)<100):
            return "%0.2f"%(v)
        else: return "%0.f"%(v)
    elif v is None:
        return ""
    else:
        return v

def CreateDirConcurrentlyIfNeeded(DirPath:pathlib.Path):
    """
    Permets de créer le répertoire passé en paramètre s'il n'existe pas et le crée si nécessaire.
    Si la création échoue, il teste s'il n'a pas été créé par un autre processus, et dans ce cas ne remonte pas d'erreur.
    :param DirPath: répertoire à créer sous forme de path
    """
    try:
        if not DirPath.exists():
            DirPath.mkdir()
    except Exception as e:
        if not DirPath.exists():
            raise e


def ComputeLimitForImage(imgwidth,imgheight,LimitWidth,LimitHeight):
    width=imgwidth
    height=imgheight
    if width>LimitWidth:
        width=LimitWidth
        height=math.trunc(imgheight*width/imgwidth)
        if height==0: height=1
    if height>LimitHeight:
        height=LimitHeight
        width=math.trunc(imgwidth*height/imgheight)
        if width==0: width=1
    return width,height

def GetAppManagerMailto():
    if 'APPMANAGER_EMAIL' in app.config and 'APPMANAGER_NAME' in app.config:
        return "<a href='mailto:{APPMANAGER_EMAIL}'>{APPMANAGER_NAME} ({APPMANAGER_EMAIL})</a>".format(**app.config)
    return ""

def CalcAstralDayTime(Date,Time,Latitude,Longitude):
    """
    Calcule la position du soleil pour l'heure donnée.
    :param Date: Date UTC
    :param Time:  Heure UTC
    :param Latitude: Latitude
    :param Longitude: Longitude
    :return: D pour Day, U pour Dusk/crépuscule, N pour Night/Nuit, A pour Aube/Dawn
    """
    from astral import Location
    l = Location()
    l.solar_depression= 'nautical'
    l.latitude = Latitude
    l.longitude = Longitude
    s = l.sun(date=Date, local=False)
    # print(Date,Time,Latitude,Longitude,s,)
    Result = '?'
    Inter=( {'d': 'sunrise', 'f': 'sunset' , 'r': 'D'}
          , {'d': 'sunset' , 'f': 'dusk'   , 'r': 'U'}
          , {'d': 'dusk'   , 'f': 'dawn'   , 'r': 'N'}
          , {'d': 'dawn'   , 'f': 'sunrise', 'r': 'A'}
           )
    for I in Inter:
        if s[I['d']].time()<s[I['f']].time() and (Time>=s[I['d']].time() and Time<=s[I['f']].time() ) :
            Result=I['r']
        elif s[I['d']].time() > s[I['f']].time() and (Time >= s[I['d']].time() or Time <= s[I['f']].time()):
            Result = I['r'] # Changement de jour entre les 2 parties de l'intervalle
    return Result

# Ici les imports des modules qui definissent des routes
import appli.main
import appli.adminusers
import appli.tasks.taskmanager
import appli.search.view
import appli.project.view
import appli.part.view

@app.errorhandler(404)
def not_found(e):
    return render_template("errors/404.html"), 404

@app.errorhandler(403)
def forbidden(e):
    return render_template("errors/403.html"), 403

@app.errorhandler(500)
def internal_server_error(e):
    app.logger.exception(e)
    return render_template("errors/500.html"), 500

@app.errorhandler(Exception)
def unhandled_exception(e):
    # Ceci est imperatif si on veux pouvoir avoir des messages d'erreurs à l'écran sous apache
    app.logger.exception(e)
    # Ajout des informations d'exception dans le template custom
    tb_list = traceback.format_tb(e.__traceback__)
    s = "<b>Error:</b> %s <br><b>Description: </b>%s \n<b>Traceback:</b>" % (html.escape(str(e.__class__)), html.escape(str(e)))
    for i in tb_list[::-1]:
        s += "\n" + html.escape(i)
    db.session.rollback()
    return render_template('errors/500.html' ,trace=s), 500

def JinjaFormatDateTime(d,format='%Y-%m-%d %H:%M:%S'):
    if d is None:
        return ""
    return d.strftime(format)

def JinjaNl2BR(t):
    return t.replace('\n', '<br>\n');

def JinjaGetManagerList():
    LstUsers=database.GetAll("""select distinct u.email,u.name,Lower(u.name)
FROM users_roles ur join users u on ur.user_id=u.id
where ur.role_id=2
and u.active=TRUE and email like '%@%'
order by Lower(u.name)""")
    return " ".join(["<li><a href='mailto:{0}'>{1} ({0})</a></li> ".format(*r) for r in LstUsers ])

app.jinja_env.filters['datetime'] = JinjaFormatDateTime
app.jinja_env.filters['nl2br'] = JinjaNl2BR
app.jinja_env.globals.update(GetManagerList=JinjaGetManagerList)

# Traitement du sheduler
from appli import schedule

def scheduler_daily_task():
    app.logger.info("Start Daily Task")
    try:
        with app.app_context():  # Création d'un contexte pour utiliser les fonction GetAll,ExecSQL qui mémorisent
            g.db = None
            import appli.cron

            appli.cron.RefreshAllProjectsStat()
            appli.cron.RefreshTaxoStat()
            app.logger.info(appli.tasks.taskmanager.AutoClean())
    except Exception as e:
        s=str(e)
        tb_list = traceback.format_tb(e.__traceback__)
        for i in tb_list[::-1]:
            s += "\n" + i
        app.logger.error("Exception on Daily Task : %s"%s)
    app.logger.info("End Daily Task")
def scheduler_func():
    # schedule.every(10).seconds.do(scheduler_daily_task)
    schedule.every().day.at("01:15").do(scheduler_daily_task)
    while 1:
        schedule.run_pending()
        time.sleep(1)
@app.before_first_request
def app_before_first_request():
    app.logger.info("Start Daily Task Thread")
    scheduler_thread = threading.Thread(target=scheduler_func,name="Scheduler")
    scheduler_thread.daemon=True
    scheduler_thread.start()