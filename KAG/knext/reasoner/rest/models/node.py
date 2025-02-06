# coding: utf-8
# Copyright 2023 OpenSPG Authors
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.


"""
    knext

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from knext.common.rest.configuration import Configuration


class Node(object):
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
        "id": "str",
        "state": "str",
        "question": "str",
        "answer": "str",
        "logs": "str",
        'title': 'str',
        'subgraph': 'list[SubGraph]'
    }

    attribute_map = {
        "id": "id",
        "state": "state",
        "question": "question",
        "answer": "answer",
        "logs": "logs",
        'title': 'title',
        'subgraph': 'subgraph'
    }

    def __init__(
        self,
        id=None,
        state=None,
        question=None,
        answer=None,
        logs=None,
        title=None,
        subgraph=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """Node - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._state = None
        self._question = None
        self._answer = None
        self._logs = None
        self._title = None
        self._subgraph = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if state is not None:
            self.state = state
        if question is not None:
            self.question = question
        if answer is not None:
            self.answer = answer
        if logs is not None:
            self.logs = logs
        if title is not None:
            self.title = title
        if subgraph is not None:
            self.subgraph = subgraph

    @property
    def id(self):
        """Gets the id of this Node.  # noqa: E501


        :return: The id of this Node.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Node.


        :param id: The id of this Node.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def state(self):
        """Gets the state of this Node.  # noqa: E501


        :return: The state of this Node.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Node.


        :param state: The state of this Node.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def question(self):
        """Gets the question of this Node.  # noqa: E501


        :return: The question of this Node.  # noqa: E501
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        """Sets the question of this Node.


        :param question: The question of this Node.  # noqa: E501
        :type: str
        """

        self._question = question

    @property
    def answer(self):
        """Gets the answer of this Node.  # noqa: E501


        :return: The answer of this Node.  # noqa: E501
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        """Sets the answer of this Node.


        :param answer: The answer of this Node.  # noqa: E501
        :type: str
        """

        self._answer = answer

    @property
    def logs(self):
        """Gets the logs of this Node.  # noqa: E501


        :return: The logs of this Node.  # noqa: E501
        :rtype: str
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this Node.


        :param logs: The logs of this Node.  # noqa: E501
        :type: str
        """

        self._logs = logs

    @property
    def title(self):
        """Gets the title of this Node.  # noqa: E501


        :return: The title of this Node.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Node.


        :param title: The title of this Node.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def subgraph(self):
        """Gets the subgraph of this Node.  # noqa: E501


        :return: The subgraph of this Node.  # noqa: E501
        :rtype: list[SubGraph]
        """
        return self._subgraph

    @subgraph.setter
    def subgraph(self, subgraph):
        """Sets the subgraph of this Node.


        :param subgraph: The subgraph of this Node.  # noqa: E501
        :type: list[SubGraph]
        """

        self._subgraph = subgraph

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
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
        if not isinstance(other, Node):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Node):
            return True

        return self.to_dict() != other.to_dict()
