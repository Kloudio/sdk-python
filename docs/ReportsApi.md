# kloudio.ReportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_report**](ReportsApi.md#create_report) | **POST** /v1/reports | Create a report
[**delete_report**](ReportsApi.md#delete_report) | **DELETE** /v1/reports/{report_id} | Delete a report
[**execute_report**](ReportsApi.md#execute_report) | **POST** /v1/reports/{report_id}/execute | Execute a report
[**get_report**](ReportsApi.md#get_report) | **GET** /v1/reports/{report_id} | Get a report
[**get_reports**](ReportsApi.md#get_reports) | **GET** /v1/reports | Get all report
[**share_report**](ReportsApi.md#share_report) | **POST** /v1/reports/share/{report_id} | Share a report
[**update_report**](ReportsApi.md#update_report) | **PUT** /v1/reports/{report_id} | Update a report


# **create_report**
> ReportsResponse create_report(api_key, reports_request)

Create a report

Use this method to create a new report. On successful creation, it returns the report object

### Example

```python
from __future__ import print_function
import time
import kloudio
from kloudio.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kloudio.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kloudio.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = kloudio.ReportsApi(api_client)
    api_key = 'api_key_example' # str | Enter your API key here
reports_request = kloudio.ReportsRequest() # ReportsRequest | To create a new report, send the following properties

    try:
        # Create a report
        api_response = api_instance.create_report(api_key, reports_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->create_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Enter your API key here | 
 **reports_request** | [**ReportsRequest**](ReportsRequest.md)| To create a new report, send the following properties | 

### Return type

[**ReportsResponse**](ReportsResponse.md)

### Authorization

No authorization required

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

# **delete_report**
> ReportDelResponse delete_report(api_key, report_id)

Delete a report

Use this method to delete a report.

### Example

```python
from __future__ import print_function
import time
import kloudio
from kloudio.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kloudio.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kloudio.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = kloudio.ReportsApi(api_client)
    api_key = 'api_key_example' # str | Enter your API key here
report_id = 'report_id_example' # str | 

    try:
        # Delete a report
        api_response = api_instance.delete_report(api_key, report_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->delete_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Enter your API key here | 
 **report_id** | **str**|  | 

### Return type

[**ReportDelResponse**](ReportDelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request, check message for more information on the error |  -  |
**401** | Unauthorized, check your API key |  -  |
**403** | Forbidden, possible CORS error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_report**
> execute_report(api_key, report_id, reports_run_request)

Execute a report

Use this method to execute a report.

### Example

```python
from __future__ import print_function
import time
import kloudio
from kloudio.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kloudio.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kloudio.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = kloudio.ReportsApi(api_client)
    api_key = 'api_key_example' # str | Enter your API key here
report_id = 'report_id_example' # str | 
reports_run_request = kloudio.ReportsRunRequest() # ReportsRunRequest | 

    try:
        # Execute a report
        api_instance.execute_report(api_key, report_id, reports_run_request)
    except ApiException as e:
        print("Exception when calling ReportsApi->execute_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Enter your API key here | 
 **report_id** | **str**|  | 
 **reports_run_request** | [**ReportsRunRequest**](ReportsRunRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request, check message for more information on the error |  -  |
**401** | Unauthorized, check your API key |  -  |
**403** | Forbidden, possible CORS error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report**
> ReportsResponse get_report(api_key, report_id)

Get a report

Use this method to get a report. On successful fetch, it returns the report object

### Example

```python
from __future__ import print_function
import time
import kloudio
from kloudio.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kloudio.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kloudio.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = kloudio.ReportsApi(api_client)
    api_key = 'api_key_example' # str | Enter your API key here
report_id = 'report_id_example' # str | 

    try:
        # Get a report
        api_response = api_instance.get_report(api_key, report_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->get_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Enter your API key here | 
 **report_id** | **str**|  | 

### Return type

[**ReportsResponse**](ReportsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request, check message for more information on the error |  -  |
**401** | Unauthorized, check your API key |  -  |
**403** | Forbidden, possible CORS error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports**
> list[ReportsResponse] get_reports(api_key)

Get all report

Use this method to get all report. On successful fetch, it returns the report object

### Example

```python
from __future__ import print_function
import time
import kloudio
from kloudio.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kloudio.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kloudio.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = kloudio.ReportsApi(api_client)
    api_key = 'api_key_example' # str | Enter your API key here

    try:
        # Get all report
        api_response = api_instance.get_reports(api_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->get_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Enter your API key here | 

### Return type

[**list[ReportsResponse]**](ReportsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized, check your API key |  -  |
**403** | Forbidden, possible CORS error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_report**
> ReportShareResponse share_report(api_key, report_id, report_share_request)

Share a report

Use this method to share a report.

### Example

```python
from __future__ import print_function
import time
import kloudio
from kloudio.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kloudio.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kloudio.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = kloudio.ReportsApi(api_client)
    api_key = 'api_key_example' # str | Enter your API key here
report_id = 'report_id_example' # str | 
report_share_request = [kloudio.ReportShareRequest()] # list[ReportShareRequest] | 

    try:
        # Share a report
        api_response = api_instance.share_report(api_key, report_id, report_share_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->share_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Enter your API key here | 
 **report_id** | **str**|  | 
 **report_share_request** | [**list[ReportShareRequest]**](ReportShareRequest.md)|  | 

### Return type

[**ReportShareResponse**](ReportShareResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request, check message for more information on the error |  -  |
**401** | Unauthorized, check your API key |  -  |
**403** | Forbidden, possible CORS error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report**
> ReportsResponse update_report(api_key, report_id, reports_request)

Update a report

Use this method to update an existing report. On successful creation, it returns the updated report object

### Example

```python
from __future__ import print_function
import time
import kloudio
from kloudio.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kloudio.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kloudio.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = kloudio.ReportsApi(api_client)
    api_key = 'api_key_example' # str | Enter your API key here
report_id = 'report_id_example' # str | 
reports_request = kloudio.ReportsRequest() # ReportsRequest | To update an existing report, send the following properties

    try:
        # Update a report
        api_response = api_instance.update_report(api_key, report_id, reports_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->update_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Enter your API key here | 
 **report_id** | **str**|  | 
 **reports_request** | [**ReportsRequest**](ReportsRequest.md)| To update an existing report, send the following properties | 

### Return type

[**ReportsResponse**](ReportsResponse.md)

### Authorization

No authorization required

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

