# coding: utf-8

"""
    Kloudio APIs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.BETA
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from kloud.api_client import ApiClient


class LicenseApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_license(self, body, api_key, **kwargs):  # noqa: E501
        """Create a license  # noqa: E501

        Use this method to create a new license.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_license(body, api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NewLicense body: (required)
        :param str api_key: Enter your API key here (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_license_with_http_info(body, api_key, **kwargs)  # noqa: E501
        else:
            (data) = self.create_license_with_http_info(body, api_key, **kwargs)  # noqa: E501
            return data

    def create_license_with_http_info(self, body, api_key, **kwargs):  # noqa: E501
        """Create a license  # noqa: E501

        Use this method to create a new license.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_license_with_http_info(body, api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NewLicense body: (required)
        :param str api_key: Enter your API key here (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'api_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_license" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_license`")  # noqa: E501
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `create_license`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_key' in params:
            header_params['api-key'] = params['api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
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
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_license(self, api_key, account_id, license_id, **kwargs):  # noqa: E501
        """Delete a license  # noqa: E501

        Use this method to delete a license.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_license(api_key, account_id, license_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_key: Enter your API key here (required)
        :param float account_id: (required)
        :param float license_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_license_with_http_info(api_key, account_id, license_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_license_with_http_info(api_key, account_id, license_id, **kwargs)  # noqa: E501
            return data

    def delete_license_with_http_info(self, api_key, account_id, license_id, **kwargs):  # noqa: E501
        """Delete a license  # noqa: E501

        Use this method to delete a license.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_license_with_http_info(api_key, account_id, license_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_key: Enter your API key here (required)
        :param float account_id: (required)
        :param float license_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'account_id', 'license_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_license" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `delete_license`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `delete_license`")  # noqa: E501
        # verify the required parameter 'license_id' is set
        if ('license_id' not in params or
                params['license_id'] is None):
            raise ValueError("Missing the required parameter `license_id` when calling `delete_license`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']  # noqa: E501
        if 'license_id' in params:
            path_params['license_id'] = params['license_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_key' in params:
            header_params['api-key'] = params['api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
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
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_licenses(self, api_key, **kwargs):  # noqa: E501
        """Get all licenses  # noqa: E501

        Use this method to get all licenses.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_licenses(api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_key: Enter your API key here (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_licenses_with_http_info(api_key, **kwargs)  # noqa: E501
        else:
            (data) = self.get_licenses_with_http_info(api_key, **kwargs)  # noqa: E501
            return data

    def get_licenses_with_http_info(self, api_key, **kwargs):  # noqa: E501
        """Get all licenses  # noqa: E501

        Use this method to get all licenses.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_licenses_with_http_info(api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_key: Enter your API key here (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_licenses" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_licenses`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_key' in params:
            header_params['api-key'] = params['api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
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
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_license(self, body, api_key, **kwargs):  # noqa: E501
        """Update a license  # noqa: E501

        Use this method to update a license.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_license(body, api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NewLicense body: (required)
        :param str api_key: Enter your API key here (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_license_with_http_info(body, api_key, **kwargs)  # noqa: E501
        else:
            (data) = self.update_license_with_http_info(body, api_key, **kwargs)  # noqa: E501
            return data

    def update_license_with_http_info(self, body, api_key, **kwargs):  # noqa: E501
        """Update a license  # noqa: E501

        Use this method to update a license.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_license_with_http_info(body, api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NewLicense body: (required)
        :param str api_key: Enter your API key here (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'api_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_license" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_license`")  # noqa: E501
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `update_license`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_key' in params:
            header_params['api-key'] = params['api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
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
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
