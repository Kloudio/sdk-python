# kloudio.RegisterApi

All URIs are relative to *http://localhost:8089*

Method | HTTP request | Description
------------- | ------------- | -------------
[**register_user**](RegisterApi.md#register_user) | **POST** /v1/register | Register a user


# **register_user**
> object register_user(new_user)

Register a user

Use this method to register a new user.

### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import kloudio
from kloudio.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8089
# See configuration.py for a list of all supported configuration parameters.
configuration = kloudio.Configuration(
    host = "http://localhost:8089"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearer
configuration = kloudio.Configuration(
    host = "http://localhost:8089",
    api_key = {
        'bearer': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with kloudio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kloudio.RegisterApi(api_client)
    new_user = kloudio.NewUser() # NewUser | 

    try:
        # Register a user
        api_response = api_instance.register_user(new_user)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RegisterApi->register_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_user** | [**NewUser**](NewUser.md)|  | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad request, check message for more information on the error |  -  |
**401** | Unauthorized, check your API key |  -  |
**403** | Forbidden, possible CORS error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

