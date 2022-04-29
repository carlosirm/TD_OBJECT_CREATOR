import teradatasql
import os
import shutil # libreria que permite borrar las carpetas de windows que no estan vacias.
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
		os.makedirs("C:/TERADATA/D_DW_VIEWS")
		os.makedirs("C:/TERADATA/D_DMT_VIEWS")
		os.makedirs("C:/TERADATA/D_VIN_VIEWS")
		os.makedirs("C:/TERADATA/ALL_TABLES")
		os.makedirs("C:/TERADATA/ALL_VIEWS")
	except FileExistsError :
		print ("Aviso: El directorio D_D##_VIEWS ya existe")
	
	for reg in lectura:
		db_schema.append(reg[0])
		base_tabla.append(reg)

	db_schema=list(set(db_schema))
	

	for index in range(0,len(db_schema)):
		try:
		   os.makedirs("C:/TERADATA/"+db_schema[index])
		   os.makedirs("C:/TMP/"+db_schema[index])
		except FileExistsError :
		   print ("Aviso: El directorio "+ db_schema[index]+ " ya existe")
   
   
	in_file.close()
	#retorna base.tabla que será usado en otras clases.
	return (base_tabla)

# eliminar los directorios temporales que se estan usando.
def remove_directory():
	shutil.rmtree('C:/TMP')
	#shutil.rmtree('C:/D_STAGING')
	#shutil.rmtree('C:/D_DW_TABLES')
	#shutil.rmtree('C:/D_DMT_TABLES')
	#shutil.rmtree('C:/D_DW_VIEWS')
	#shutil.rmtree('C:/D_DMT_VIEWS')
	#shutil.rmtree('C:/D_VIN_VIEWS')
	return ("Directorio TMP Borrado")
	
	
#td_txt_reader()	

	







