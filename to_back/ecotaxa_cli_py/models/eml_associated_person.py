# coding: utf-8

"""
    EcoTaxa

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from to_back.ecotaxa_cli_py.configuration import Configuration


class EMLAssociatedPerson(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'given_name': 'str',
        'sur_name': 'str',
        'organization_name': 'str',
        'position_name': 'str',
        'delivery_point': 'str',
        'city': 'str',
        'administrative_area': 'str',
        'postal_code': 'str',
        'country': 'str',
        'phone': 'str',
        'electronic_mail_address': 'str',
        'online_url': 'str',
        'user_id': 'str',
        'role': 'str'
    }

    attribute_map = {
        'given_name': 'givenName',
        'sur_name': 'surName',
        'organization_name': 'organizationName',
        'position_name': 'positionName',
        'delivery_point': 'deliveryPoint',
        'city': 'city',
        'administrative_area': 'administrativeArea',
        'postal_code': 'postalCode',
        'country': 'country',
        'phone': 'phone',
        'electronic_mail_address': 'electronicMailAddress',
        'online_url': 'onlineUrl',
        'user_id': 'userID',
        'role': 'role'
    }

    def __init__(self, given_name=None, sur_name=None, organization_name=None, position_name=None, delivery_point=None, city=None, administrative_area=None, postal_code=None, country=None, phone=None, electronic_mail_address=None, online_url=None, user_id=None, role=None, local_vars_configuration=None):  # noqa: E501
        """EMLAssociatedPerson - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._given_name = None
        self._sur_name = None
        self._organization_name = None
        self._position_name = None
        self._delivery_point = None
        self._city = None
        self._administrative_area = None
        self._postal_code = None
        self._country = None
        self._phone = None
        self._electronic_mail_address = None
        self._online_url = None
        self._user_id = None
        self._role = None
        self.discriminator = None

        if given_name is not None:
            self.given_name = given_name
        if sur_name is not None:
            self.sur_name = sur_name
        self.organization_name = organization_name
        self.position_name = position_name
        if delivery_point is not None:
            self.delivery_point = delivery_point
        if city is not None:
            self.city = city
        if administrative_area is not None:
            self.administrative_area = administrative_area
        if postal_code is not None:
            self.postal_code = postal_code
        self.country = country
        if phone is not None:
            self.phone = phone
        if electronic_mail_address is not None:
            self.electronic_mail_address = electronic_mail_address
        if online_url is not None:
            self.online_url = online_url
        if user_id is not None:
            self.user_id = user_id
        if role is not None:
            self.role = role

    @property
    def given_name(self):
        """Gets the given_name of this EMLAssociatedPerson.  # noqa: E501


        :return: The given_name of this EMLAssociatedPerson.  # noqa: E501
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """Sets the given_name of this EMLAssociatedPerson.


        :param given_name: The given_name of this EMLAssociatedPerson.  # noqa: E501
        :type given_name: str
        """

        self._given_name = given_name

    @property
    def sur_name(self):
        """Gets the sur_name of this EMLAssociatedPerson.  # noqa: E501


        :return: The sur_name of this EMLAssociatedPerson.  # noqa: E501
        :rtype: str
        """
        return self._sur_name

    @sur_name.setter
    def sur_name(self, sur_name):
        """Sets the sur_name of this EMLAssociatedPerson.


        :param sur_name: The sur_name of this EMLAssociatedPerson.  # noqa: E501
        :type sur_name: str
        """

        self._sur_name = sur_name

    @property
    def organization_name(self):
        """Gets the organization_name of this EMLAssociatedPerson.  # noqa: E501


        :return: The organization_name of this EMLAssociatedPerson.  # noqa: E501
        :rtype: str
        """
        return self._organization_name

    @organization_name.setter
    def organization_name(self, organization_name):
        """Sets the organization_name of this EMLAssociatedPerson.


        :param organization_name: The organization_name of this EMLAssociatedPerson.  # noqa: E501
        :type organization_name: str
        """
        if self.local_vars_configuration.client_side_validation and organization_name is None:  # noqa: E501
            raise ValueError("Invalid value for `organization_name`, must not be `None`")  # noqa: E501

        self._organization_name = organization_name

    @property
    def position_name(self):
        """Gets the position_name of this EMLAssociatedPerson.  # noqa: E501


        :return: The position_name of this EMLAssociatedPerson.  # noqa: E501
        :rtype: str
        """
        return self._position_name

    @position_name.setter
    def position_name(self, position_name):
        """Sets the position_name of this EMLAssociatedPerson.


        :param position_name: The position_name of this EMLAssociatedPerson.  # noqa: E501
        :type position_name: str
        """
        if self.local_vars_configuration.client_side_validation and position_name is None:  # noqa: E501
            raise ValueError("Invalid value for `position_name`, must not be `None`")  # noqa: E501

        self._position_name = position_name

    @property
    def delivery_point(self):
        """Gets the delivery_point of this EMLAssociatedPerson.  # noqa: E501


        :return: The delivery_point of this EMLAssociatedPerson.  # noqa: E501
        :rtype: str
        """
        return self._delivery_point

    @delivery_point.setter
    def delivery_point(self, delivery_point):
        """Sets the delivery_point of this EMLAssociatedPerson.


        :param delivery_point: The delivery_point of this EMLAssociatedPerson.  # noqa: E501
        :type delivery_point: str
        """

        self._delivery_point = delivery_point

    @property
    def city(self):
        """Gets the city of this EMLAssociatedPerson.  # noqa: E501


        :return: The city of this EMLAssociatedPerson.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this EMLAssociatedPerson.


        :param city: The city of this EMLAssociatedPerson.  # noqa: E501
        :type city: str
        """

        self._city = city

    @property
    def administrative_area(self):
        """Gets the administrative_area of this EMLAssociatedPerson.  # noqa: E501


        :return: The administrative_area of this EMLAssociatedPerson.  # noqa: E501
        :rtype: str
        """
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, administrative_area):
        """Sets the administrative_area of this EMLAssociatedPerson.


        :param administrative_area: The administrative_area of this EMLAssociatedPerson.  # noqa: E501
        :type administrative_area: str
        """

        self._administrative_area = administrative_area

    @property
    def postal_code(self):
        """Gets the postal_code of this EMLAssociatedPerson.  # noqa: E501


        :return: The postal_code of this EMLAssociatedPerson.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this EMLAssociatedPerson.


        :param postal_code: The postal_code of this EMLAssociatedPerson.  # noqa: E501
        :type postal_code: str
        """

        self._postal_code = postal_code

    @property
    def country(self):
        """Gets the country of this EMLAssociatedPerson.  # noqa: E501


        :return: The country of this EMLAssociatedPerson.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this EMLAssociatedPerson.


        :param country: The country of this EMLAssociatedPerson.  # noqa: E501
        :type country: str
        """
        if self.local_vars_configuration.client_side_validation and country is None:  # noqa: E501
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def phone(self):
        """Gets the phone of this EMLAssociatedPerson.  # noqa: E501


        :return: The phone of this EMLAssociatedPerson.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this EMLAssociatedPerson.


        :param phone: The phone of this EMLAssociatedPerson.  # noqa: E501
        :type phone: str
        """

        self._phone = phone

    @property
    def electronic_mail_address(self):
        """Gets the electronic_mail_address of this EMLAssociatedPerson.  # noqa: E501


        :return: The electronic_mail_address of this EMLAssociatedPerson.  # noqa: E501
        :rtype: str
        """
        return self._electronic_mail_address

    @electronic_mail_address.setter
    def electronic_mail_address(self, electronic_mail_address):
        """Sets the electronic_mail_address of this EMLAssociatedPerson.


        :param electronic_mail_address: The electronic_mail_address of this EMLAssociatedPerson.  # noqa: E501
        :type electronic_mail_address: str
        """

        self._electronic_mail_address = electronic_mail_address

    @property
    def online_url(self):
        """Gets the online_url of this EMLAssociatedPerson.  # noqa: E501


        :return: The online_url of this EMLAssociatedPerson.  # noqa: E501
        :rtype: str
        """
        return self._online_url

    @online_url.setter
    def online_url(self, online_url):
        """Sets the online_url of this EMLAssociatedPerson.


        :param online_url: The online_url of this EMLAssociatedPerson.  # noqa: E501
        :type online_url: str
        """

        self._online_url = online_url

    @property
    def user_id(self):
        """Gets the user_id of this EMLAssociatedPerson.  # noqa: E501


        :return: The user_id of this EMLAssociatedPerson.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this EMLAssociatedPerson.


        :param user_id: The user_id of this EMLAssociatedPerson.  # noqa: E501
        :type user_id: str
        """

        self._user_id = user_id

    @property
    def role(self):
        """Gets the role of this EMLAssociatedPerson.  # noqa: E501


        :return: The role of this EMLAssociatedPerson.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this EMLAssociatedPerson.


        :param role: The role of this EMLAssociatedPerson.  # noqa: E501
        :type role: str
        """

        self._role = role

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EMLAssociatedPerson):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EMLAssociatedPerson):
            return True

        return self.to_dict() != other.to_dict()
