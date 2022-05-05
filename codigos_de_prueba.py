import teradatasql
import os
from t002_file_manager import directory_creator, txt_reader, get_txt_header,get_txt_data, remove_directory
from t002_parametrized_tbl import object_writer
from t002_object_creator import object_creator
 

#txt_read_f2 = txt_reader('TABLE_VIEW_REL.txt') #incorporacion nueva
get_txt_data('TABLE_VIEW_REL.txt')


"""
if 'A' in ['A','B','C']:
	print ('si existe la A')
else:
	print ('no existe')
	"""