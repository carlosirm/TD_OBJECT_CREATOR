import  csv ## llamada a la libreria csv.
#string = "hola mundo estoy en Caracas" 
#print(string.replace("Caracas", "Valencia"))


def object_writer(df_folder_objets_list):

	df_folder_objets_list = df_folder_objets_list.reset_index()  # make sure indexes pair with number of rows

	for index, registro in df_folder_objets_list.iterrows():
		if registro['TARGET_DB_TYPE'] == 'TABLE':
			print ('imprimiendo registro')
			print (registro)
			#registro = [x.upper() for x in registro] #convertir las base_tabla a mayusculas
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
					
					#db_schema.append(reg[0])
					linea[0]=linea[0].replace(registro['TARGET_DB'], registro['PARAM_TARGET_DB'])
					linea[0]=linea[0].replace("FALLBACK", "NO FALLBACK")
					linea[0]=linea[0].replace("DEFAULT MERGEBLOCKRATIO,", "DEFAULT MERGEBLOCKRATIO")
					linea[0]=linea[0].replace("MAP = TD_MAP1", "")
					#print (linea[0])
					output_file.write(linea[0]+"\n")
				
			input_file.close()
			print ('Archivo /'+registro['TARGET_DB']+"/"+registro['tablename']+'.sql CREADO')
			output_file.close()
	return 'nada'
	
