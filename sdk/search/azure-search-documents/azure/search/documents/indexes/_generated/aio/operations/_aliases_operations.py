# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.7, generator: @autorest/python@6.7.8)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, overload
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
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._aliases_operations import (
    build_create_or_update_request,
    build_create_request,
    build_delete_request,
    build_get_request,
    build_list_request,
)
from .._vendor import SearchServiceClientMixinABC

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AliasesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~search_service_client.aio.SearchServiceClient`'s
        :attr:`aliases` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def create(
        self,
        alias: _models.SearchAlias,
        request_options: Optional[_models.RequestOptions] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SearchAlias:
        """Creates a new search alias.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Create-Alias

        :param alias: The definition of the alias to create. Required.
        :type alias: ~search_service_client.models.SearchAlias
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SearchAlias or the result of cls(response)
        :rtype: ~search_service_client.models.SearchAlias
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create(
        self,
        alias: IO,
        request_options: Optional[_models.RequestOptions] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SearchAlias:
        """Creates a new search alias.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Create-Alias

        :param alias: The definition of the alias to create. Required.
        :type alias: IO
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SearchAlias or the result of cls(response)
        :rtype: ~search_service_client.models.SearchAlias
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create(
        self,
        alias: Union[_models.SearchAlias, IO],
        request_options: Optional[_models.RequestOptions] = None,
        **kwargs: Any
    ) -> _models.SearchAlias:
        """Creates a new search alias.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Create-Alias

        :param alias: The definition of the alias to create. Is either a SearchAlias type or a IO type.
         Required.
        :type alias: ~search_service_client.models.SearchAlias or IO
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SearchAlias or the result of cls(response)
        :rtype: ~search_service_client.models.SearchAlias
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.SearchAlias] = kwargs.pop("cls", None)

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(alias, (IOBase, bytes)):
            _content = alias
        else:
            _json = self._serialize.body(alias, "SearchAlias")

        request = build_create_request(
            x_ms_client_request_id=_x_ms_client_request_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("SearchAlias", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    @distributed_trace
    def list(
        self, request_options: Optional[_models.RequestOptions] = None, **kwargs: Any
    ) -> AsyncIterable["_models.SearchAlias"]:
        """Lists all aliases available for a search service.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/List-Aliases

        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SearchAlias or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~search_service_client.models.SearchAlias]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.ListAliasesResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:
                _x_ms_client_request_id = None
                if request_options is not None:
                    _x_ms_client_request_id = request_options.x_ms_client_request_id

                request = build_list_request(
                    x_ms_client_request_id=_x_ms_client_request_id,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

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
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ListAliasesResult", pipeline_response)
            list_of_elem = deserialized.aliases
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @overload
    async def create_or_update(
        self,
        alias_name: str,
        prefer: Union[str, _models.Enum0],
        alias: _models.SearchAlias,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        request_options: Optional[_models.RequestOptions] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SearchAlias:
        """Creates a new search alias or updates an alias if it already exists.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Update-Alias

        :param alias_name: The definition of the alias to create or update. Required.
        :type alias_name: str
        :param prefer: For HTTP PUT requests, instructs the service to return the created/updated
         resource on success. "return=representation" Required.
        :type prefer: str or ~search_service_client.models.Enum0
        :param alias: The definition of the alias to create or update. Required.
        :type alias: ~search_service_client.models.SearchAlias
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value. Default value is None.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value. Default value is None.
        :type if_none_match: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SearchAlias or the result of cls(response)
        :rtype: ~search_service_client.models.SearchAlias
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        alias_name: str,
        prefer: Union[str, _models.Enum0],
        alias: IO,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        request_options: Optional[_models.RequestOptions] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SearchAlias:
        """Creates a new search alias or updates an alias if it already exists.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Update-Alias

        :param alias_name: The definition of the alias to create or update. Required.
        :type alias_name: str
        :param prefer: For HTTP PUT requests, instructs the service to return the created/updated
         resource on success. "return=representation" Required.
        :type prefer: str or ~search_service_client.models.Enum0
        :param alias: The definition of the alias to create or update. Required.
        :type alias: IO
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value. Default value is None.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value. Default value is None.
        :type if_none_match: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SearchAlias or the result of cls(response)
        :rtype: ~search_service_client.models.SearchAlias
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        alias_name: str,
        prefer: Union[str, _models.Enum0],
        alias: Union[_models.SearchAlias, IO],
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        request_options: Optional[_models.RequestOptions] = None,
        **kwargs: Any
    ) -> _models.SearchAlias:
        """Creates a new search alias or updates an alias if it already exists.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Update-Alias

        :param alias_name: The definition of the alias to create or update. Required.
        :type alias_name: str
        :param prefer: For HTTP PUT requests, instructs the service to return the created/updated
         resource on success. "return=representation" Required.
        :type prefer: str or ~search_service_client.models.Enum0
        :param alias: The definition of the alias to create or update. Is either a SearchAlias type or
         a IO type. Required.
        :type alias: ~search_service_client.models.SearchAlias or IO
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value. Default value is None.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value. Default value is None.
        :type if_none_match: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SearchAlias or the result of cls(response)
        :rtype: ~search_service_client.models.SearchAlias
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.SearchAlias] = kwargs.pop("cls", None)

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(alias, (IOBase, bytes)):
            _content = alias
        else:
            _json = self._serialize.body(alias, "SearchAlias")

        request = build_create_or_update_request(
            alias_name=alias_name,
            prefer=prefer,
            x_ms_client_request_id=_x_ms_client_request_id,
            if_match=if_match,
            if_none_match=if_none_match,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if response.status_code == 200:
            deserialized = self._deserialize("SearchAlias", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("SearchAlias", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self,
        alias_name: str,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        request_options: Optional[_models.RequestOptions] = None,
        **kwargs: Any
    ) -> None:
        """Deletes a search alias and its associated mapping to an index. This operation is permanent,
        with no recovery option. The mapped index is untouched by this operation.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Delete-Alias

        :param alias_name: The name of the alias to delete. Required.
        :type alias_name: str
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value. Default value is None.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value. Default value is None.
        :type if_none_match: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
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

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        request = build_delete_request(
            alias_name=alias_name,
            x_ms_client_request_id=_x_ms_client_request_id,
            if_match=if_match,
            if_none_match=if_none_match,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204, 404]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def get(
        self, alias_name: str, request_options: Optional[_models.RequestOptions] = None, **kwargs: Any
    ) -> _models.SearchAlias:
        """Retrieves an alias definition.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Get-Alias

        :param alias_name: The name of the alias to retrieve. Required.
        :type alias_name: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SearchAlias or the result of cls(response)
        :rtype: ~search_service_client.models.SearchAlias
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.SearchAlias] = kwargs.pop("cls", None)

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        request = build_get_request(
            alias_name=alias_name,
            x_ms_client_request_id=_x_ms_client_request_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("SearchAlias", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
