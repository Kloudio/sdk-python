# kloud.RegisterApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**register_user**](RegisterApi.md#register_user) | **POST** /v1/register | Register a user

# **register_user**
> register_user(body, api_key)

Register a user

Use this method to register a new user.

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.RegisterApi()
body = kloud.NewUser() # NewUser | 
api_key = 'api_key_example' # str | Enter your API key here

try:
    # Register a user
    api_instance.register_user(body, api_key)
except ApiException as e:
    print("Exception when calling RegisterApi->register_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewUser**](NewUser.md)|  | 
 **api_key** | **str**| Enter your API key here | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

