# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.7, generator: @autorest/python@6.7.6)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any

from azure.core import PipelineClient
from azure.core.rest import HttpRequest, HttpResponse

from ._configuration import AzureCommunicationRoomsServiceConfiguration
from ._serialization import Deserializer, Serializer
from .operations import ParticipantsOperations, RoomsOperations


class AzureCommunicationRoomsService:  # pylint: disable=client-accepts-api-version-keyword
    """Azure Communication Room Service.

    :ivar rooms: RoomsOperations operations
    :vartype rooms: azure.communication.rooms.operations.RoomsOperations
    :ivar participants: ParticipantsOperations operations
    :vartype participants: azure.communication.rooms.operations.ParticipantsOperations
    :param endpoint: The endpoint of the Azure Communication resource. Required.
    :type endpoint: str
    :keyword api_version: Api Version. Default value is "2023-10-30-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, endpoint: str, **kwargs: Any
    ) -> None:
        _endpoint = "{endpoint}"
        self._config = AzureCommunicationRoomsServiceConfiguration(endpoint=endpoint, **kwargs)
        self._client: PipelineClient = PipelineClient(base_url=_endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.rooms = RoomsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.participants = ParticipantsOperations(self._client, self._config, self._serialize, self._deserialize)

    def send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "AzureCommunicationRoomsService":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
