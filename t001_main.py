import teradatasql
import os
from t002_file_manager import directory_creator, td_txt_reader, get_login_data, remove_directory
from t002_parametrized_tbl import object_writer
from t002_object_creator import object_creator
 



lectura = td_txt_reader()
login_data = get_login_data(lectura)
base_tabla = directory_creator(lectura)

print ('object_creator(login_data) ')
object_creator(login_data)

print ('object_writer(base_tabla)')
object_writer(base_tabla)

#remove_directory() 
