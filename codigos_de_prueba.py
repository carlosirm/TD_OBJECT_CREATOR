import teradatasql
import os
from t002_file_manager import directory_creator, txt_reader, get_txt_header,get_txt_data, remove_directory,  get_folder_name, get_folder_objets_list
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

valores = get_folder_objets_list (csv_data_dbo,csv_data_tvr )
print (valores)
print (len(valores))

#print (get_folder_name (valores))

"""for v in valores:
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