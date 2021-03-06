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


class StructuredEventContainer(object):
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
        'flow': 'list[StructuredFlowEvent]',
        'rest': 'list[StructuredRestCallEvent]',
        'notification': 'list[StructuredNotificationEvent]'
    }

    attribute_map = {
        'flow': 'flow',
        'rest': 'rest',
        'notification': 'notification'
    }

    def __init__(self, flow=None, rest=None, notification=None):
        """
        StructuredEventContainer - a model defined in Swagger
        """

        self._flow = None
        self._rest = None
        self._notification = None

        if flow is not None:
          self.flow = flow
        if rest is not None:
          self.rest = rest
        if notification is not None:
          self.notification = notification

    @property
    def flow(self):
        """
        Gets the flow of this StructuredEventContainer.

        :return: The flow of this StructuredEventContainer.
        :rtype: list[StructuredFlowEvent]
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        """
        Sets the flow of this StructuredEventContainer.

        :param flow: The flow of this StructuredEventContainer.
        :type: list[StructuredFlowEvent]
        """

        self._flow = flow

    @property
    def rest(self):
        """
        Gets the rest of this StructuredEventContainer.

        :return: The rest of this StructuredEventContainer.
        :rtype: list[StructuredRestCallEvent]
        """
        return self._rest

    @rest.setter
    def rest(self, rest):
        """
        Sets the rest of this StructuredEventContainer.

        :param rest: The rest of this StructuredEventContainer.
        :type: list[StructuredRestCallEvent]
        """

        self._rest = rest

    @property
    def notification(self):
        """
        Gets the notification of this StructuredEventContainer.

        :return: The notification of this StructuredEventContainer.
        :rtype: list[StructuredNotificationEvent]
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """
        Sets the notification of this StructuredEventContainer.

        :param notification: The notification of this StructuredEventContainer.
        :type: list[StructuredNotificationEvent]
        """

        self._notification = notification

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
        if not isinstance(other, StructuredEventContainer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
