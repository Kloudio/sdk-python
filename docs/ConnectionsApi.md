# kloud.ConnectionsApi

All URIs are relative to */*

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
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.ConnectionsApi()
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_connection**
> ConnectionRespose create_connection(body, api_key)

Create a connection

Use this method to create a new connection. On successful creation, it returns the connection object

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.ConnectionsApi()
body = kloud.ConnectionRequest() # ConnectionRequest | To create a new connection, send the following properties
api_key = 'api_key_example' # str | Enter your API key here

try:
    # Create a connection
    api_response = api_instance.create_connection(body, api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->create_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectionRequest**](ConnectionRequest.md)| To create a new connection, send the following properties | 
 **api_key** | **str**| Enter your API key here | 

### Return type

[**ConnectionRespose**](ConnectionRespose.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connection**
> ConnectionDelResponse delete_connection(api_key, connection_id)

Delete a connection

Use this method to delete a connection by the ID

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.ConnectionsApi()
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_connection**
> ConnectionRespose retrieve_connection(api_key, connection_id)

Get a connection

Use this method to get a connection by the ID

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.ConnectionsApi()
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_connections**
> list[ConnectionRespose] retrieve_connections(api_key)

Get all connections

Use this method to get all connections you have created and have been shared with you.

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.ConnectionsApi()
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_connection**
> ConnectionShareResponse share_connection(body, api_key, connection_id)

Share a connection

Use this method to share an existing connection with other members

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.ConnectionsApi()
body = [kloud.ConnectionShareRequest()] # list[ConnectionShareRequest] | 
api_key = 'api_key_example' # str | Enter your API key here
connection_id = 'connection_id_example' # str | 

try:
    # Share a connection
    api_response = api_instance.share_connection(body, api_key, connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->share_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ConnectionShareRequest]**](ConnectionShareRequest.md)|  | 
 **api_key** | **str**| Enter your API key here | 
 **connection_id** | **str**|  | 

### Return type

[**ConnectionShareResponse**](ConnectionShareResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connection**
> ConnectionRespose update_connection(body, api_key, connection_id)

Update a connection

Use this method to update a new connection. To update a connection, pass in the connection_id as a parameter and the properties you wish to change in the body.On successful creation, it returns the updated connection object

### Example
```python
from __future__ import print_function
import time
import kloud
from kloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kloud.ConnectionsApi()
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectionRequest**](ConnectionRequest.md)| Pass in the properties you wish to change as an object in the body of the request | 
 **api_key** | **str**| Enter your API key here | 
 **connection_id** | **str**|  | 

### Return type

[**ConnectionRespose**](ConnectionRespose.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

