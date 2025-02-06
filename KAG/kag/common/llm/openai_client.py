# -*- coding: utf-8 -*-
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


from openai import OpenAI, AzureOpenAI
import logging

from kag.interface import LLMClient
from typing import Callable

logging.getLogger("openai").setLevel(logging.ERROR)
logging.getLogger("httpx").setLevel(logging.ERROR)
logger = logging.getLogger(__name__)

AzureADTokenProvider = Callable[[], str]


@LLMClient.register("maas")
@LLMClient.register("openai")
class OpenAIClient(LLMClient):
    """
    A client class for interacting with the OpenAI API.

    Initializes the client with an API key, base URL, streaming option, temperature parameter, and default model.

    """

    def __init__(
        self,
        api_key: str,
        base_url: str,
        model: str,
        stream: bool = False,
        temperature: float = 0.7,
        timeout: float = None,
    ):
        """
        Initializes the OpenAIClient instance.

        Args:
            api_key (str): The API key for accessing the OpenAI API.
            base_url (str): The base URL for the OpenAI API.
            model (str): The default model to use for requests.
            stream (bool, optional): Whether to stream the response. Defaults to False.
            temperature (float, optional): The temperature parameter for the model. Defaults to 0.7.
            timeout (float): The timeout duration for the service request. Defaults to None, means no timeout.
        """

        self.api_key = api_key
        self.base_url = base_url
        self.model = model
        self.stream = stream
        self.temperature = temperature
        self.timeout = timeout
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)
        self.check()

    def __call__(self, prompt: str, image_url: str = None):
        """
        Executes a model request when the object is called and returns the result.

        Parameters:
            prompt (str): The prompt provided to the model.

        Returns:
            str: The response content generated by the model.
        """
        # Call the model with the given prompt and return the response
        if image_url:
            message = [
                {"role": "system", "content": "you are a helpful assistant"},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": image_url}},
                    ],
                },
            ]
            response = self.client.chat.completions.create(
                model=self.model,
                messages=message,
                stream=self.stream,
                temperature=self.temperature,
                timeout=self.timeout,
            )
            rsp = response.choices[0].message.content
            return rsp

        else:
            message = [
                {"role": "system", "content": "you are a helpful assistant"},
                {"role": "user", "content": prompt},
            ]
            response = self.client.chat.completions.create(
                model=self.model,
                messages=message,
                stream=self.stream,
                temperature=self.temperature,
                timeout=self.timeout,
            )
            rsp = response.choices[0].message.content
            return rsp


@LLMClient.register("azure_openai")
class AzureOpenAIClient(LLMClient):
    def __init__(
        self,
        api_key: str,
        base_url: str,
        model: str,
        stream: bool = False,
        api_version: str = "2024-12-01-preview",
        temperature: float = 0.7,
        azure_deployment: str = None,
        timeout: float = None,
        azure_ad_token: str = None,
        azure_ad_token_provider: AzureADTokenProvider = None,
    ):
        """
        Initializes the AzureOpenAIClient instance.

        Args:
            api_key (str): The API key for accessing the Azure OpenAI API.
            api_version (str): The API version for the Azure OpenAI API (eg. "2024-12-01-preview, 2024-10-01-preview,2024-05-01-preview").
            base_url (str): The base URL for the Azure OpenAI API.
            azure_deployment (str): The deployment name for the Azure OpenAI model
            model (str): The default model to use for requests.
            stream (bool, optional): Whether to stream the response. Defaults to False.
            temperature (float, optional): The temperature parameter for the model. Defaults to 0.7.
            timeout (float): The timeout duration for the service request. Defaults to None, means no timeout.
            azure_ad_token: Your Azure Active Directory token, https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id
            azure_ad_token_provider: A function that returns an Azure Active Directory token, will be invoked on every request.
            azure_deployment: A model deployment, if given sets the base client URL to include `/deployments/{azure_deployment}`.
                Note: this means you won't be able to use non-deployment endpoints. Not supported with Assistants APIs.
        """

        self.api_key = api_key
        self.base_url = base_url
        self.azure_deployment = azure_deployment
        self.model = model
        self.stream = stream
        self.temperature = temperature
        self.timeout = timeout
        self.api_version = api_version
        self.azure_ad_token = azure_ad_token
        self.azure_ad_token_provider = azure_ad_token_provider
        self.client = AzureOpenAI(
            api_key=self.api_key,
            base_url=self.base_url,
            azure_deployment=self.azure_deployment,
            model=self.model,
            api_version=self.api_version,
            azure_ad_token=self.azure_ad_token,
            azure_ad_token_provider=self.azure_ad_token_provider,
        )
        self.check()

    def __call__(self, prompt: str, image_url: str = None):
        """
        Executes a model request when the object is called and returns the result.

        Parameters:
            prompt (str): The prompt provided to the model.

        Returns:
            str: The response content generated by the model.
        """
        # Call the model with the given prompt and return the response
        if image_url:
            message = [
                {"role": "system", "content": "you are a helpful assistant"},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": image_url}},
                    ],
                },
            ]
            response = self.client.chat.completions.create(
                model=self.model,
                messages=message,
                stream=self.stream,
                temperature=self.temperature,
                timeout=self.timeout,
            )
            rsp = response.choices[0].message.content
            return rsp

        else:
            message = [
                {"role": "system", "content": "you are a helpful assistant"},
                {"role": "user", "content": prompt},
            ]
            response = self.client.chat.completions.create(
                model=self.model,
                messages=message,
                stream=self.stream,
                temperature=self.temperature,
                timeout=self.timeout,
            )
            rsp = response.choices[0].message.content
            return rsp
