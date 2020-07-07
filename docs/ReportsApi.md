# kloud.ReportsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_report**](ReportsApi.md#create_report) | **POST** /v1/reports | Create a report
[**delete_report**](ReportsApi.md#delete_report) | **DELETE** /v1/reports/{report_id} | Delete a report
[**execute_report**](ReportsApi.md#execute_report) | **POST** /v1/reports/execute/{report_id} | Execute a report
[**get_report**](ReportsApi.md#get_report) | **GET** /v1/reports/{report_id} | Get a report
[**get_reports**](ReportsApi.md#get_reports) | **GET** /v1/reports | Get all report
[**share_report**](ReportsApi.md#share_report) | **POST** /v1/reports/share/{report_id} | Share a report
[**update_report**](ReportsApi.md#update_report) | **PUT** /v1/reports/{report_id} | Update a report

# **create_report**
> ReportsResponse create_report(body, api_key)

Create a report

Use this method to create a new report. On successful creation, it returns the report object

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.ReportsApi()
body = kloud.ReportsRequest() # ReportsRequest | To create a new report, send the following properties
api_key = 'api_key_example' # str | Enter your API key here

try:
    # Create a report
    api_response = api_instance.create_report(body, api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->create_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportsRequest**](ReportsRequest.md)| To create a new report, send the following properties | 
 **api_key** | **str**| Enter your API key here | 

### Return type

[**ReportsResponse**](ReportsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_report**
> ReportDelResponse delete_report(api_key, report_id)

Delete a report

Use this method to delete a report.

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.ReportsApi()
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_report**
> execute_report(api_key, report_id)

Execute a report

Use this method to execute a report.

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.ReportsApi()
api_key = 'api_key_example' # str | Enter your API key here
report_id = 'report_id_example' # str | 

try:
    # Execute a report
    api_instance.execute_report(api_key, report_id)
except ApiException as e:
    print("Exception when calling ReportsApi->execute_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Enter your API key here | 
 **report_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report**
> ReportsResponse get_report(api_key, report_id)

Get a report

Use this method to get a report. On successful fetch, it returns the report object

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.ReportsApi()
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports**
> list[ReportsResponse] get_reports(api_key)

Get all report

Use this method to get all report. On successful fetch, it returns the report object

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.ReportsApi()
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_report**
> ReportShareResponse share_report(body, api_key, report_id)

Share a report

Use this method to share a report.

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.ReportsApi()
body = [kloud.ReportShareRequest()] # list[ReportShareRequest] | 
api_key = 'api_key_example' # str | Enter your API key here
report_id = 'report_id_example' # str | 

try:
    # Share a report
    api_response = api_instance.share_report(body, api_key, report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->share_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ReportShareRequest]**](ReportShareRequest.md)|  | 
 **api_key** | **str**| Enter your API key here | 
 **report_id** | **str**|  | 

### Return type

[**ReportShareResponse**](ReportShareResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report**
> ReportsResponse update_report(body, api_key, report_id)

Update a report

Use this method to update an existing report. On successful creation, it returns the updated report object

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.ReportsApi()
body = kloud.ReportsRequest() # ReportsRequest | To update an existing report, send the following properties
api_key = 'api_key_example' # str | Enter your API key here
report_id = 'report_id_example' # str | 

try:
    # Update a report
    api_response = api_instance.update_report(body, api_key, report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->update_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportsRequest**](ReportsRequest.md)| To update an existing report, send the following properties | 
 **api_key** | **str**| Enter your API key here | 
 **report_id** | **str**|  | 

### Return type

[**ReportsResponse**](ReportsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

