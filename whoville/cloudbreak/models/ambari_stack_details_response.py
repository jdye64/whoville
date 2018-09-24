# coding: utf-8

"""
    Cloudbreak API

    Cloudbreak is a powerful left surf that breaks over a coral reef, a mile off southwest the island of Tavarua, Fiji. Cloudbreak is a cloud agnostic Hadoop as a Service API. Abstracts the provisioning and ease management and monitoring of on-demand clusters. SequenceIQ's Cloudbreak is a RESTful application development platform with the goal of helping developers to build solutions for deploying Hadoop YARN clusters in different environments. Once it is deployed in your favourite servlet container it exposes a REST API allowing to span up Hadoop clusters of arbitary sizes and cloud providers. Provisioning Hadoop has never been easier. Cloudbreak is built on the foundation of cloud providers API (Amazon AWS, Microsoft Azure, Google Cloud Platform, Openstack), Apache Ambari, Docker lightweight containers, Swarm and Consul. For further product documentation follow the link: <a href=\"http://hortonworks.com/apache/cloudbreak/\">http://hortonworks.com/apache/cloudbreak/</a>

    OpenAPI spec version: 2.7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AmbariStackDetailsResponse(object):
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
        'stack': 'dict(str, str)',
        'util': 'dict(str, str)',
        'mpacks': 'list[ManagementPackDetails]',
        'enable_gpl_repo': 'bool',
        'verify': 'bool',
        'hdp_version': 'str'
    }

    attribute_map = {
        'stack': 'stack',
        'util': 'util',
        'mpacks': 'mpacks',
        'enable_gpl_repo': 'enableGplRepo',
        'verify': 'verify',
        'hdp_version': 'hdpVersion'
    }

    def __init__(self, stack=None, util=None, mpacks=None, enable_gpl_repo=False, verify=False, hdp_version=None):
        """
        AmbariStackDetailsResponse - a model defined in Swagger
        """

        self._stack = None
        self._util = None
        self._mpacks = None
        self._enable_gpl_repo = None
        self._verify = None
        self._hdp_version = None

        if stack is not None:
          self.stack = stack
        if util is not None:
          self.util = util
        if mpacks is not None:
          self.mpacks = mpacks
        if enable_gpl_repo is not None:
          self.enable_gpl_repo = enable_gpl_repo
        if verify is not None:
          self.verify = verify
        if hdp_version is not None:
          self.hdp_version = hdp_version

    @property
    def stack(self):
        """
        Gets the stack of this AmbariStackDetailsResponse.

        :return: The stack of this AmbariStackDetailsResponse.
        :rtype: dict(str, str)
        """
        return self._stack

    @stack.setter
    def stack(self, stack):
        """
        Sets the stack of this AmbariStackDetailsResponse.

        :param stack: The stack of this AmbariStackDetailsResponse.
        :type: dict(str, str)
        """

        self._stack = stack

    @property
    def util(self):
        """
        Gets the util of this AmbariStackDetailsResponse.

        :return: The util of this AmbariStackDetailsResponse.
        :rtype: dict(str, str)
        """
        return self._util

    @util.setter
    def util(self, util):
        """
        Sets the util of this AmbariStackDetailsResponse.

        :param util: The util of this AmbariStackDetailsResponse.
        :type: dict(str, str)
        """

        self._util = util

    @property
    def mpacks(self):
        """
        Gets the mpacks of this AmbariStackDetailsResponse.

        :return: The mpacks of this AmbariStackDetailsResponse.
        :rtype: list[ManagementPackDetails]
        """
        return self._mpacks

    @mpacks.setter
    def mpacks(self, mpacks):
        """
        Sets the mpacks of this AmbariStackDetailsResponse.

        :param mpacks: The mpacks of this AmbariStackDetailsResponse.
        :type: list[ManagementPackDetails]
        """

        self._mpacks = mpacks

    @property
    def enable_gpl_repo(self):
        """
        Gets the enable_gpl_repo of this AmbariStackDetailsResponse.

        :return: The enable_gpl_repo of this AmbariStackDetailsResponse.
        :rtype: bool
        """
        return self._enable_gpl_repo

    @enable_gpl_repo.setter
    def enable_gpl_repo(self, enable_gpl_repo):
        """
        Sets the enable_gpl_repo of this AmbariStackDetailsResponse.

        :param enable_gpl_repo: The enable_gpl_repo of this AmbariStackDetailsResponse.
        :type: bool
        """

        self._enable_gpl_repo = enable_gpl_repo

    @property
    def verify(self):
        """
        Gets the verify of this AmbariStackDetailsResponse.

        :return: The verify of this AmbariStackDetailsResponse.
        :rtype: bool
        """
        return self._verify

    @verify.setter
    def verify(self, verify):
        """
        Sets the verify of this AmbariStackDetailsResponse.

        :param verify: The verify of this AmbariStackDetailsResponse.
        :type: bool
        """

        self._verify = verify

    @property
    def hdp_version(self):
        """
        Gets the hdp_version of this AmbariStackDetailsResponse.

        :return: The hdp_version of this AmbariStackDetailsResponse.
        :rtype: str
        """
        return self._hdp_version

    @hdp_version.setter
    def hdp_version(self, hdp_version):
        """
        Sets the hdp_version of this AmbariStackDetailsResponse.

        :param hdp_version: The hdp_version of this AmbariStackDetailsResponse.
        :type: str
        """

        self._hdp_version = hdp_version

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
        if not isinstance(other, AmbariStackDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other