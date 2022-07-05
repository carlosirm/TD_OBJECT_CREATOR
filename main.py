import teradatasql
import os
from file_manager import set_directory_creator, txt_reader, get_txt_header,get_txt_data, remove_directory,  get_folder_name, get_folder_objets_list
from parametrized_tbl import object_writer
from object_creator import object_creator
 

remove_directory('C:/TMP/')
remove_directory('C:/TERADATA/')
csv_data_dbo = get_txt_data('td_db_objects.txt')
csv_data_tvr = get_txt_data('TABLE_VIEW_REL.txt')
valores = get_folder_objets_list (csv_data_dbo,csv_data_tvr )

print (valores)

carpeta = get_folder_name (valores)
set_directory_creator(carpeta)

header_data = get_txt_header(csv_data_dbo)
object_creator(header_data, valores)