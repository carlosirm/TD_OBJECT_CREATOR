import  csv ## llamada a la libreria csv.
#string = "hola mundo estoy en Caracas" 
#print(string.replace("Caracas", "Valencia"))


def object_writer(df_valid_obj):

	df_valid_obj = df_valid_obj.reset_index()  # make sure indexes pair with number of rows



	for index, registro in df_valid_obj.iterrows():
		if registro['TARGET_DB_TYPE'] == 'TABLE' and registro['validity'] == True:
			
			
			input_file = open("C:/TMP/"+registro['TARGET_DB']+"/"+registro['tablename']+'.txt', "r", encoding="utf8")
			output_file = open("C:/TERADATA/"+registro['TARGET_DB']+"/"+registro['tablename']+'.sql', "w", encoding="utf8")
			output_file.write("SELECT 1 FROM dbc.tablesv\n")
			output_file.write("WHERE databasename = '" + registro['PARAM_TARGET_DB'] + "' AND TRIM(TABLENAME) = '"+registro['tablename']+"';\n\n")
			output_file.write(".IF ACTIVITYCOUNT = 0 THEN .GOTO NEXT\n\n")
			output_file.write("DROP TABLE " + registro['PARAM_TARGET_DB'] +"."+registro['tablename']+";\n\n")
			output_file.write(".LABEL NEXT\n\n")
			archivo = csv.reader(input_file, delimiter='*')
			for linea in archivo:
				if len(linea) > 0:
					
					linea[0]=linea[0].replace(registro['TARGET_DB'], registro['PARAM_TARGET_DB'])
					linea[0]=linea[0].replace("FALLBACK", "NO FALLBACK")
					linea[0]=linea[0].replace("DEFAULT MERGEBLOCKRATIO,", "DEFAULT MERGEBLOCKRATIO")
					linea[0]=linea[0].replace("MAP = TD_MAP1", "")
					
					output_file.write(linea[0]+"\n")
				
			input_file.close()
			print ('Archivo C:/TERADATA/'+registro['TARGET_DB']+"/"+registro['tablename']+'.sql CREADO')
			output_file.close()
	return 'nada'
	
