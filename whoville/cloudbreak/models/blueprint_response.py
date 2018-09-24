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


class BlueprintResponse(object):
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
        'ambari_blueprint': 'str',
        'description': 'str',
        'inputs': 'list[BlueprintParameter]',
        'tags': 'dict(str, object)',
        'name': 'str',
        'id': 'int',
        'host_group_count': 'int',
        'status': 'str',
        'public': 'bool'
    }

    attribute_map = {
        'ambari_blueprint': 'ambariBlueprint',
        'description': 'description',
        'inputs': 'inputs',
        'tags': 'tags',
        'name': 'name',
        'id': 'id',
        'host_group_count': 'hostGroupCount',
        'status': 'status',
        'public': 'public'
    }

    def __init__(self, ambari_blueprint=None, description=None, inputs=None, tags=None, name=None, id=None, host_group_count=None, status=None, public=False):
        """
        BlueprintResponse - a model defined in Swagger
        """

        self._ambari_blueprint = None
        self._description = None
        self._inputs = None
        self._tags = None
        self._name = None
        self._id = None
        self._host_group_count = None
        self._status = None
        self._public = None

        if ambari_blueprint is not None:
          self.ambari_blueprint = ambari_blueprint
        if description is not None:
          self.description = description
        if inputs is not None:
          self.inputs = inputs
        if tags is not None:
          self.tags = tags
        self.name = name
        if id is not None:
          self.id = id
        if host_group_count is not None:
          self.host_group_count = host_group_count
        if status is not None:
          self.status = status
        if public is not None:
          self.public = public

    @property
    def ambari_blueprint(self):
        """
        Gets the ambari_blueprint of this BlueprintResponse.
        ambari blueprint JSON, set this or the url field

        :return: The ambari_blueprint of this BlueprintResponse.
        :rtype: str
        """
        return self._ambari_blueprint

    @ambari_blueprint.setter
    def ambari_blueprint(self, ambari_blueprint):
        """
        Sets the ambari_blueprint of this BlueprintResponse.
        ambari blueprint JSON, set this or the url field

        :param ambari_blueprint: The ambari_blueprint of this BlueprintResponse.
        :type: str
        """

        self._ambari_blueprint = ambari_blueprint

    @property
    def description(self):
        """
        Gets the description of this BlueprintResponse.
        description of the resource

        :return: The description of this BlueprintResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BlueprintResponse.
        description of the resource

        :param description: The description of this BlueprintResponse.
        :type: str
        """
        if description is not None and len(description) > 1000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1000`")
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")

        self._description = description

    @property
    def inputs(self):
        """
        Gets the inputs of this BlueprintResponse.
        input parameters of the blueprint

        :return: The inputs of this BlueprintResponse.
        :rtype: list[BlueprintParameter]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """
        Sets the inputs of this BlueprintResponse.
        input parameters of the blueprint

        :param inputs: The inputs of this BlueprintResponse.
        :type: list[BlueprintParameter]
        """

        self._inputs = inputs

    @property
    def tags(self):
        """
        Gets the tags of this BlueprintResponse.
        user defined tags for blueprint

        :return: The tags of this BlueprintResponse.
        :rtype: dict(str, object)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this BlueprintResponse.
        user defined tags for blueprint

        :param tags: The tags of this BlueprintResponse.
        :type: dict(str, object)
        """

        self._tags = tags

    @property
    def name(self):
        """
        Gets the name of this BlueprintResponse.
        name of the resource

        :return: The name of this BlueprintResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BlueprintResponse.
        name of the resource

        :param name: The name of this BlueprintResponse.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def id(self):
        """
        Gets the id of this BlueprintResponse.
        id of the resource

        :return: The id of this BlueprintResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BlueprintResponse.
        id of the resource

        :param id: The id of this BlueprintResponse.
        :type: int
        """

        self._id = id

    @property
    def host_group_count(self):
        """
        Gets the host_group_count of this BlueprintResponse.
        number of host groups

        :return: The host_group_count of this BlueprintResponse.
        :rtype: int
        """
        return self._host_group_count

    @host_group_count.setter
    def host_group_count(self, host_group_count):
        """
        Sets the host_group_count of this BlueprintResponse.
        number of host groups

        :param host_group_count: The host_group_count of this BlueprintResponse.
        :type: int
        """

        self._host_group_count = host_group_count

    @property
    def status(self):
        """
        Gets the status of this BlueprintResponse.
        status of the blueprint

        :return: The status of this BlueprintResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this BlueprintResponse.
        status of the blueprint

        :param status: The status of this BlueprintResponse.
        :type: str
        """
        allowed_values = ["DEFAULT", "DEFAULT_DELETED", "USER_MANAGED"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def public(self):
        """
        Gets the public of this BlueprintResponse.
        resource is visible in account

        :return: The public of this BlueprintResponse.
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """
        Sets the public of this BlueprintResponse.
        resource is visible in account

        :param public: The public of this BlueprintResponse.
        :type: bool
        """

        self._public = public

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
        if not isinstance(other, BlueprintResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other