import teradatasql
import os
from file_manager import set_directory_creator, txt_reader, get_txt_header,get_txt_data, remove_directory,  get_folder_name, get_folder_objets_list,dbo_to_dataframe,csv_to_dataframe
from parametrized_tbl import object_writer
from object_creator import object_creator, get_db_connection
 

#Leer el archivo td_db_objects
csv_data_dbo = get_txt_data('td_db_objects.txt')

# Convertir el archivo csv a un dataframde de pandas.
# Excluye la primera linea de logueo de usuario e internamente
# asigna nombres a las columnas
df_dbo = dbo_to_dataframe (csv_data_dbo)

# Convierte el archivo a un dataframe.
df_tvr = csv_to_dataframe ('TABLE_VIEW_REL.txt')

# Combina los dos dataframes anteriores y obtiene una lista completa
# de todos los objetos a crear.
obj_list = get_folder_objets_list(df_dbo,df_tvr)

# Obtiene los nombres de las carpetas a crear
carpetas = get_folder_name (obj_list)
# Eliminar directorios antes de crear los nuevos.

# Limpia los directorios en caso de que existan.
remove_directory('C:/TMP/')
remove_directory('C:/TERADATA/')

# Crea las carpetas
set_directory_creator (carpetas)

# Open the connection with the DB.
txt_read = txt_reader('td_db_objects.txt')
header_data = get_txt_header (txt_read) 
cursor_actual = get_db_connection(header_data)

object_creator(obj_list,cursor_actual)

object_writer (obj_list)



# Crear Archivos de definicion de tablas en TMP.
# Ejecutar show table


# Abrir archivo en TMP y escribirlo en TERADATA/archivo.sql editado. (cabecera, variables de entorno, etc)