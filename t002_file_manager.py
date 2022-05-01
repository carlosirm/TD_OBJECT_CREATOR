import teradatasql
import os
import shutil # libreria que permite borrar las carpetas de windows que no estan vacias.
import  csv ## llamada a la libreria csv.

# CREA DIRECTORIOS A PARTIR DE LO LEIDO EN EL ARCHIVO td_db_objects.txt


def td_txt_reader(file_name):
	in_file = open( file_name , "r", encoding="utf8")
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

	for reg in lectura:
		db_schema.append(reg[0].upper())
		base_tabla.append(reg)

	db_schema=list(set(db_schema))


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
	#retorna base.tabla que será usado en otras clases.
	return (base_tabla)
# eliminar los directorios temporales que se estan usando.
	
def remove_directory():
	shutil.rmtree('C:/TMP')
	return ("Directorio TMP y TERADATA Borrados")

#td_txt_reader()	

	







