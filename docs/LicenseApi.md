# kloud.LicenseApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_license**](LicenseApi.md#create_license) | **POST** /v1/license | Create a license
[**delete_license**](LicenseApi.md#delete_license) | **DELETE** /v1/license/{account_id}/{license_id} | Delete a license
[**get_licenses**](LicenseApi.md#get_licenses) | **GET** /v1/license | Get all licenses
[**update_license**](LicenseApi.md#update_license) | **PUT** /v1/license | Update a license

# **create_license**
> create_license(body, api_key)

Create a license

Use this method to create a new license.

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.LicenseApi()
body = kloud.NewLicense() # NewLicense | 
api_key = 'api_key_example' # str | Enter your API key here

try:
    # Create a license
    api_instance.create_license(body, api_key)
except ApiException as e:
    print("Exception when calling LicenseApi->create_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewLicense**](NewLicense.md)|  | 
 **api_key** | **str**| Enter your API key here | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_license**
> delete_license(api_key, account_id, license_id)

Delete a license

Use this method to delete a license.

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.LicenseApi()
api_key = 'api_key_example' # str | Enter your API key here
account_id = 1.2 # float | 
license_id = 1.2 # float | 

try:
    # Delete a license
    api_instance.delete_license(api_key, account_id, license_id)
except ApiException as e:
    print("Exception when calling LicenseApi->delete_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Enter your API key here | 
 **account_id** | **float**|  | 
 **license_id** | **float**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_licenses**
> get_licenses(api_key)

Get all licenses

Use this method to get all licenses.

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.LicenseApi()
api_key = 'api_key_example' # str | Enter your API key here

try:
    # Get all licenses
    api_instance.get_licenses(api_key)
except ApiException as e:
    print("Exception when calling LicenseApi->get_licenses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Enter your API key here | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_license**
> update_license(body, api_key)

Update a license

Use this method to update a license.

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.LicenseApi()
body = kloud.NewLicense() # NewLicense | 
api_key = 'api_key_example' # str | Enter your API key here

try:
    # Update a license
    api_instance.update_license(body, api_key)
except ApiException as e:
    print("Exception when calling LicenseApi->update_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewLicense**](NewLicense.md)|  | 
 **api_key** | **str**| Enter your API key here | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

