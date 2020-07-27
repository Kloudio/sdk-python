# NewConnection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the connection, has to be unique for each user, cannot start with numeric characters. | 
**host** | **str** | Host of the connection. To use localhost, please install Kloudio Gateway. | 
**port** | **str** | Port for the connection | 
**database** | **str** | Database name | 
**username** | **str** | Username used for authentication | 
**password** | **str** | Password used for authentication | 
**connection_type** | **str** | Accepted values: CUSTOMERSUCCESS,PAYMENT,CRM,SOCIAL,NOSQL,CLOUDSTORAGE,WEB,FINANCE,DATABASE,ECOMMERCE,AUTOMATION,ERP | 
**db_type** | **str** | Accepted values: MSSQL,INTERCOM,STRIPE,FACEBOOKPAGES,S4HANA,AIRTABLE,SHOPIFY,FRESHSUCCESS,HUBSPOT,ORACLEFINANCIALSCLOUD,FACEBOOKADS,MYSQL,ORACLE,PGSQL,SALESFORCE,SNOWFLAKE,QUICKBOOKSDESKTOP,GITHUB,SQUARE,QUICKBOOKS,SMARTSHEET,MONGODB,NETSUITE,AZURESQL,XERO,ZAPIER,ZENDESKCHAT,GOOGLEADWORDS,GOOGLEADMANAGER,BIGQUERY,AWSATHENA,DYNAMODB,MARIADB,CUSTOMAPI,JIRA,REDSHIFT,ZENDESKSUPPORT,OUTREACH,ANAPLAN,GOOGLEDRIVE,DROPBOX,AMAZONS3,DATABRICKS | 
**production** | **bool** |  | [optional] 
**ssl** | **bool** |  | [optional] 
**share_with** | [**object**](.md) |  | [optional] 
**enable_tunnel** | **bool** |  | [optional] 
**tunnel_info** | [**object**](.md) |  | [optional] 
**other_options** | [**object**](.md) |  | [optional] 
**fed** | **bool** |  | [optional] 
**dw** | **bool** |  | [optional] 
**metadata** | **str** |  | [optional] 
**integration_user_id** | **float** |  | [optional] 
**web_type** | **str** |  | [optional] 
**ssl_info** | [**object**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


