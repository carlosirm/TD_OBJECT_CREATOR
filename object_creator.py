import teradatasql
import os
from file_manager import set_directory_creator, txt_reader, get_txt_header, remove_directory
from parametrized_tbl import object_writer
 

# ARMA LAS DDL A PARTIR DE LA BASE Y EL NOMBRE DE LA TABLA.


def get_db_connection (header_data):
    print("Conectando a la Base de Datos")
    con = teradatasql.connect(host=header_data[0], user=header_data[1], password=header_data[2])
    cursor_tbl = con.cursor()  
    cursor_view = con.cursor() 
    # convertir estos cursores en un diccionario y luego 
    # usarlos en su correspondiente caso en el siguiente metodo
    cursor = {"cursor_tbl":cursor_tbl,"cursor_view":cursor_view}
    
    
    return (cursor)

def object_creator(df_folder_objets_list,cursor):

    df_folder_objets_list = df_folder_objets_list.reset_index()  # make sure indexes pair with number of rows

    for index, row in df_folder_objets_list.iterrows():
        print (row)
        if row['TARGET_DB_TYPE'] == 'TABLE':
            dwtbl_out_file = open("C:/TMP/"+ row['TARGET_DB']+"/"+ row['tablename']+'.txt', "w", encoding="utf8")
            print ("     OK: Consultando la tabla..."+ row['TARGET_DB'] +"."+ row['tablename'])
            sql_show = "SHOW TABLE "+ row['TARGET_DB'] +"."+ row['tablename']
            try:
                cursor["cursor_tbl"].execute(sql_show)
                print (cursor["cursor_tbl"].execute(sql_show))
            except teradatasql.OperationalError :
                print ("ERROR: No existe la tabla "+registro[0]+"."+registro[1])
            for reg_tbl in cursor["cursor_tbl"]:
                dwtbl_out_file.write(reg_tbl[0].upper())
            dwtbl_out_file.close()
            
        else:
            print ("Generando vista "+ row['TARGET_DB'] + "." + row['tablename'])
            dw_out_file = open("C:/TERADATA/" + row['TARGET_DB'].upper() + "/"+ row['tablename'] +'.sql', "w", encoding="utf8")
            
            sql_macro = "exec XA52251.DW_VIEW_CREATOR (  '"+ row['TARGET_DB'] +"', UPPER('"+ row['tablename'] +"'))"
           
            cursor["cursor_view"].execute(sql_macro)

            for reg_view in cursor["cursor_view"]:
                print (reg_view[0].upper())
                dw_out_file.write(reg_view[0].upper()+'\n')
            dw_out_file.close()
            

    return 0

"""
txt_read = td_txt_reader()
header_data = get_txt_header(txt_read)
base_tabla = directory_creator(txt_read)

print ('object_creator(header_data) ')
object_creator(header_data)

print ('object_writer(base_tabla)')
object_writer(base_tabla)

#remove_directory() 
"""
