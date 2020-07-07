# kloud

- API version: 0.1.BETA
- Package version: 0.09
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import kloud 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import kloud
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.ConnectionsApi(kloud.ApiClient(configuration))
api_key = 'api_key_example' # str | Enter your API key here
connection_id = 'connection_id_example' # str | 

try:
    # Clone a connection
    api_response = api_instance.clone_connection(api_key, connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->clone_connection: %s\n" % e)

# create an instance of the API class
api_instance = kloud.ConnectionsApi(kloud.ApiClient(configuration))
body = kloud.ConnectionRequest() # ConnectionRequest | To create a new connection, send the following properties
api_key = 'api_key_example' # str | Enter your API key here

try:
    # Create a connection
    api_response = api_instance.create_connection(body, api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->create_connection: %s\n" % e)

# create an instance of the API class
api_instance = kloud.ConnectionsApi(kloud.ApiClient(configuration))
api_key = 'api_key_example' # str | Enter your API key here
connection_id = 'connection_id_example' # str | 

try:
    # Delete a connection
    api_response = api_instance.delete_connection(api_key, connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->delete_connection: %s\n" % e)

# create an instance of the API class
api_instance = kloud.ConnectionsApi(kloud.ApiClient(configuration))
api_key = 'api_key_example' # str | Enter your API key here
connection_id = 'connection_id_example' # str | 

try:
    # Get a connection
    api_response = api_instance.retrieve_connection(api_key, connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->retrieve_connection: %s\n" % e)

# create an instance of the API class
api_instance = kloud.ConnectionsApi(kloud.ApiClient(configuration))
api_key = 'api_key_example' # str | Enter your API key here

try:
    # Get all connections
    api_response = api_instance.retrieve_connections(api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->retrieve_connections: %s\n" % e)

# create an instance of the API class
api_instance = kloud.ConnectionsApi(kloud.ApiClient(configuration))
body = [kloud.ConnectionShareRequest()] # list[ConnectionShareRequest] | 
api_key = 'api_key_example' # str | Enter your API key here
connection_id = 'connection_id_example' # str | 

try:
    # Share a connection
    api_response = api_instance.share_connection(body, api_key, connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->share_connection: %s\n" % e)

# create an instance of the API class
api_instance = kloud.ConnectionsApi(kloud.ApiClient(configuration))
body = kloud.ConnectionRequest() # ConnectionRequest | Pass in the properties you wish to change as an object in the body of the request
api_key = 'api_key_example' # str | Enter your API key here
connection_id = 'connection_id_example' # str | 

try:
    # Update a connection
    api_response = api_instance.update_connection(body, api_key, connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->update_connection: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ConnectionsApi* | [**clone_connection**](docs/ConnectionsApi.md#clone_connection) | **POST** /v1/connections/{connection_id} | Clone a connection
*ConnectionsApi* | [**create_connection**](docs/ConnectionsApi.md#create_connection) | **POST** /v1/connections | Create a connection
*ConnectionsApi* | [**delete_connection**](docs/ConnectionsApi.md#delete_connection) | **DELETE** /v1/connections/{connection_id} | Delete a connection
*ConnectionsApi* | [**retrieve_connection**](docs/ConnectionsApi.md#retrieve_connection) | **GET** /v1/connections/{connection_id} | Get a connection
*ConnectionsApi* | [**retrieve_connections**](docs/ConnectionsApi.md#retrieve_connections) | **GET** /v1/connections | Get all connections
*ConnectionsApi* | [**share_connection**](docs/ConnectionsApi.md#share_connection) | **POST** /v1/connections/share/{connection_id} | Share a connection
*ConnectionsApi* | [**update_connection**](docs/ConnectionsApi.md#update_connection) | **PUT** /v1/connections/{connection_id} | Update a connection
*JobsApi* | [**delete_job**](docs/JobsApi.md#delete_job) | **DELETE** /v1/jobs/{job_id} | Delete a job
*JobsApi* | [**disable_job**](docs/JobsApi.md#disable_job) | **POST** /v1/jobs/{job_id}/disable | Disable a job
*JobsApi* | [**enable_job**](docs/JobsApi.md#enable_job) | **POST** /v1/jobs/{job_id}/enable | Enable a job
*JobsApi* | [**get_job**](docs/JobsApi.md#get_job) | **GET** /v1/jobs/{job_id} | Get a job
*JobsApi* | [**jobs_controller_create_job**](docs/JobsApi.md#jobs_controller_create_job) | **POST** /v1/jobs | Create a job
*JobsApi* | [**jobs_controller_get_jobs**](docs/JobsApi.md#jobs_controller_get_jobs) | **GET** /v1/jobs | Get all jobs
*JobsApi* | [**jobs_controller_resume_job**](docs/JobsApi.md#jobs_controller_resume_job) | **POST** /v1/jobs/resume | Resume jobs
*JobsApi* | [**jobs_controller_suspend_job**](docs/JobsApi.md#jobs_controller_suspend_job) | **POST** /v1/jobs/suspend | Suspend jobs
*JobsApi* | [**jobs_controller_update_job**](docs/JobsApi.md#jobs_controller_update_job) | **PUT** /v1/jobs | Update a job
*JobsApi* | [**run_job**](docs/JobsApi.md#run_job) | **POST** /v1/jobs/{job_id}/run | Run a job
*ReportsApi* | [**create_report**](docs/ReportsApi.md#create_report) | **POST** /v1/reports | Create a report
*ReportsApi* | [**delete_report**](docs/ReportsApi.md#delete_report) | **DELETE** /v1/reports/{report_id} | Delete a report
*ReportsApi* | [**execute_report**](docs/ReportsApi.md#execute_report) | **POST** /v1/reports/execute/{report_id} | Execute a report
*ReportsApi* | [**get_report**](docs/ReportsApi.md#get_report) | **GET** /v1/reports/{report_id} | Get a report
*ReportsApi* | [**get_reports**](docs/ReportsApi.md#get_reports) | **GET** /v1/reports | Get all report
*ReportsApi* | [**share_report**](docs/ReportsApi.md#share_report) | **POST** /v1/reports/share/{report_id} | Share a report
*ReportsApi* | [**update_report**](docs/ReportsApi.md#update_report) | **PUT** /v1/reports/{report_id} | Update a report

## Documentation For Models

 - [ConnectionDelResponse](docs/ConnectionDelResponse.md)
 - [ConnectionRequest](docs/ConnectionRequest.md)
 - [ConnectionRespose](docs/ConnectionRespose.md)
 - [ConnectionShareRequest](docs/ConnectionShareRequest.md)
 - [ConnectionShareResponse](docs/ConnectionShareResponse.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [JobArray](docs/JobArray.md)
 - [JobDto](docs/JobDto.md)
 - [ReportDelResponse](docs/ReportDelResponse.md)
 - [ReportShareRequest](docs/ReportShareRequest.md)
 - [ReportShareResponse](docs/ReportShareResponse.md)
 - [ReportsRequest](docs/ReportsRequest.md)
 - [ReportsResponse](docs/ReportsResponse.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author


