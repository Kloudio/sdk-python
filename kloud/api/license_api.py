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


class LicenseApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_license(self, api_key, new_license, **kwargs):  # noqa: E501
        """Create a license  # noqa: E501

        Use this method to create a new license.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_license(api_key, new_license, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str api_key: Enter your API key here (required)
        :param NewLicense new_license: (required)
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
        return self.create_license_with_http_info(api_key, new_license, **kwargs)  # noqa: E501

    def create_license_with_http_info(self, api_key, new_license, **kwargs):  # noqa: E501
        """Create a license  # noqa: E501

        Use this method to create a new license.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_license_with_http_info(api_key, new_license, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str api_key: Enter your API key here (required)
        :param NewLicense new_license: (required)
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
            'new_license'
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
                    " to method create_license" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'api_key' is set
        if self.api_client.client_side_validation and ('api_key' not in local_var_params or  # noqa: E501
                                                        local_var_params['api_key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `api_key` when calling `create_license`")  # noqa: E501
        # verify the required parameter 'new_license' is set
        if self.api_client.client_side_validation and ('new_license' not in local_var_params or  # noqa: E501
                                                        local_var_params['new_license'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `new_license` when calling `create_license`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_key' in local_var_params:
            header_params['api-key'] = local_var_params['api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'new_license' in local_var_params:
            body_params = local_var_params['new_license']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/license', 'POST',
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

    def delete_license(self, api_key, account_id, license_id, **kwargs):  # noqa: E501
        """Delete a license  # noqa: E501

        Use this method to delete a license.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_license(api_key, account_id, license_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str api_key: Enter your API key here (required)
        :param float account_id: (required)
        :param float license_id: (required)
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
        return self.delete_license_with_http_info(api_key, account_id, license_id, **kwargs)  # noqa: E501

    def delete_license_with_http_info(self, api_key, account_id, license_id, **kwargs):  # noqa: E501
        """Delete a license  # noqa: E501

        Use this method to delete a license.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_license_with_http_info(api_key, account_id, license_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str api_key: Enter your API key here (required)
        :param float account_id: (required)
        :param float license_id: (required)
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
            'account_id',
            'license_id'
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
                    " to method delete_license" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'api_key' is set
        if self.api_client.client_side_validation and ('api_key' not in local_var_params or  # noqa: E501
                                                        local_var_params['api_key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `api_key` when calling `delete_license`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if self.api_client.client_side_validation and ('account_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['account_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account_id` when calling `delete_license`")  # noqa: E501
        # verify the required parameter 'license_id' is set
        if self.api_client.client_side_validation and ('license_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['license_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `license_id` when calling `delete_license`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id']  # noqa: E501
        if 'license_id' in local_var_params:
            path_params['license_id'] = local_var_params['license_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_key' in local_var_params:
            header_params['api-key'] = local_var_params['api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/license/{account_id}/{license_id}', 'DELETE',
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

    def get_licenses(self, api_key, **kwargs):  # noqa: E501
        """Get all licenses  # noqa: E501

        Use this method to get all licenses.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_licenses(api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str api_key: Enter your API key here (required)
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
        return self.get_licenses_with_http_info(api_key, **kwargs)  # noqa: E501

    def get_licenses_with_http_info(self, api_key, **kwargs):  # noqa: E501
        """Get all licenses  # noqa: E501

        Use this method to get all licenses.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_licenses_with_http_info(api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str api_key: Enter your API key here (required)
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
            'api_key'
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
                    " to method get_licenses" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'api_key' is set
        if self.api_client.client_side_validation and ('api_key' not in local_var_params or  # noqa: E501
                                                        local_var_params['api_key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `api_key` when calling `get_licenses`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_key' in local_var_params:
            header_params['api-key'] = local_var_params['api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/license', 'GET',
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

    def update_license(self, api_key, new_license, **kwargs):  # noqa: E501
        """Update a license  # noqa: E501

        Use this method to update a license.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_license(api_key, new_license, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str api_key: Enter your API key here (required)
        :param NewLicense new_license: (required)
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
        return self.update_license_with_http_info(api_key, new_license, **kwargs)  # noqa: E501

    def update_license_with_http_info(self, api_key, new_license, **kwargs):  # noqa: E501
        """Update a license  # noqa: E501

        Use this method to update a license.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_license_with_http_info(api_key, new_license, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str api_key: Enter your API key here (required)
        :param NewLicense new_license: (required)
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
            'new_license'
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
                    " to method update_license" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'api_key' is set
        if self.api_client.client_side_validation and ('api_key' not in local_var_params or  # noqa: E501
                                                        local_var_params['api_key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `api_key` when calling `update_license`")  # noqa: E501
        # verify the required parameter 'new_license' is set
        if self.api_client.client_side_validation and ('new_license' not in local_var_params or  # noqa: E501
                                                        local_var_params['new_license'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `new_license` when calling `update_license`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_key' in local_var_params:
            header_params['api-key'] = local_var_params['api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'new_license' in local_var_params:
            body_params = local_var_params['new_license']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/license', 'PUT',
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
