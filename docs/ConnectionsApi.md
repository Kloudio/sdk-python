# kloudio.ConnectionsApi

All URIs are relative to *http://localhost:8089*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_connection**](ConnectionsApi.md#clone_connection) | **POST** /v1/connections/{connection_id} | Clone a connection
[**create_connection**](ConnectionsApi.md#create_connection) | **POST** /v1/connections | Create a connection
[**delete_connection**](ConnectionsApi.md#delete_connection) | **DELETE** /v1/connections/{connection_id} | Delete a connection
[**retrieve_connection**](ConnectionsApi.md#retrieve_connection) | **GET** /v1/connections/{connection_id} | Get a connection
[**retrieve_connections**](ConnectionsApi.md#retrieve_connections) | **GET** /v1/connections | Get all connections
[**share_connection**](ConnectionsApi.md#share_connection) | **POST** /v1/connections/share/{connection_id} | Share a connection
[**update_connection**](ConnectionsApi.md#update_connection) | **PUT** /v1/connections/{connection_id} | Update a connection


# **clone_connection**
> ConnectionRespose clone_connection(connection_id)

Clone a connection

Use this method to clone an existing connection

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
    api_instance = kloudio.ConnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | 

    try:
        # Clone a connection
        api_response = api_instance.clone_connection(connection_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConnectionsApi->clone_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 

### Return type

[**ConnectionRespose**](ConnectionRespose.md)

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

# **create_connection**
> ConnectionRespose create_connection(new_connection)

Create a connection

Use this method to create a new connection. On successful creation, it returns the connection object

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
    api_instance = kloudio.ConnectionsApi(api_client)
    new_connection = kloudio.NewConnection() # NewConnection | To create a new connection, send the following properties

    try:
        # Create a connection
        api_response = api_instance.create_connection(new_connection)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConnectionsApi->create_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_connection** | [**NewConnection**](NewConnection.md)| To create a new connection, send the following properties | 

### Return type

[**ConnectionRespose**](ConnectionRespose.md)

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

# **delete_connection**
> ConnectionDelResponse delete_connection(connection_id)

Delete a connection

Use this method to delete a connection by the ID

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
    api_instance = kloudio.ConnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | 

    try:
        # Delete a connection
        api_response = api_instance.delete_connection(connection_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConnectionsApi->delete_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 

### Return type

[**ConnectionDelResponse**](ConnectionDelResponse.md)

### Authorization

[bearer](../README.md#bearer)

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

# **retrieve_connection**
> ConnectionRespose retrieve_connection(connection_id)

Get a connection

Use this method to get a connection by the ID

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
    api_instance = kloudio.ConnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | 

    try:
        # Get a connection
        api_response = api_instance.retrieve_connection(connection_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConnectionsApi->retrieve_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 

### Return type

[**ConnectionRespose**](ConnectionRespose.md)

### Authorization

[bearer](../README.md#bearer)

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

# **retrieve_connections**
> list[ConnectionRespose] retrieve_connections()

Get all connections

Use this method to get all connections you have created and have been shared with you.

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
    api_instance = kloudio.ConnectionsApi(api_client)
    
    try:
        # Get all connections
        api_response = api_instance.retrieve_connections()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConnectionsApi->retrieve_connections: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ConnectionRespose]**](ConnectionRespose.md)

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

# **share_connection**
> ConnectionShareResponse share_connection(connection_id, share_connection)

Share a connection

Use this method to share an existing connection with other members

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
    api_instance = kloudio.ConnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | 
share_connection = [kloudio.ShareConnection()] # list[ShareConnection] | 

    try:
        # Share a connection
        api_response = api_instance.share_connection(connection_id, share_connection)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConnectionsApi->share_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 
 **share_connection** | [**list[ShareConnection]**](ShareConnection.md)|  | 

### Return type

[**ConnectionShareResponse**](ConnectionShareResponse.md)

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

# **update_connection**
> ConnectionRespose update_connection(connection_id, update_connection)

Update a connection

Use this method to update a new connection. To update a connection, pass in the connection_id as a parameter and the properties you wish to change in the body.On successful creation, it returns the updated connection object

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
    api_instance = kloudio.ConnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | 
update_connection = kloudio.UpdateConnection() # UpdateConnection | Pass in the properties you wish to change as an object in the body of the request

    try:
        # Update a connection
        api_response = api_instance.update_connection(connection_id, update_connection)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConnectionsApi->update_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 
 **update_connection** | [**UpdateConnection**](UpdateConnection.md)| Pass in the properties you wish to change as an object in the body of the request | 

### Return type

[**ConnectionRespose**](ConnectionRespose.md)

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

