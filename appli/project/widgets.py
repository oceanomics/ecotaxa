# -*- coding: utf-8 -*-
# This file is part of Ecotaxa, see license.md in the application root directory for license informations.
# Copyright (C) 2015-2020  Picheral, Colin, Irisson (UPMC-CNRS)
#
# Some classes around displayed parts in page
#
import json
from collections import OrderedDict
from typing import Dict

from appli import ScaleForDisplay, ntcv


class ClassificationPageStats(object):
    """
        Top animated bar with statistics about current project + current filters.
    """

    @staticmethod
    def render(filters, projid):
        # Make API call params from filters
        form_json = json.dumps(filters)
        ajax_call = """
        <script>
            $.ajax({
              type: "POST",
              url: "/api/object_set/%s/summary?only_total=False",
              data: JSON.stringify(%s),""" % (projid, form_json)
        ajax_call += """  
              contentType: "application/json; charset=utf-8",
              dataType: "json",
              success: function(rsp) {
                nbr = rsp['total_objects'];
                if (nbr == 0) {
                  txt_valid = "-";
                  pct_valid = 0;
                  pct_predict = 0;
                  pct_dubious = 0;
                } else {
                  nbr_v = rsp['validated_objects'];
                  nbr_d = rsp['dubious_objects'];
                  nbr_p = rsp['predicted_objects'];
                  nbr_o = nbr - nbr_v - nbr_d - nbr_p;
                  txt_valid = '<span style="color:#0A0">'+nbr_v+' </span>,'+ 
                              '<span style="color:#5bc0de"> '+nbr_p+' </span>,'+ 
                              '<span style="color:#F0AD4E"> '+nbr_d+' </span>,'+
                              '<span style="color:#888"> '+nbr_o+' </span> / '+nbr;
                  pct_valid = Math.round(100 * nbr_v / nbr);
                  pct_predict = Math.round(100 * nbr_p / nbr);
                  pct_dubious = Math.round(100 * nbr_d / nbr);
                }
                $('#objcount').html(txt_valid);
                $('#progress-bar-validated').css('width',pct_valid+'%');
                $('#progress-bar-predicted').css('width',pct_predict+'%');
                $('#progress-bar-dubious').css('width',pct_dubious+'%');
              },
              error: function(jqXHR, textStatus, errorThrown) {
                $('#objcount').html('<span>'+textStatus+errorThrown+'</span>');
              }
            });
        </script>"""
        return ajax_call


class PopoverPane(object):
    """
        A small hint-style window giving a set of information about the image.
    """

    # The fields displayed by default, whatever the setup in the project
    always_there = OrderedDict([("usr.name", "by"),
                                ("txp.name", "parent"),
                                ("sam.orig_id", "in"),
                                ("obj.orig_id", "Image Name"),
                                ("obj.classif_auto_score", "Score"),
                                ("obj.classif_when", "Validation date")])

    def __init__(self, field_list, row):
        """
        """
        self.field_list: OrderedDict = field_list
        self.row: Dict = row

    def render(self, width_on_row):
        row = self.row
        lines = []
        poptitletxt = self.row['obj.orig_id']
        for fld, disp in self.field_list.items():
            if fld == 'obj.orig_id':
                continue
            elif fld == 'usr.name':
                if ntcv(row['usr.name']) != "":
                    lines.append("<em>%s</em> %s" % (disp, row[fld]))
            elif fld == 'txp.name':
                lines.append("<em>%s</em> %s" % (disp, ntcv(row[fld])))
            elif fld == 'sam.orig_id':
                lines.append("<em>%s</em> %s" % (disp, ntcv(row[fld])))
            elif fld == 'obj.classif_auto_score' and row["obj.classif_qual"] == 'V':
                lines.append("%s : %s" % (disp, "-"))
            else:
                lines.append("%s : %s" % (disp, ScaleForDisplay(row[fld])))
        return "data-title=\"{0}\" data-content=\"{1}\" data-placement='{2}'". \
            format(poptitletxt, '<br>'.join(lines), 'left' if width_on_row > 500 else 'right')
