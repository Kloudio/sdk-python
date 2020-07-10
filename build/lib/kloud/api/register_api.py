# coding: utf-8

"""
    Kloudio APIs

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.BETA
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from kloud.api_client import ApiClient
from kloud.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class RegisterApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def register_user(self, api_key, new_user, **kwargs):  # noqa: E501
        """Register a user  # noqa: E501

        Use this method to register a new user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.register_user(api_key, new_user, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str api_key: Enter your API key here (required)
        :param NewUser new_user: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.register_user_with_http_info(api_key, new_user, **kwargs)  # noqa: E501

    def register_user_with_http_info(self, api_key, new_user, **kwargs):  # noqa: E501
        """Register a user  # noqa: E501

        Use this method to register a new user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.register_user_with_http_info(api_key, new_user, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str api_key: Enter your API key here (required)
        :param NewUser new_user: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(object, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'api_key',
            'new_user'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method register_user" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'api_key' is set
        if self.api_client.client_side_validation and ('api_key' not in local_var_params or  # noqa: E501
                                                        local_var_params['api_key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `api_key` when calling `register_user`")  # noqa: E501
        # verify the required parameter 'new_user' is set
        if self.api_client.client_side_validation and ('new_user' not in local_var_params or  # noqa: E501
                                                        local_var_params['new_user'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `new_user` when calling `register_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_key' in local_var_params:
            header_params['api-key'] = local_var_params['api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'new_user' in local_var_params:
            body_params = local_var_params['new_user']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/register', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
