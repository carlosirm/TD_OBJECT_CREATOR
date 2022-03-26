import  csv ## llamada a la libreria csv.
#string = "hola mundo estoy en Caracas" 
#print(string.replace("Caracas", "Valencia"))


def object_writer(objetos):
	

	#objetos = [['D_DW_TABLES','NOSIS_PARTY_TELEPHONE'],['D_DW_TABLES','NOSIS_SITUATION']]
	
	for registro in objetos:
		registro = [x.upper() for x in registro] #convertir las base_tabla a mayusculas
		input_file = open("TMP/"+registro[0]+"/"+registro[1]+'.txt', "r", encoding="utf8")
		output_file = open("TERADATA/"+registro[0]+"/"+registro[1]+'.sql', "w", encoding="utf8")
		output_file.write("SELECT 1 FROM dbc.tablesv\n")
		output_file.write("WHERE databasename = '" + registro[0].replace("D_","${DW_AMBIENTE}_") + "' AND TRIM(TABLENAME) = '"+registro[1]+"';\n\n")
		output_file.write(".IF ACTIVITYCOUNT = 0 THEN .GOTO NEXT\n\n")
		output_file.write("DROP TABLE " + registro[0].replace("D_","${DW_AMBIENTE}_") +"."+registro[1]+";\n\n")
		output_file.write(".LABEL NEXT\n\n")
		archivo = csv.reader(input_file, delimiter='*')
		for linea in archivo:
			if len(linea) > 0:
				
				#db_schema.append(reg[0])
				linea[0]=linea[0].replace("D_DW_TABLES", "${DW_AMBIENTE}_DW_TABLES")
				linea[0]=linea[0].replace("D_STAGING", "${DW_AMBIENTE}_STAGING")
				linea[0]=linea[0].replace("D_VIN_STAGING", "${DW_AMBIENTE}_VIN_STAGING")
				linea[0]=linea[0].replace("D_VIN_TABLES", "${DW_AMBIENTE}_VIN_TABLES")
				linea[0]=linea[0].replace("D_DMT_TABLES", "${DW_AMBIENTE}_DMT_TABLES")
				linea[0]=linea[0].replace("FALLBACK", "NO FALLBACK")
				linea[0]=linea[0].replace("DEFAULT MERGEBLOCKRATIO,", "DEFAULT MERGEBLOCKRATIO")
				linea[0]=linea[0].replace("MAP = TD_MAP1", "")
				#print (linea[0])
				output_file.write(linea[0]+"\n")
			
		input_file.close()
		print ('Archivo /'+registro[0]+"/"+registro[1]+'.sql CREADO')
		output_file.close()
	return 'nada'
	
