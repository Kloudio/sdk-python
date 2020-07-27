# kloudio.JobsApi

All URIs are relative to *http://localhost:8089*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_job**](JobsApi.md#create_job) | **POST** /v1/jobs | Create a job
[**delete_job**](JobsApi.md#delete_job) | **DELETE** /v1/jobs/{job_id} | Delete a job
[**disable_job**](JobsApi.md#disable_job) | **POST** /v1/jobs/{job_id}/disable | Disable a job
[**enable_job**](JobsApi.md#enable_job) | **POST** /v1/jobs/{job_id}/enable | Enable a job
[**resume_jobs**](JobsApi.md#resume_jobs) | **POST** /v1/jobs/resume | Resume jobs
[**retrieve_job**](JobsApi.md#retrieve_job) | **GET** /v1/jobs/{job_id} | Get a job
[**retrieve_jobs**](JobsApi.md#retrieve_jobs) | **GET** /v1/jobs | Get all jobs
[**run_job**](JobsApi.md#run_job) | **POST** /v1/jobs/{job_id}/run | Run a job
[**suspend_jobs**](JobsApi.md#suspend_jobs) | **POST** /v1/jobs/suspend | Suspend jobs
[**update_job**](JobsApi.md#update_job) | **PUT** /v1/jobs | Update a job


# **create_job**
> object create_job(new_job)

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
        api_response = api_instance.create_job(new_job)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->create_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_job** | [**NewJob**](NewJob.md)| To create a new job, send the following properties | 

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

# **delete_job**
> object delete_job(job_id)

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
        api_response = api_instance.delete_job(job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->delete_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

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
**200** | OK |  -  |
**201** | OK |  -  |
**401** | Unauthorized, check your API key |  -  |
**403** | Forbidden, possible CORS error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_job**
> object disable_job(job_id)

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
        api_response = api_instance.disable_job(job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->disable_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

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
**200** | OK |  -  |
**201** | OK |  -  |
**401** | Unauthorized, check your API key |  -  |
**403** | Forbidden, possible CORS error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_job**
> object enable_job(job_id)

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
        api_response = api_instance.enable_job(job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->enable_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

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
**200** | OK |  -  |
**201** | OK |  -  |
**401** | Unauthorized, check your API key |  -  |
**403** | Forbidden, possible CORS error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_jobs**
> object resume_jobs(jobs_array)

Resume jobs

Use this method to resume jobs.

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
    jobs_array = kloudio.JobsArray() # JobsArray | To resume a job, pass an array of the job IDs.

    try:
        # Resume jobs
        api_response = api_instance.resume_jobs(jobs_array)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->resume_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobs_array** | [**JobsArray**](JobsArray.md)| To resume a job, pass an array of the job IDs. | 

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

# **retrieve_job**
> object retrieve_job(job_id)

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
        api_response = api_instance.retrieve_job(job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->retrieve_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

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
**200** | OK |  -  |
**401** | Unauthorized, check your API key |  -  |
**403** | Forbidden, possible CORS error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_jobs**
> object retrieve_jobs()

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
        api_response = api_instance.retrieve_jobs()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->retrieve_jobs: %s\n" % e)
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
**200** | OK |  -  |
**401** | Unauthorized, check your API key |  -  |
**403** | Forbidden, possible CORS error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_job**
> object run_job(job_id)

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
        api_response = api_instance.run_job(job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->run_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

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
**200** | OK |  -  |
**201** | OK |  -  |
**401** | Unauthorized, check your API key |  -  |
**403** | Forbidden, possible CORS error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_jobs**
> object suspend_jobs(jobs_array)

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
    jobs_array = kloudio.JobsArray() # JobsArray | To suspend a job, pass an array of the job IDs.

    try:
        # Suspend jobs
        api_response = api_instance.suspend_jobs(jobs_array)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->suspend_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobs_array** | [**JobsArray**](JobsArray.md)| To suspend a job, pass an array of the job IDs. | 

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

# **update_job**
> object update_job(new_job)

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
        api_response = api_instance.update_job(new_job)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->update_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_job** | [**NewJob**](NewJob.md)| To update a job, send the following properties | 

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

