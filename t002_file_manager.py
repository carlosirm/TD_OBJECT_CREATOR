import teradatasql
import os
import shutil # libreria que permite borrar las carpetas de windows que no estan vacias.
import  csv ## llamada a la libreria csv.

# CREA DIRECTORIOS A PARTIR DE LO LEIDO EN EL ARCHIVO td_db_objects.txt

"""
Lee un objeto txt
"""
def txt_reader(file_name):
	in_file = open( file_name , "r", encoding="utf8")
	txt_read = csv.reader(in_file, delimiter=',')
	
	return (txt_read)

#retorna los datos de logueo.
def get_txt_header(txt_read):
    
	header_data = next(txt_read)
	print ("Obteniendo datos de autenticación...")
	return (header_data) 

def get_txt_data(file_name):
	"""txt_reader(file_name)
	db_objects_list = next(txt_reader(file_name))"""
	db_objects_list = open( file_name , "r", encoding="utf8")
	
	print (db_objects_list)
	for objec in db_objects_list:
		print (objec)
	print ("Obteniendo datos de autenticación...")
	return (db_objects_list) 



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

	







