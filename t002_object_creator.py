import teradatasql
import os
from t002_file_manager import directory_creator, td_txt_reader, get_header_data, remove_directory
from t002_parametrized_tbl import object_writer
 

# ARMA LAS DDL A PARTIR DE LA BASE Y EL NOMBRE DE LA TABLA.



def object_creator(header_data, info_databases):

    print("Conectando a la Base de Datos")
    con = teradatasql.connect(host=header_data[0], user=header_data[1], password=header_data[2])
    cursor = con.cursor()
    cursor2 = con.cursor()
    cursor3 = con.cursor()
    cursor4 = con.cursor()

    
    #print (lectura[0])
    #base_tabla = [x.upper() for x in base_tabla]

    for registro in info_databases['base_tablas']:
        print (info_databases['base_tablas'])
        registro = [x.upper() for x in registro] #convertir las base_tabla a mayusculas
        dwtbl_out_file = open("C:/TMP/"+registro[0]+"/"+registro[1]+'.txt', "w", encoding="utf8")
        print ("     OK: Consultando la tabla..."+registro[0]+"."+registro[1])
        sql = "SHOW TABLE "+registro[0]+"."+registro[1]
        print (sql)
        try:
            cursor.execute(sql)
        except teradatasql.OperationalError :
            print ("ERROR: No existe la tabla "+registro[0]+"."+registro[1])
        for reg in cursor:
            dwtbl_out_file.write(reg[0])
        dwtbl_out_file.close()
        
        # si la base de D_DW_TABLES ejecuta la macro de las vistas.
        
        tbl_a_vistas = info_databases['vistas_db']  # Aqui esta almacenado un diccionario con todas las bases de datos de vistas.
        
        for tvr in tbl_a_vistas:
            if registro[0] == tvr[0].upper():
                print ("Generando vista "+registro[0]+"."+registro[1])
                dw_out_file = open("C:/TERADATA/" + tvr[1].upper() + "/"+registro[1]+'.sql', "w", encoding="utf8")
                
                sql2 = "exec XA52251.DW_VIEW_CREATOR (  '"+registro[0]+"', UPPER('"+registro[1]+"'))"
               
                cursor2.execute(sql2)
                for reg in cursor2:
                    print("for 1" + reg[0])
                    dw_out_file.write(reg[0]+'\n')
                dw_out_file.close()
            
    return 0

"""
lectura = td_txt_reader()
header_data = get_header_data(lectura)
base_tabla = directory_creator(lectura)

print ('object_creator(header_data) ')
object_creator(header_data)

print ('object_writer(base_tabla)')
object_writer(base_tabla)

#remove_directory() 
"""
