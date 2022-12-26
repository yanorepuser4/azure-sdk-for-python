# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._channels_operations import (
    build_create_or_update_request,
    build_delete_request,
    build_get_full_url_request,
    build_get_request,
    build_list_by_partner_namespace_request,
    build_update_request,
)

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ChannelsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.eventgrid.aio.EventGridManagementClient`'s
        :attr:`channels` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, partner_namespace_name: str, channel_name: str, **kwargs: Any
    ) -> _models.Channel:
        """Get a channel.

        Get properties of a channel.

        :param resource_group_name: The name of the resource group within the partners subscription.
         Required.
        :type resource_group_name: str
        :param partner_namespace_name: Name of the partner namespace. Required.
        :type partner_namespace_name: str
        :param channel_name: Name of the channel. Required.
        :type channel_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Channel or the result of cls(response)
        :rtype: ~azure.mgmt.eventgrid.models.Channel
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-06-15"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        cls: ClsType[_models.Channel] = kwargs.pop("cls", None)

        request = build_get_request(
            resource_group_name=resource_group_name,
            partner_namespace_name=partner_namespace_name,
            channel_name=channel_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Channel", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerNamespaces/{partnerNamespaceName}/channels/{channelName}"
    }

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        partner_namespace_name: str,
        channel_name: str,
        channel_info: _models.Channel,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Channel:
        """Create or update a channel.

        Synchronously creates or updates a new channel with the specified parameters.

        :param resource_group_name: The name of the resource group within the partners subscription.
         Required.
        :type resource_group_name: str
        :param partner_namespace_name: Name of the partner namespace. Required.
        :type partner_namespace_name: str
        :param channel_name: Name of the channel. Required.
        :type channel_name: str
        :param channel_info: Channel information. Required.
        :type channel_info: ~azure.mgmt.eventgrid.models.Channel
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Channel or the result of cls(response)
        :rtype: ~azure.mgmt.eventgrid.models.Channel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        partner_namespace_name: str,
        channel_name: str,
        channel_info: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Channel:
        """Create or update a channel.

        Synchronously creates or updates a new channel with the specified parameters.

        :param resource_group_name: The name of the resource group within the partners subscription.
         Required.
        :type resource_group_name: str
        :param partner_namespace_name: Name of the partner namespace. Required.
        :type partner_namespace_name: str
        :param channel_name: Name of the channel. Required.
        :type channel_name: str
        :param channel_info: Channel information. Required.
        :type channel_info: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Channel or the result of cls(response)
        :rtype: ~azure.mgmt.eventgrid.models.Channel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        partner_namespace_name: str,
        channel_name: str,
        channel_info: Union[_models.Channel, IO],
        **kwargs: Any
    ) -> _models.Channel:
        """Create or update a channel.

        Synchronously creates or updates a new channel with the specified parameters.

        :param resource_group_name: The name of the resource group within the partners subscription.
         Required.
        :type resource_group_name: str
        :param partner_namespace_name: Name of the partner namespace. Required.
        :type partner_namespace_name: str
        :param channel_name: Name of the channel. Required.
        :type channel_name: str
        :param channel_info: Channel information. Is either a model type or a IO type. Required.
        :type channel_info: ~azure.mgmt.eventgrid.models.Channel or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Channel or the result of cls(response)
        :rtype: ~azure.mgmt.eventgrid.models.Channel
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-06-15"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Channel] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(channel_info, (IO, bytes)):
            _content = channel_info
        else:
            _json = self._serialize.body(channel_info, "Channel")

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            partner_namespace_name=partner_namespace_name,
            channel_name=channel_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_or_update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("Channel", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("Channel", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    create_or_update.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerNamespaces/{partnerNamespaceName}/channels/{channelName}"
    }

    async def _delete_initial(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, partner_namespace_name: str, channel_name: str, **kwargs: Any
    ) -> None:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-06-15"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_delete_request(
            resource_group_name=resource_group_name,
            partner_namespace_name=partner_namespace_name,
            channel_name=channel_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self._delete_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _delete_initial.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerNamespaces/{partnerNamespaceName}/channels/{channelName}"
    }

    @distributed_trace_async
    async def begin_delete(
        self, resource_group_name: str, partner_namespace_name: str, channel_name: str, **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Delete a channel.

        Delete an existing channel.

        :param resource_group_name: The name of the resource group within the partners subscription.
         Required.
        :type resource_group_name: str
        :param partner_namespace_name: Name of the partner namespace. Required.
        :type partner_namespace_name: str
        :param channel_name: Name of the channel. Required.
        :type channel_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-06-15"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._delete_initial(  # type: ignore
                resource_group_name=resource_group_name,
                partner_namespace_name=partner_namespace_name,
                channel_name=channel_name,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    begin_delete.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerNamespaces/{partnerNamespaceName}/channels/{channelName}"
    }

    @overload
    async def update(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        partner_namespace_name: str,
        channel_name: str,
        channel_update_parameters: _models.ChannelUpdateParameters,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """Update a Channel.

        Synchronously updates a channel with the specified parameters.

        :param resource_group_name: The name of the resource group within the partners subscription.
         Required.
        :type resource_group_name: str
        :param partner_namespace_name: Name of the partner namespace. Required.
        :type partner_namespace_name: str
        :param channel_name: Name of the channel. Required.
        :type channel_name: str
        :param channel_update_parameters: Channel update information. Required.
        :type channel_update_parameters: ~azure.mgmt.eventgrid.models.ChannelUpdateParameters
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        partner_namespace_name: str,
        channel_name: str,
        channel_update_parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """Update a Channel.

        Synchronously updates a channel with the specified parameters.

        :param resource_group_name: The name of the resource group within the partners subscription.
         Required.
        :type resource_group_name: str
        :param partner_namespace_name: Name of the partner namespace. Required.
        :type partner_namespace_name: str
        :param channel_name: Name of the channel. Required.
        :type channel_name: str
        :param channel_update_parameters: Channel update information. Required.
        :type channel_update_parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        partner_namespace_name: str,
        channel_name: str,
        channel_update_parameters: Union[_models.ChannelUpdateParameters, IO],
        **kwargs: Any
    ) -> None:
        """Update a Channel.

        Synchronously updates a channel with the specified parameters.

        :param resource_group_name: The name of the resource group within the partners subscription.
         Required.
        :type resource_group_name: str
        :param partner_namespace_name: Name of the partner namespace. Required.
        :type partner_namespace_name: str
        :param channel_name: Name of the channel. Required.
        :type channel_name: str
        :param channel_update_parameters: Channel update information. Is either a model type or a IO
         type. Required.
        :type channel_update_parameters: ~azure.mgmt.eventgrid.models.ChannelUpdateParameters or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-06-15"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(channel_update_parameters, (IO, bytes)):
            _content = channel_update_parameters
        else:
            _json = self._serialize.body(channel_update_parameters, "ChannelUpdateParameters")

        request = build_update_request(
            resource_group_name=resource_group_name,
            partner_namespace_name=partner_namespace_name,
            channel_name=channel_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerNamespaces/{partnerNamespaceName}/channels/{channelName}"
    }

    @distributed_trace
    def list_by_partner_namespace(
        self,
        resource_group_name: str,
        partner_namespace_name: str,
        filter: Optional[str] = None,
        top: Optional[int] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.Channel"]:
        """List channels.

        List all the channels in a partner namespace.

        :param resource_group_name: The name of the resource group within the partners subscription.
         Required.
        :type resource_group_name: str
        :param partner_namespace_name: Name of the partner namespace. Required.
        :type partner_namespace_name: str
        :param filter: The query used to filter the search results using OData syntax. Filtering is
         permitted on the 'name' property only and with limited number of OData operations. These
         operations are: the 'contains' function as well as the following logical operations: not, and,
         or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The
         following is a valid filter example: $filter=contains(namE, 'PATTERN') and name ne 'PATTERN-1'.
         The following is not a valid filter example: $filter=location eq 'westus'. Default value is
         None.
        :type filter: str
        :param top: The number of results to return per page for the list operation. Valid range for
         top parameter is 1 to 100. If not specified, the default number of results to be returned is 20
         items per page. Default value is None.
        :type top: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either Channel or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.eventgrid.models.Channel]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-06-15"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        cls: ClsType[_models.ChannelsListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_partner_namespace_request(
                    resource_group_name=resource_group_name,
                    partner_namespace_name=partner_namespace_name,
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    top=top,
                    api_version=api_version,
                    template_url=self.list_by_partner_namespace.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ChannelsListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list_by_partner_namespace.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerNamespaces/{partnerNamespaceName}/channels"
    }

    @distributed_trace_async
    async def get_full_url(
        self, resource_group_name: str, partner_namespace_name: str, channel_name: str, **kwargs: Any
    ) -> _models.EventSubscriptionFullUrl:
        """Get full URL of partner destination channel.

        Get the full endpoint URL of a partner destination channel.

        :param resource_group_name: The name of the resource group within the partners subscription.
         Required.
        :type resource_group_name: str
        :param partner_namespace_name: Name of the partner namespace. Required.
        :type partner_namespace_name: str
        :param channel_name: Name of the Channel. Required.
        :type channel_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EventSubscriptionFullUrl or the result of cls(response)
        :rtype: ~azure.mgmt.eventgrid.models.EventSubscriptionFullUrl
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-06-15"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        cls: ClsType[_models.EventSubscriptionFullUrl] = kwargs.pop("cls", None)

        request = build_get_full_url_request(
            resource_group_name=resource_group_name,
            partner_namespace_name=partner_namespace_name,
            channel_name=channel_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_full_url.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("EventSubscriptionFullUrl", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_full_url.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerNamespaces/{partnerNamespaceName}/channels/{channelName}/getFullUrl"
    }
