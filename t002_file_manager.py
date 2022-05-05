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

	







