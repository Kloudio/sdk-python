# kloudio.JobsApi

All URIs are relative to *http://localhost:8089*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_job**](JobsApi.md#delete_job) | **DELETE** /v1/jobs/{job_id} | Delete a job
[**disable_job**](JobsApi.md#disable_job) | **POST** /v1/jobs/{job_id}/disable | Disable a job
[**enable_job**](JobsApi.md#enable_job) | **POST** /v1/jobs/{job_id}/enable | Enable a job
[**get_job**](JobsApi.md#get_job) | **GET** /v1/jobs/{job_id} | Get a job
[**jobs_controller_create_job**](JobsApi.md#jobs_controller_create_job) | **POST** /v1/jobs | Create a job
[**jobs_controller_get_jobs**](JobsApi.md#jobs_controller_get_jobs) | **GET** /v1/jobs | Get all jobs
[**jobs_controller_resume_job**](JobsApi.md#jobs_controller_resume_job) | **POST** /v1/jobs/resume | Resume jobs
[**jobs_controller_suspend_job**](JobsApi.md#jobs_controller_suspend_job) | **POST** /v1/jobs/suspend | Suspend jobs
[**jobs_controller_update_job**](JobsApi.md#jobs_controller_update_job) | **PUT** /v1/jobs | Update a job
[**run_job**](JobsApi.md#run_job) | **POST** /v1/jobs/{job_id}/run | Run a job


# **delete_job**
> delete_job(job_id)

Delete a job

Use this method to delete a job by its ID

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
    api_instance = kloudio.JobsApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        # Delete a job
        api_instance.delete_job(job_id)
    except ApiException as e:
        print("Exception when calling JobsApi->delete_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized, check your API key |  -  |
**403** | Forbidden, possible CORS error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_job**
> disable_job(job_id)

Disable a job

Use this method to disable a job by its ID

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
    api_instance = kloudio.JobsApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        # Disable a job
        api_instance.disable_job(job_id)
    except ApiException as e:
        print("Exception when calling JobsApi->disable_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized, check your API key |  -  |
**403** | Forbidden, possible CORS error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_job**
> enable_job(job_id)

Enable a job

Use this method to enable a job by its ID

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
    api_instance = kloudio.JobsApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        # Enable a job
        api_instance.enable_job(job_id)
    except ApiException as e:
        print("Exception when calling JobsApi->enable_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized, check your API key |  -  |
**403** | Forbidden, possible CORS error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> NewJob get_job(job_id)

Get a job

Use this method to get all a job by its ID

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
    api_instance = kloudio.JobsApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        # Get a job
        api_response = api_instance.get_job(job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

[**NewJob**](NewJob.md)

### Authorization

[bearer](../README.md#bearer)

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

# **jobs_controller_create_job**
> NewJob jobs_controller_create_job(new_job)

Create a job

Use this method to create a new job. On successful creation, it returns the job object

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
    api_instance = kloudio.JobsApi(api_client)
    new_job = kloudio.NewJob() # NewJob | To create a new job, send the following properties

    try:
        # Create a job
        api_response = api_instance.jobs_controller_create_job(new_job)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->jobs_controller_create_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_job** | [**NewJob**](NewJob.md)| To create a new job, send the following properties | 

### Return type

[**NewJob**](NewJob.md)

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

# **jobs_controller_get_jobs**
> list[NewJob] jobs_controller_get_jobs()

Get all jobs

Use this method to get all jobs you have created.

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
    api_instance = kloudio.JobsApi(api_client)
    
    try:
        # Get all jobs
        api_response = api_instance.jobs_controller_get_jobs()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->jobs_controller_get_jobs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NewJob]**](NewJob.md)

### Authorization

[bearer](../README.md#bearer)

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

# **jobs_controller_resume_job**
> jobs_controller_resume_job(job_array)

Resume jobs

Use this method to suspend jobs.

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
    api_instance = kloudio.JobsApi(api_client)
    job_array = kloudio.JobArray() # JobArray | To resume a job, pass an array of the job IDs.

    try:
        # Resume jobs
        api_instance.jobs_controller_resume_job(job_array)
    except ApiException as e:
        print("Exception when calling JobsApi->jobs_controller_resume_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_array** | [**JobArray**](JobArray.md)| To resume a job, pass an array of the job IDs. | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad request, check message for more information on the error |  -  |
**401** | Unauthorized, check your API key |  -  |
**403** | Forbidden, possible CORS error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_controller_suspend_job**
> jobs_controller_suspend_job(job_array)

Suspend jobs

Use this method to suspend jobs.

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
    api_instance = kloudio.JobsApi(api_client)
    job_array = kloudio.JobArray() # JobArray | To suspend a job, pass an array of the job IDs.

    try:
        # Suspend jobs
        api_instance.jobs_controller_suspend_job(job_array)
    except ApiException as e:
        print("Exception when calling JobsApi->jobs_controller_suspend_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_array** | [**JobArray**](JobArray.md)| To suspend a job, pass an array of the job IDs. | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad request, check message for more information on the error |  -  |
**401** | Unauthorized, check your API key |  -  |
**403** | Forbidden, possible CORS error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_controller_update_job**
> NewJob jobs_controller_update_job(new_job)

Update a job

Use this method to update a job. On successful update, it returns the job object

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
    api_instance = kloudio.JobsApi(api_client)
    new_job = kloudio.NewJob() # NewJob | To update a job, send the following properties

    try:
        # Update a job
        api_response = api_instance.jobs_controller_update_job(new_job)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->jobs_controller_update_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_job** | [**NewJob**](NewJob.md)| To update a job, send the following properties | 

### Return type

[**NewJob**](NewJob.md)

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

# **run_job**
> run_job(job_id)

Run a job

Use this method to run a job by its ID

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
    api_instance = kloudio.JobsApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        # Run a job
        api_instance.run_job(job_id)
    except ApiException as e:
        print("Exception when calling JobsApi->run_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized, check your API key |  -  |
**403** | Forbidden, possible CORS error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

