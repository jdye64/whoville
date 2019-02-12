# coding: utf-8

"""
    Cloudbreak API

    Cloudbreak is a powerful left surf that breaks over a coral reef, a mile off southwest the island of Tavarua, Fiji. Cloudbreak is a cloud agnostic Hadoop as a Service API. Abstracts the provisioning and ease management and monitoring of on-demand clusters. SequenceIQ's Cloudbreak is a RESTful application development platform with the goal of helping developers to build solutions for deploying Hadoop YARN clusters in different environments. Once it is deployed in your favourite servlet container it exposes a REST API allowing to span up Hadoop clusters of arbitary sizes and cloud providers. Provisioning Hadoop has never been easier. Cloudbreak is built on the foundation of cloud providers API (Amazon AWS, Microsoft Azure, Google Cloud Platform, Openstack), Apache Ambari, Docker lightweight containers, Swarm and Consul. For further product documentation follow the link: <a href=\"http://hortonworks.com/apache/cloudbreak/\">http://hortonworks.com/apache/cloudbreak/</a>

    OpenAPI spec version: 2.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class EncryptionKeyConfigJson(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'id': 'str',
        'description': 'str',
        'display_name': 'str',
        'properties': 'dict(str, object)'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'description': 'description',
        'display_name': 'displayName',
        'properties': 'properties'
    }

    def __init__(self, name=None, id=None, description=None, display_name=None, properties=None):
        """
        EncryptionKeyConfigJson - a model defined in Swagger
        """

        self._name = None
        self._id = None
        self._description = None
        self._display_name = None
        self._properties = None

        if name is not None:
          self.name = name
        if id is not None:
          self.id = id
        if description is not None:
          self.description = description
        if display_name is not None:
          self.display_name = display_name
        if properties is not None:
          self.properties = properties

    @property
    def name(self):
        """
        Gets the name of this EncryptionKeyConfigJson.

        :return: The name of this EncryptionKeyConfigJson.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EncryptionKeyConfigJson.

        :param name: The name of this EncryptionKeyConfigJson.
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """
        Gets the id of this EncryptionKeyConfigJson.

        :return: The id of this EncryptionKeyConfigJson.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EncryptionKeyConfigJson.

        :param id: The id of this EncryptionKeyConfigJson.
        :type: str
        """

        self._id = id

    @property
    def description(self):
        """
        Gets the description of this EncryptionKeyConfigJson.

        :return: The description of this EncryptionKeyConfigJson.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this EncryptionKeyConfigJson.

        :param description: The description of this EncryptionKeyConfigJson.
        :type: str
        """

        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this EncryptionKeyConfigJson.

        :return: The display_name of this EncryptionKeyConfigJson.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this EncryptionKeyConfigJson.

        :param display_name: The display_name of this EncryptionKeyConfigJson.
        :type: str
        """

        self._display_name = display_name

    @property
    def properties(self):
        """
        Gets the properties of this EncryptionKeyConfigJson.

        :return: The properties of this EncryptionKeyConfigJson.
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this EncryptionKeyConfigJson.

        :param properties: The properties of this EncryptionKeyConfigJson.
        :type: dict(str, object)
        """

        self._properties = properties

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, EncryptionKeyConfigJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other