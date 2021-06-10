# coding: utf-8

"""
    EcoTaxa

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.14
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from to_back.ecotaxa_cli_py.configuration import Configuration


class AcquisitionModel(object):
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
        'acquisid': 'int',
        'acq_sample_id': 'int',
        'orig_id': 'str',
        'instrument': 'str',
        'free_columns': 'object'
    }

    attribute_map = {
        'acquisid': 'acquisid',
        'acq_sample_id': 'acq_sample_id',
        'orig_id': 'orig_id',
        'instrument': 'instrument',
        'free_columns': 'free_columns'
    }

    def __init__(self, acquisid=None, acq_sample_id=None, orig_id=None, instrument=None, free_columns=None, local_vars_configuration=None):  # noqa: E501
        """AcquisitionModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._acquisid = None
        self._acq_sample_id = None
        self._orig_id = None
        self._instrument = None
        self._free_columns = None
        self.discriminator = None

        if acquisid is not None:
            self.acquisid = acquisid
        self.acq_sample_id = acq_sample_id
        self.orig_id = orig_id
        if instrument is not None:
            self.instrument = instrument
        if free_columns is not None:
            self.free_columns = free_columns

    @property
    def acquisid(self):
        """Gets the acquisid of this AcquisitionModel.  # noqa: E501


        :return: The acquisid of this AcquisitionModel.  # noqa: E501
        :rtype: int
        """
        return self._acquisid

    @acquisid.setter
    def acquisid(self, acquisid):
        """Sets the acquisid of this AcquisitionModel.


        :param acquisid: The acquisid of this AcquisitionModel.  # noqa: E501
        :type: int
        """

        self._acquisid = acquisid

    @property
    def acq_sample_id(self):
        """Gets the acq_sample_id of this AcquisitionModel.  # noqa: E501


        :return: The acq_sample_id of this AcquisitionModel.  # noqa: E501
        :rtype: int
        """
        return self._acq_sample_id

    @acq_sample_id.setter
    def acq_sample_id(self, acq_sample_id):
        """Sets the acq_sample_id of this AcquisitionModel.


        :param acq_sample_id: The acq_sample_id of this AcquisitionModel.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and acq_sample_id is None:  # noqa: E501
            raise ValueError("Invalid value for `acq_sample_id`, must not be `None`")  # noqa: E501

        self._acq_sample_id = acq_sample_id

    @property
    def orig_id(self):
        """Gets the orig_id of this AcquisitionModel.  # noqa: E501


        :return: The orig_id of this AcquisitionModel.  # noqa: E501
        :rtype: str
        """
        return self._orig_id

    @orig_id.setter
    def orig_id(self, orig_id):
        """Sets the orig_id of this AcquisitionModel.


        :param orig_id: The orig_id of this AcquisitionModel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and orig_id is None:  # noqa: E501
            raise ValueError("Invalid value for `orig_id`, must not be `None`")  # noqa: E501

        self._orig_id = orig_id

    @property
    def instrument(self):
        """Gets the instrument of this AcquisitionModel.  # noqa: E501


        :return: The instrument of this AcquisitionModel.  # noqa: E501
        :rtype: str
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """Sets the instrument of this AcquisitionModel.


        :param instrument: The instrument of this AcquisitionModel.  # noqa: E501
        :type: str
        """

        self._instrument = instrument

    @property
    def free_columns(self):
        """Gets the free_columns of this AcquisitionModel.  # noqa: E501


        :return: The free_columns of this AcquisitionModel.  # noqa: E501
        :rtype: object
        """
        return self._free_columns

    @free_columns.setter
    def free_columns(self, free_columns):
        """Sets the free_columns of this AcquisitionModel.


        :param free_columns: The free_columns of this AcquisitionModel.  # noqa: E501
        :type: object
        """

        self._free_columns = free_columns

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
        if not isinstance(other, AcquisitionModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AcquisitionModel):
            return True

        return self.to_dict() != other.to_dict()
