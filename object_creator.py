import teradatasql
import os
from file_manager import set_directory_creator, txt_reader, get_txt_header, remove_directory
from parametrized_tbl import object_writer
import pandas as pd
 

# ARMA LAS DDL A PARTIR DE LA BASE Y EL NOMBRE DE LA TABLA.


def get_db_connection (header_data):
    print("Conectando a la Base de Datos\n")
    con = teradatasql.connect(host=header_data[0], user=header_data[1], password=header_data[2])
    cursor_tbl = con.cursor()  
    cursor_view = con.cursor() 
    # convertir estos cursores en un diccionario y luego 
    # usarlos en su correspondiente caso en el siguiente metodo
    cursor = {"cursor_tbl":cursor_tbl,"cursor_view":cursor_view}
    
    
    return (cursor)

# Verifies if a table is valid or exist in the database.
# Return true if exist, false if not.
def object_checker (df_folder_objets_list,cursor):

    dic_valid_obj = {'TARGET_DB_TYPE':[],'SOURCE_DB':[],'TARGET_DB':[],'PARAM_SOURCE_DB':[],'PARAM_TARGET_DB':[],'tablename':[],'validity':[]}

    df_folder_objets_list = df_folder_objets_list.reset_index()  # make sure indexes pair with number of rows
    for index, row in df_folder_objets_list.iterrows():

        dic_valid_obj['TARGET_DB_TYPE'].append(row['TARGET_DB_TYPE'])
        dic_valid_obj['SOURCE_DB'].append(row['SOURCE_DB'])
        dic_valid_obj['TARGET_DB'].append(row['TARGET_DB'])
        dic_valid_obj['PARAM_SOURCE_DB'].append(row['PARAM_SOURCE_DB'])
        dic_valid_obj['PARAM_TARGET_DB'].append(row['PARAM_TARGET_DB'])
        dic_valid_obj['tablename'].append(row['tablename'])
        
        sql_show = "SHOW TABLE "+ row['SOURCE_DB'] +"."+ row['tablename']
        try:
            cursor["cursor_tbl"].execute(sql_show)
            
        except teradatasql.OperationalError :
            print ("ATENCIÓN!: No existe la tabla "+ row['TARGET_DB'] +"."+ row['tablename'])

            dic_valid_obj['validity'].append(False)
            continue 
            

        dic_valid_obj['validity'].append(True)   
        
        df_valid_obj = pd.DataFrame(dic_valid_obj)
            
    
    return (df_valid_obj )     #Objetos validos para consultar en la base.                

def object_creator(df_valid_obj,cursor):


    df_valid_obj = df_valid_obj.reset_index()  # make sure indexes pair with number of rows

    for index, row in df_valid_obj.iterrows():
    # Creación de las tablas en TMP

        if row['TARGET_DB_TYPE'] == 'TABLE' and row['validity'] == True: #código duplicado en object_writer Mejorar

            dwtbl_out_file = open("C:/TMP/TABLES/"+ row['TARGET_DB']+"/"+ row['tablename']+'.txt', "w", encoding="utf8")
            
            sql_show = "SHOW TABLE "+ row['TARGET_DB'] +"."+ row['tablename']
            try:
                cursor["cursor_tbl"].execute(sql_show)
                
            except teradatasql.OperationalError :
                print ("ERROR: No existe la tabla "+ row['TARGET_DB'] +"."+ row['tablename'])
                continue
            
            #dwtbl_out_file = open("C:/TMP/"+ row['TARGET_DB']+"/"+ row['tablename']+'.txt', "w", encoding="utf8")
            for reg_tbl in cursor["cursor_tbl"]:
                print ("Generando la tabla:     "+ row['TARGET_DB'] +"."+ row['tablename'] )
                dwtbl_out_file.write(reg_tbl[0].upper())
            dwtbl_out_file.close()
    # Creación de las vistas en la carpeta Teradata        
        elif row['TARGET_DB_TYPE'] == 'VIEW' and row['validity'] == True:
            print ("Generando vista:        "+ row['TARGET_DB'] + "." + row['tablename'] + '\n')
            dw_out_file = open("C:/TERADATA/VIEWS/" + row['TARGET_DB'].upper() + "/"+ row['tablename'] +'.sql', "w", encoding="utf8")
            
                        #exec VIEW_CREATOR (  'D_DW_TABLES', 'DATOS_PERSONALES','${DW_AMBIENTE}_DW_TABLES','${DW_AMBIENTE}_DW_VIEWS')
            sql_macro = "exec VIEW_CREATOR (  '"+ row['SOURCE_DB'] +"', '"+ row['tablename'] + "', '"+ row['PARAM_SOURCE_DB']+"','" + row['PARAM_TARGET_DB']+"')"

            cursor["cursor_view"].execute(sql_macro)

            for reg_view in cursor["cursor_view"]:
                
                dw_out_file.write(reg_view[0].upper()+'\n')
            dw_out_file.close()
    
            

    return 0

