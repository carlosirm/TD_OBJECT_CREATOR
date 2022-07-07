def get_folder_objets_list (data_dbo,data_tvr):

	csv_data_tvr = list(data_tvr) # convertir a lista el objecto csv para que sea iterable
	csv_data_dbo = list(data_dbo) # convertir a lista el objecto csv para que sea iterable
	folder_objets_list = []
	csv_data_tvr_len = len(csv_data_tvr)

	it_num = 0
	
	for l_data_dbo in csv_data_dbo:
		l_data_dbo = [value.upper() for value in l_data_dbo]
		it_num = it_num+1
		#print ('iteracion num : ' + str(it_num) )
		#print (l_data_dbo)
		tvr_num = 0
		
		for l_data_tvr in csv_data_tvr:
			l_data_tvr = [value.upper() for value in l_data_tvr]
			tvr_num = tvr_num + 1
			#print ('	\niteracion_cd: ' + str(it_num) + str(tvr_num))
			#print ('	objeto dbo: ' + l_data_dbo[0].upper() + ' objeto tvr: ' + l_data_tvr[0].upper())
			
			temp_tvr = []
	
			# Condicional que agrega los objetos de vistas.
			if l_data_dbo[0] == l_data_tvr[0]:
				#print ('		' + l_data_dbo[0].upper() + ' +  ' + l_data_tvr[0].upper())
				temp_tvr.append(l_data_tvr[0])	# and add databasename to  the list.
				temp_tvr.append(l_data_tvr[2])	# and add paramdatabasename to  the list.
				temp_tvr.append(l_data_dbo[1])	# and add tablename to  the list.
				#print ('		TABLA agregada a la lista')
				#print ('		' + str(temp_tvr))
				folder_objets_list.append(temp_tvr)

				temp_tvr = []

				temp_tvr.append(l_data_tvr[1])	# and add databasename to  the list.
				temp_tvr.append(l_data_tvr[3])	# and add paramdatabasename to  the list.
				temp_tvr.append(l_data_dbo[1])	# and add tablename to  the list.
				#'D_DMT_TABLES', '${DW_AMBIENTE}_DW_TABLES', 'TABLA_DE_PRUEBAS'#
				#print ('		VISTA agregada a la lista')
				#print ('		' + str(temp_tvr))
				folder_objets_list.append(temp_tvr)

				#print ('		Resultado Parcial lado C1')
				#print (folder_objets_list)
				break

			# Si no es vista, se agrega como tabla. Ejemplo una base Staging.
			elif csv_data_tvr_len ==  tvr_num and l_data_dbo[0] != l_data_tvr[0]:
				#print (csv_data_tvr_len) 
				#print (tvr_num)
				#print ('		TABLA STAGING agregada a la lista')
				#print ('		' + str(temp_tvr))
				temp_tvr.append(l_data_dbo[0])	# and add databasename to  the list.
				temp_tvr.append(l_data_tvr[2])	# and add paramdatabasename to  the list.
				temp_tvr.append(l_data_dbo[1])	# and add tablename to  the list.
				folder_objets_list.append(temp_tvr)
				#print ('		Resultado Parcial lado C2')
				#print (folder_objets_list)
	return (folder_objets_list)
