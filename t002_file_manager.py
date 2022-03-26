import teradatasql
import os
import  csv ## llamada a la libreria csv.

# CREA DIRECTORIOS A PARTIR DE LO LEIDO EN EL ARCHIVO td_db_objects.txt


def td_txt_reader():
	in_file = open("td_db_objects.txt", "r", encoding="utf8")
	lectura = csv.reader(in_file, delimiter=',')
	
	return (lectura)


def get_login_data(lectura):
    
	login_data = next(lectura)
	print ("Obteniendo datos de autenticación...")
	return (login_data) #retorna los datos de logueo.

def directory_creator(lectura):
	in_file = open("td_db_objects.txt", "r", encoding="utf8")
	#login_data = next(lectura)
	#user = login_data[0]
	#password = login_data[0]
	db_schema=[]
	base_tabla=[]
	print ("Creando directorios...")
	
	try:
		os.makedirs("TERADATA/D_DW_VIEWS")
		os.makedirs("TERADATA/D_DMT_VIEWS")
		os.makedirs("TERADATA/D_VIN_VIEWS")
		os.makedirs("TERADATA/ALL_TABLES")
		os.makedirs("TERADATA/ALL_VIEWS")
	except FileExistsError :
		print ("Aviso: El directorio D_D##_VIEWS ya existe")
	
	for reg in lectura:
		db_schema.append(reg[0])
		base_tabla.append(reg)

	db_schema=list(set(db_schema))
	

	for index in range(0,len(db_schema)):
		try:
		   os.makedirs("TERADATA/"+db_schema[index])
		   os.makedirs("TMP/"+db_schema[index])
		except FileExistsError :
		   print ("Aviso: El directorio "+ db_schema[index]+ " ya existe")
   
   
	in_file.close()
	#retorna base.tabla que será usado en otras clases.
	return (base_tabla)

def remove_directory():
	os.rmdir('TMP')
	os.rmdir('D_STAGING')
	os.rmdir('D_DW_TABLES')
	os.rmdir('D_DMT_TABLES')
	os.rmdir('D_DW_VIEWS')
	os.rmdir('D_DMT_VIEWS')
	os.rmdir('D_VIN_VIEWS')
	return ("Directorio TMP Borrado")
	
	
#td_txt_reader()	

	







