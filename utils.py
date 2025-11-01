
from tasks import datos_globales_dicc

from tasks import listar_tareas

# ANTES DE ESCRIBIR CODIGO EN ESTE ARCHIVO PIENSA:
# Y TMB DECILO EN VOS ALTA JARED

# QUE TIPO DE DATO ESTOY ITERANDO? 
# ESTOY ACCEDIENDO POR INDICE O POR CLAVE?

# RECORDA EL DOLOR DE HUEVOS QUE FUE HACER ESTAS DOS FUNCIONES DE ABAJO LOL


def cambiar_estado():
	confirmacion = input("Desea cambiar el estado de una tarea? \n")


	listar_tareas()
	req_id = int(input("Ingrese el numero de tarea que quiere cambiar \n"))
	encontrado = False

	#lo mejor seria recorrer por el elemento directamente
	for tarea in datos_globales_dicc:
		if tarea['ID'] == req_id:
			encontrado = True
			if tarea['estado'] == 'si':
				tarea['estado'] = 'no'
			else:
				tarea['estado'] = 'si'
			print('Estado cambiado con exito.')
			break
	if not encontrado:
		print("No se encontro la tarea.")


def eliminar_tareas():
	listar_tareas()
	req_id2 = int(input('Ingrese el numero de tarea que quiere eliminar'))
	encontrado2 = False

	for tarea2 in datos_globales_dicc:
		if tarea2['ID'] == req_id2:
			encontrado2 = True
			datos_globales_dicc.remove(tarea2) #mejor porque ya se el ID
			print("Tarea eliminada con exito.")
			break

	if not encontrado2:
		print("No hay ningun numero con esa tarea.")




