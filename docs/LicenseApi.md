# kloudio.LicenseApi

All URIs are relative to *http://localhost:8089*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_license**](LicenseApi.md#create_license) | **POST** /v1/license | Create a license
[**delete_license**](LicenseApi.md#delete_license) | **DELETE** /v1/license/{license_id} | Delete a license
[**get_licenses**](LicenseApi.md#get_licenses) | **GET** /v1/license | Get all licenses
[**update_license**](LicenseApi.md#update_license) | **PUT** /v1/license | Update a license


# **create_license**
> object create_license(new_license)

Create a license

Use this method to create a new license.

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
    api_instance = kloudio.LicenseApi(api_client)
    new_license = kloudio.NewLicense() # NewLicense | 

    try:
        # Create a license
        api_response = api_instance.create_license(new_license)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LicenseApi->create_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_license** | [**NewLicense**](NewLicense.md)|  | 

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

# **delete_license**
> object delete_license(license_id)

Delete a license

Use this method to delete a license.

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
    api_instance = kloudio.LicenseApi(api_client)
    license_id = 3.4 # float | 

    try:
        # Delete a license
        api_response = api_instance.delete_license(license_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LicenseApi->delete_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_id** | **float**|  | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad request, check message for more information on the error |  -  |
**401** | Unauthorized, check your API key |  -  |
**403** | Forbidden, possible CORS error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_licenses**
> object get_licenses()

Get all licenses

Use this method to get all licenses.

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
    api_instance = kloudio.LicenseApi(api_client)
    
    try:
        # Get all licenses
        api_response = api_instance.get_licenses()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LicenseApi->get_licenses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad request, check message for more information on the error |  -  |
**401** | Unauthorized, check your API key |  -  |
**403** | Forbidden, possible CORS error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_license**
> object update_license(new_license)

Update a license

Use this method to update a license.

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
    api_instance = kloudio.LicenseApi(api_client)
    new_license = kloudio.NewLicense() # NewLicense | 

    try:
        # Update a license
        api_response = api_instance.update_license(new_license)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LicenseApi->update_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_license** | [**NewLicense**](NewLicense.md)|  | 

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

