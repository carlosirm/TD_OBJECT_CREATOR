import teradatasql
import os
from t002_file_manager import directory_creator, txt_reader, get_txt_header,get_txt_data, remove_directory,  get_folder_name
from t002_parametrized_tbl import object_writer
from t002_object_creator import object_creator
 

"""
archi = get_txt_data('TABLE_VIEW_REL.txt')
for a in archi:
	print (a)
"""

csv_data_dbo = get_txt_data('td_db_objects.txt')
csv_data_tvr = get_txt_data('TABLE_VIEW_REL.txt')

"""
print (csv_data_dbo)
for c in csv_data_dbo:
	print (c)
"""

get_folder_name (csv_data_dbo,csv_data_tvr )

"""
if 'A' in ['A','B','C']:
	print ('si existe la A')
else:
	print ('no existe')
	"""