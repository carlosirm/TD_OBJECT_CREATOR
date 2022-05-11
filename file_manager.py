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
	csv_data_tvr_len = len(csv_data_tvr)

	it_num = 0
	
	for l_data_dbo in csv_data_dbo:
		l_data_dbo = [value.upper() for value in l_data_dbo]
		it_num = it_num+1
		#print ('iteracion num : ' + str(it_num) )
		#print (l_data_dbo)
		tvr_num = 0
		
		for l_data_tvr in csv_data_tvr:
			l_data_tvr = [value.upper() for value in l_data_tvr]
			tvr_num = tvr_num + 1
			#print ('	\niteracion_cd: ' + str(it_num) + str(tvr_num))
			#print ('	objeto dbo: ' + l_data_dbo[0].upper() + ' objeto tvr: ' + l_data_tvr[0].upper())
			
			temp_tvr = []
	
			# Condicional que agrega los objetos de vistas.
			if l_data_dbo[0] == l_data_tvr[0]:
				#print ('		' + l_data_dbo[0].upper() + ' +  ' + l_data_tvr[0].upper())
				temp_tvr.append(l_data_tvr[0])	# and add databasename to  the list.
				temp_tvr.append(l_data_tvr[2])	# and add paramdatabasename to  the list.
				temp_tvr.append(l_data_dbo[1])	# and add tablename to  the list.
				#print ('		TABLA agregada a la lista')
				#print ('		' + str(temp_tvr))
				folder_objets_list.append(temp_tvr)

				temp_tvr = []

				temp_tvr.append(l_data_tvr[1])	# and add databasename to  the list.
				temp_tvr.append(l_data_tvr[3])	# and add paramdatabasename to  the list.
				temp_tvr.append(l_data_dbo[1])	# and add tablename to  the list.
				#'D_DMT_TABLES', '${DW_AMBIENTE}_DW_TABLES', 'TABLA_DE_PRUEBAS'#
				#print ('		VISTA agregada a la lista')
				#print ('		' + str(temp_tvr))
				folder_objets_list.append(temp_tvr)

				#print ('		Resultado Parcial lado C1')
				#print (folder_objets_list)
				break

			# Si no es vista, se agrega como tabla. Ejemplo una base Staging.
			elif csv_data_tvr_len ==  tvr_num and l_data_dbo[0] != l_data_tvr[0]:
				#print (csv_data_tvr_len) 
				#print (tvr_num)
				#print ('		TABLA STAGING agregada a la lista')
				#print ('		' + str(temp_tvr))
				temp_tvr.append(l_data_dbo[0])	# and add databasename to  the list.
				temp_tvr.append(l_data_tvr[2])	# and add paramdatabasename to  the list.
				temp_tvr.append(l_data_dbo[1])	# and add tablename to  the list.
				folder_objets_list.append(temp_tvr)
				#print ('		Resultado Parcial lado C2')
				#print (folder_objets_list)
	return (folder_objets_list)


"""
Function: get_folder_name
Get all the folders to be created, including views folders
in: csv_data_dbo ('_csv.reader') contains all distint tables to be created.
in: csv_data_dbo ('_csv.reader') contains database views related database tables and enviroment variable for these databases
out: folder_name (list)
"""
def get_folder_name (folder_objets_list):
	folder_name =[]
	#print (csv_data_dbo)
	for folder_objects in folder_objets_list:
		folder_name.append(folder_objects[0].upper())
		folder_name=list(set(folder_name))
	#print (folder_name)
	return (folder_name)

# obtiene la lista de tablas y vistas a crear



def set_directory_creator(folder_name):

	for f in folder_name:
		try:
			os.makedirs("C:/TMP/"+ f)
			os.makedirs("C:/TERADATA/"+ f)
			#print ('crear directorio de vistas ' + tvr[1]) 
		except FileExistsError :
	  		print ("\nAviso: El directorio "+ f + " ya existe")
	return 0
# eliminar los directorios temporales que se estan usando.
	
def remove_directory():
	shutil.rmtree('C:/TMP')
	shutil.rmtree('C:/TERADATA')
	return ("Directorio TMP y TERADATA Borrados")

#txt_reader()	

	







