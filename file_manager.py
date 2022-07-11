import teradatasql
import os
import shutil # libreria que permite borrar las carpetas de windows que no estan vacias.
import  csv ## llamada a la libreria csv.
import pandas as pd

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
	return (csv_data) 


"""
Convierte el archivo td_db_objects.txt en un dataframe, excluyendo la primera linea de logueo de usuario.
"""

def dbo_to_dataframe (csv_data):

	#dbname = []
	#tblname = []

	dic = {'databasename':[],'tablename':[]}

	for linea in csv_data:
		dic['databasename'].append(linea[0].upper().strip())	# recorrer y agregar la col 0/databasename al dataframe.
		dic['tablename'].append(linea[1].upper().strip())		# recorrer y agregar la col 1/databasename al dataframe.

	df = pd.DataFrame(dic)
	return (df)

"""
convierte un csv en dataframe
"""
def csv_to_dataframe (filename):
	df = pd.read_csv(filename) 
	return (df) 

"""
Obtiene una lista con los objetos de de tablas y vistas a crear a partir de lista de entrada td_db_objects.txt y table_view_rel.
"""
def get_folder_objets_list (df_dbo,df_tvr):

	df_folder_objets_list = pd.merge(df_dbo, df_tvr, how='left', left_on = 'databasename', right_on = 'SOURCE_DB')
	return (df_folder_objets_list)


"""
Function: get_folder_name
Get all the folders to be created, including views folders
in: df_folder_objets_list (dataframe) contains all distint tables and views to be created.

out: folder_name (list)
"""
def get_folder_name (df_folder_objets_list):
	pd.set_option('display.max_rows', None) 
	folder_name = list(set(df_folder_objets_list["TARGET_DB"]))
	return (folder_name)


# crea las carpetas de tablas y vistas

def set_directory_creator(folder_name):

	for f in folder_name:
		try:
			os.makedirs("C:/TMP/"+ f)
			os.makedirs("C:/TERADATA/"+ f)
			
		except FileExistsError :
	  		print ("\nAviso: El directorio "+ f + " ya existe")
	return 0
# eliminar los directorios temporales que se estan usando.
	
def remove_directory(path):
	directorio = os.path.isdir(path)

	if directorio == True:
		shutil.rmtree(path)
	else:
		print ("\nAviso: No hay directorios que borrar")
	return ("Directorio TMP y TERADATA Borrados")



	







