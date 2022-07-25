# TD_OBJECT_CREATOR
 This it's an automated tool for ETL and Data Developers. It enable you to create production's tables and views packages from develoment enviroment.
 **Warning!**
 Use this at your own convinience and your own risk. Suitable for private and not for cloud enviroment.
 
## Installation
1. **Run a_install_python_libraries**. It contains pip installation of some libraries such ```teradatasql``` and ```pandas```.
2. **Run b_Macro View_Creator** in teradata database into your own teradata database user.

3. **Configure TABLE_VIEW_REL.TXT.** This file contains line by line the relationship between tables, views and enviroment variable in csv format.

	## **Header**
	The first line is the header of the file. Plase don't modify, Risk to breake the application.
	``` TARGET_DB_TYPE,SOURCE_DB,TARGET_DB,PARAM_TARGET_DB,PARAM_SOURCE_DB ```
	
	
	**TARGET_DB_TYPE:** Target's Object type. Only can be TABLE or VIEW.
	
	**SOURCE_DB:** The name of the source database. Example DEV_DWH_TABLES. Please note that this databases starts with 'DEV_' which stand for 'DEVELOPMENT'
	
	**TARGET_DB:** The name of the target database. Here there are two cases.
	
	* If the object it's a TABLE set same as SOURCE_DB.
	
	* If it's a VIEW set the views database related to this table database. 
				
	**PARAM_TARGET_DB:** This is the same as TARGET_DB but you may include an enviroment variable for cases which uses versioners as Serena Dimensions and similars.
	
	**PARAM_SOURCE_DB:** This is the same as SOURCE_DB but you may include an enviroment variable for cases which uses versioners as Serena Dimensions and similars.
	
	## **Data Table Lines**
	
	Set always the same database in all fields and set enviroment variable for PARAM fields if you like.
	```TABLE,DEV_DWH_TABLES,DEV_DWH_TABLES,${DWH_ENVIROMENT}_DWH_TABLES,${DWH_ENVIROMENT}_DWH_TABLES```
	
	## **Data View Lines**
	
	Set the relation between the source tables and the views.
	
	```VIEW,DEV_DWH_TABLES,DEV_DWH_VIEWS,${DWH_ENVIROMENT}_DWH_VIEWS,${DWH_ENVIROMENT}_DWH_TABLES```
	
	## **Staging database**
	
	**Example:** This database has no related view, so there isn't need to add an anditional line for that
	
	```TABLE,DEV_STAGING,DEV_STAGING,${DWH_ENVIROMENT}_STAGING,${DWH_ENVIROMENT}_STAGING```

4. **Configure the td_db_objects.txt.** This file contains the data loggin to the teradata server.
	
	Modify the first line with this structure. 
	IP Server, user , password.
	```192.168.183.128,teradev,teradev```
	
	The sucesive lines supose to be objects in the database with database,tablename format. Set as many as you like.
	Case which databases were configure as DATAWAREHOUSE it automatically will create a 'view script' for the related table.
	```
	dev_dwh_tables,DATOS_personales
	dev_dwh_tables,YIELD_SUMMARY_3FN
	dev_staging,YIELD_SUMMARY_3FN
	dev_staging,YIELD_SUMMARY
	dev_DMT_TABLES,LOCAL_OFFICE
	```
	
	
5.- **Execute objetos_td.bat**
