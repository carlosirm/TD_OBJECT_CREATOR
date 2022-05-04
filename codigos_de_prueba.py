import teradatasql
import os
from t002_file_manager import directory_creator, td_txt_reader, get_header_data, remove_directory
from t002_parametrized_tbl import object_writer
from t002_object_creator import object_creator
 

lectura_f2 = td_txt_reader('TABLE_VIEW_REL.txt') #incorporacion nueva
header_data = get_header_data(lectura_f2)

lectura_obj = td_txt_reader('td_db_objects.txt')
header_data = get_header_data(lectura_obj)

base_tabla = directory_creator(lectura_obj, lectura_f2)

print ('Llamando a object_creator(header_data) ')
object_creator(header_data, base_tabla)

print ('Llamando a object_writer(base_tabla)')
object_writer(base_tabla)



"""
if 'A' in ['A','B','C']:
	print ('si existe la A')
else:
	print ('no existe')
	"""