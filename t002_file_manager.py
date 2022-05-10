import teradatasql
import os
import shutil # libreria que permite borrar las carpetas de windows que no estan vacias.
import  csv ## llamada a la libreria csv.

# CREA DIRECTORIOS A PARTIR DE LO LEIDO EN EL ARCHIVO td_db_objects.txt

"""
Function: txt_reader
Reads a txt file.
in: file_name (string) 
out: txt_read ('_csv.reader')
"""
def txt_reader(file_name):
	in_file = open( file_name , "r", encoding="utf8")
	txt_read = csv.reader(in_file, delimiter=',')
	#print (type (txt_read))
	
	return (txt_read)

"""
Function: get_txt_header
return the first line of a txt file. 
in: txt_read ('_csv.reader')
out: header_data ('list')
"""
def get_txt_header(txt_read):
    
	header_data = next(txt_read)
	print ("Obteniendo datos de autenticación...")
	#print (type (header_data))
	return (header_data) 


"""
Function: get_txt_data
return the data content of a txt in a csv.reader format to be iterated.
in: file_name (string) 
out: csv_data ('_csv.reader')
"""
def get_txt_data(file_name):

	csv_data = txt_reader(file_name)
	next(csv_data)

	#in_file = open( file_name , "r", encoding="utf8")
	#csv_data = csv.reader(in_file, delimiter=',')
	#print (csv_data)
	
	return (csv_data) 



def get_folder_objets_list (data_dbo,data_tvr):

	csv_data_tvr = list(data_tvr) # convertir a lista el objecto csv para que sea iterable
	csv_data_dbo = list(data_dbo) # convertir a lista el objecto csv para que sea iterable
	folder_objets_list = []

	#it_num = 0
	
	for l_data_dbo in list(csv_data_dbo):
		
		#it_num = it_num+1
		#print ('iteracion num : ' + str(it_num) )
		#print (l_data_dbo)
		#tvr_num = 0
		#[value.upper() for value in letras]
		for l_data_tvr in list(csv_data_tvr):
			#tvr_num = tvr_num + 1
			#print ('	\niteracion_cd: ' + str(it_num) + str(tvr_num))
			
			print ('	objeto dbo: ' + l_data_dbo[0].upper() + ' objeto tvr: ' + l_data_tvr[0].upper())
			temp_tvr = l_data_tvr[:]
			if l_data_dbo[0].upper() == l_data_tvr[0].upper():
				#print ('		' + l_data_dbo[0].upper() + ' +  ' + l_data_tvr[0].upper())
				temp_tvr.append(l_data_dbo[1].upper())	# and add tablename to complete the list.
				#print ('		Objeto agregado a la lista')
				#print ('		' + str(temp_tvr))
				folder_objets_list.append(temp_tvr)
			

	return (folder_objets_list)


"""
D_dw_tables,DATOS_personales
d_dmt_tables.direcciones

d_dw_tables,d_dw_views,${DW_AMBIENTE}_DW_TABLES,${DW_AMBIENTE}_DW_VIEWS
d_dmt_tables, d_dmt_views,${DW_AMBIENTE}_DW_TABLES, ${DW_AMBIENTE}_DMT_VIEWS
d_vin_tables, d_vin_views,${DW_AMBIENTE}_DW_TABLES,${DW_AMBIENTE}_VIN_VIEWS"""

"""
Function: get_folder_name
Get all the folders to be created, including views folders
in: csv_data_dbo ('_csv.reader') contains all distint tables to be created.
in: csv_data_dbo ('_csv.reader') contains database views related database tables and enviroment variable for these databases
out: folder_name (list)
"""
def get_folder_name (csv_data_dbo,csv_data_tvr):
	folder_name =[]
	#print (csv_data_dbo)
	for l_data_dbo in csv_data_dbo:
		#print (l_data_dbo)
		folder_name.append(l_data_dbo[0].upper())
		folder_name=list(set(folder_name))
	print (folder_name)
	return (folder_name)






def directory_creator(txt_read, txt_read_tvr):

	in_file = open("td_db_objects.txt", "r", encoding="utf8")
	#header_data = next(txt_read)
	#user = header_data[0]
	#password = header_data[0]
	db_schema=[]
	base_tabla=[]
	vistas_db = []
	info_databases = {}
	print ("Creando directorios...")


	# Crear las carpetas de las bases de datos (schema)
	for reg in txt_read:
		print (reg)
		db_schema.append(reg[0].upper())
		base_tabla.append(reg)

	db_schema=list(set(db_schema))

	for tvr in txt_read_tvr:
		"""print (tvr)
		print (tvr[0])
		print (db_schema)"""
		if tvr[0].upper() in db_schema: # Si la tabla esta en la lista de carpetas a crear (table_databases)
			# crear la carpeta de vista equivalente a la tabla
			vistas_db.append(tvr) # agrego las bases de vistas a una lista.
			try:
				os.makedirs("C:/TMP/"+tvr[1].upper())
				os.makedirs("C:/TERADATA/"+tvr[1].upper())
				#print ('crear directorio de vistas ' + tvr[1]) 
			except FileExistsError :
		  		print ("\nAviso: El directorio de vistas "+ tvr[1].upper() + " ya existe")


	for index in range(0,len(db_schema)):

		try:
			os.makedirs("C:/TMP/"+db_schema[index])
			os.makedirs("C:/TERADATA/"+db_schema[index])
		   
		except FileExistsError :
		   print ("Aviso: El directorio "+ db_schema[index]+ " ya existe")
		   """aqui fallaba el programa porque al existir la ruta C:/Teradata saltaba a la excepcion
		   y no llegaba a crear el directorio TMP, lo que hacia que fallara el metodo object_creator al
		   no tener disponible el directorio TMP. """


	in_file.close()
	
	#retorna base.tabla en una clave y en otra devuelve las carpetas de vistas a crear que será usado en otras clases.
	info_databases = {'base_tablas':base_tabla, 'vistas_db':vistas_db} #clave valor de los objetos almacenados
	return (info_databases)
# eliminar los directorios temporales que se estan usando.
	
def remove_directory():
	shutil.rmtree('C:/TMP')
	shutil.rmtree('C:/TERADATA')
	return ("Directorio TMP y TERADATA Borrados")

#txt_reader()	

	







