import teradatasql
import os
import pandas as pd
from file_manager import set_directory_creator, txt_reader, get_txt_header,get_txt_data, remove_directory,  get_folder_name, get_folder_objets_list,dbo_to_dataframe,csv_to_dataframe
from parametrized_tbl import object_writer
from object_creator import object_creator
 




##print (tips.head(2))


"""
Convierte el archivo td_db_objects.txt en un dataframe
input: 
"""

csv_data_dbo = get_txt_data('td_db_objects.txt')

df_dbo = dbo_to_dataframe (csv_data_dbo)
df_tvr = csv_to_dataframe ('TABLE_VIEW_REL.txt')

obj_list = get_folder_objets_list(df_dbo,df_tvr)

print (obj_list)


"""
alien_0 = {'color': 'green'}                            # assign again green to key color.
print("The alien is " + alien_0['color'] + ".")         # print the value 'green' for the key 'color'
alien_0['color'] = 'yellow'                             # reassign the value for 'color'
print("The alien is now " + alien_0['color'] + ".")     # check the change for the key color.
"""
#
#print (df)


"""
csv_data_dbo = get_txt_data('td_db_objects.txt')
csv_data_tvr = get_txt_data('TABLE_VIEW_REL.txt')


print (csv_data_dbo)
for c in csv_data_dbo:
	print (c)


valores = get_folder_objets_list (csv_data_dbo,csv_data_tvr )
print (valores)
print (len(valores))

carpeta = get_folder_name (valores)


set_directory_creator(carpeta)

for v in valores:
	print (v)


letras = ['a','b','c','d','e']
numeros = ['a','2','c','4','5']
nuevo = []
nuevo.append(letras[0])
nuevo.append(letras[2])
print (nuevo)


letras_mayusculas = [value.upper() for value in letras]
print (letras_mayusculas)

for l in letras:
	for n in numeros:
		if l == n:
			print (l+n)

l_data_dbo = 'Hola'
l_data_tvr = 'HOLA'

if l_data_dbo.upper() == l_data_tvr.upper():
	print ('Las cadenas son iguales')
else:
	print ('hay diferencias en las cadenas')
#if l_data_dbo[0].upper() == l_data_tvr[0].upper():


csv_data_dbo = [['A','B','C'],['d','e','f'],['g','h','i']]
csv_data_tvr = [['A','2','3'],['d','4','5'],['g','6','7']]


if 'A' in ['A','B','C']:
	print ('si existe la A')
else:
	print ('no existe')
	"""