# kloud.JobsApi

All URIs are relative to */*

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
> delete_job(api_key, job_id)

Delete a job

Use this method to delete a job by its ID

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.JobsApi()
api_key = 'api_key_example' # str | Enter your API key here
job_id = 'job_id_example' # str | 

try:
    # Delete a job
    api_instance.delete_job(api_key, job_id)
except ApiException as e:
    print("Exception when calling JobsApi->delete_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Enter your API key here | 
 **job_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_job**
> disable_job(api_key, job_id)

Disable a job

Use this method to disable a job by its ID

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.JobsApi()
api_key = 'api_key_example' # str | Enter your API key here
job_id = 'job_id_example' # str | 

try:
    # Disable a job
    api_instance.disable_job(api_key, job_id)
except ApiException as e:
    print("Exception when calling JobsApi->disable_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Enter your API key here | 
 **job_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_job**
> enable_job(api_key, job_id)

Enable a job

Use this method to enable a job by its ID

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.JobsApi()
api_key = 'api_key_example' # str | Enter your API key here
job_id = 'job_id_example' # str | 

try:
    # Enable a job
    api_instance.enable_job(api_key, job_id)
except ApiException as e:
    print("Exception when calling JobsApi->enable_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Enter your API key here | 
 **job_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> JobDto get_job(api_key, job_id)

Get a job

Use this method to get all a job by its ID

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.JobsApi()
api_key = 'api_key_example' # str | Enter your API key here
job_id = 'job_id_example' # str | 

try:
    # Get a job
    api_response = api_instance.get_job(api_key, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Enter your API key here | 
 **job_id** | **str**|  | 

### Return type

[**JobDto**](JobDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_controller_create_job**
> JobDto jobs_controller_create_job(body, api_key)

Create a job

Use this method to create a new job. On successful creation, it returns the job object

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.JobsApi()
body = kloud.JobDto() # JobDto | To create a new job, send the following properties
api_key = 'api_key_example' # str | Enter your API key here

try:
    # Create a job
    api_response = api_instance.jobs_controller_create_job(body, api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_controller_create_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobDto**](JobDto.md)| To create a new job, send the following properties | 
 **api_key** | **str**| Enter your API key here | 

### Return type

[**JobDto**](JobDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_controller_get_jobs**
> list[JobDto] jobs_controller_get_jobs(api_key)

Get all jobs

Use this method to get all jobs you have created.

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.JobsApi()
api_key = 'api_key_example' # str | Enter your API key here

try:
    # Get all jobs
    api_response = api_instance.jobs_controller_get_jobs(api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_controller_get_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Enter your API key here | 

### Return type

[**list[JobDto]**](JobDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_controller_resume_job**
> jobs_controller_resume_job(body, api_key)

Resume jobs

Use this method to suspend jobs.

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.JobsApi()
body = kloud.JobArray() # JobArray | To resume a job, pass an array of the job IDs.
api_key = 'api_key_example' # str | Enter your API key here

try:
    # Resume jobs
    api_instance.jobs_controller_resume_job(body, api_key)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_controller_resume_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobArray**](JobArray.md)| To resume a job, pass an array of the job IDs. | 
 **api_key** | **str**| Enter your API key here | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_controller_suspend_job**
> jobs_controller_suspend_job(body, api_key)

Suspend jobs

Use this method to suspend jobs.

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.JobsApi()
body = kloud.JobArray() # JobArray | To suspend a job, pass an array of the job IDs.
api_key = 'api_key_example' # str | Enter your API key here

try:
    # Suspend jobs
    api_instance.jobs_controller_suspend_job(body, api_key)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_controller_suspend_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobArray**](JobArray.md)| To suspend a job, pass an array of the job IDs. | 
 **api_key** | **str**| Enter your API key here | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_controller_update_job**
> JobDto jobs_controller_update_job(body, api_key)

Update a job

Use this method to update a job. On successful update, it returns the job object

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.JobsApi()
body = kloud.JobDto() # JobDto | To update a job, send the following properties
api_key = 'api_key_example' # str | Enter your API key here

try:
    # Update a job
    api_response = api_instance.jobs_controller_update_job(body, api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_controller_update_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobDto**](JobDto.md)| To update a job, send the following properties | 
 **api_key** | **str**| Enter your API key here | 

### Return type

[**JobDto**](JobDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_job**
> run_job(api_key, job_id)

Run a job

Use this method to run a job by its ID

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.JobsApi()
api_key = 'api_key_example' # str | Enter your API key here
job_id = 'job_id_example' # str | 

try:
    # Run a job
    api_instance.run_job(api_key, job_id)
except ApiException as e:
    print("Exception when calling JobsApi->run_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Enter your API key here | 
 **job_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

