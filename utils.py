
from tasks import datos_globales_dicc


def cambiar_estado():
	confirmacion = input("Desea cambiar el estado de una tarea? \n")

	if confirmacion in ['Si', "si"]:
		for user in datos_globales_dicc:
			print(user)
			break


	

