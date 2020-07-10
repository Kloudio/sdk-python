# kloudio.ConnectionsApi

All URIs are relative to *http://localhost*

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
> ConnectionRespose clone_connection(api_key, connection_id)

Clone a connection

Use this method to clone an existing connection

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
    api_instance = kloudio.ConnectionsApi(api_client)
    api_key = 'api_key_example' # str | Enter your API key here
connection_id = 'connection_id_example' # str | 

    try:
        # Clone a connection
        api_response = api_instance.clone_connection(api_key, connection_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConnectionsApi->clone_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Enter your API key here | 
 **connection_id** | **str**|  | 

### Return type

[**ConnectionRespose**](ConnectionRespose.md)

### Authorization

No authorization required

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
> ConnectionRespose create_connection(api_key, connection_request)

Create a connection

Use this method to create a new connection. On successful creation, it returns the connection object

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
    api_instance = kloudio.ConnectionsApi(api_client)
    api_key = 'api_key_example' # str | Enter your API key here
connection_request = kloudio.ConnectionRequest() # ConnectionRequest | To create a new connection, send the following properties

    try:
        # Create a connection
        api_response = api_instance.create_connection(api_key, connection_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConnectionsApi->create_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Enter your API key here | 
 **connection_request** | [**ConnectionRequest**](ConnectionRequest.md)| To create a new connection, send the following properties | 

### Return type

[**ConnectionRespose**](ConnectionRespose.md)

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

# **delete_connection**
> ConnectionDelResponse delete_connection(api_key, connection_id)

Delete a connection

Use this method to delete a connection by the ID

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
    api_instance = kloudio.ConnectionsApi(api_client)
    api_key = 'api_key_example' # str | Enter your API key here
connection_id = 'connection_id_example' # str | 

    try:
        # Delete a connection
        api_response = api_instance.delete_connection(api_key, connection_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConnectionsApi->delete_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Enter your API key here | 
 **connection_id** | **str**|  | 

### Return type

[**ConnectionDelResponse**](ConnectionDelResponse.md)

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

# **retrieve_connection**
> ConnectionRespose retrieve_connection(api_key, connection_id)

Get a connection

Use this method to get a connection by the ID

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
    api_instance = kloudio.ConnectionsApi(api_client)
    api_key = 'api_key_example' # str | Enter your API key here
connection_id = 'connection_id_example' # str | 

    try:
        # Get a connection
        api_response = api_instance.retrieve_connection(api_key, connection_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConnectionsApi->retrieve_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Enter your API key here | 
 **connection_id** | **str**|  | 

### Return type

[**ConnectionRespose**](ConnectionRespose.md)

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

# **retrieve_connections**
> list[ConnectionRespose] retrieve_connections(api_key)

Get all connections

Use this method to get all connections you have created and have been shared with you.

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
    api_instance = kloudio.ConnectionsApi(api_client)
    api_key = 'api_key_example' # str | Enter your API key here

    try:
        # Get all connections
        api_response = api_instance.retrieve_connections(api_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConnectionsApi->retrieve_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Enter your API key here | 

### Return type

[**list[ConnectionRespose]**](ConnectionRespose.md)

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

# **share_connection**
> ConnectionShareResponse share_connection(api_key, connection_id, connection_share_request)

Share a connection

Use this method to share an existing connection with other members

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
    api_instance = kloudio.ConnectionsApi(api_client)
    api_key = 'api_key_example' # str | Enter your API key here
connection_id = 'connection_id_example' # str | 
connection_share_request = [kloudio.ConnectionShareRequest()] # list[ConnectionShareRequest] | 

    try:
        # Share a connection
        api_response = api_instance.share_connection(api_key, connection_id, connection_share_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConnectionsApi->share_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Enter your API key here | 
 **connection_id** | **str**|  | 
 **connection_share_request** | [**list[ConnectionShareRequest]**](ConnectionShareRequest.md)|  | 

### Return type

[**ConnectionShareResponse**](ConnectionShareResponse.md)

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

# **update_connection**
> ConnectionRespose update_connection(api_key, connection_id, connection_update_request)

Update a connection

Use this method to update a new connection. To update a connection, pass in the connection_id as a parameter and the properties you wish to change in the body.On successful creation, it returns the updated connection object

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
    api_instance = kloudio.ConnectionsApi(api_client)
    api_key = 'api_key_example' # str | Enter your API key here
connection_id = 'connection_id_example' # str | 
connection_update_request = kloudio.ConnectionUpdateRequest() # ConnectionUpdateRequest | Pass in the properties you wish to change as an object in the body of the request

    try:
        # Update a connection
        api_response = api_instance.update_connection(api_key, connection_id, connection_update_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConnectionsApi->update_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Enter your API key here | 
 **connection_id** | **str**|  | 
 **connection_update_request** | [**ConnectionUpdateRequest**](ConnectionUpdateRequest.md)| Pass in the properties you wish to change as an object in the body of the request | 

### Return type

[**ConnectionRespose**](ConnectionRespose.md)

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

