class Calculadora(object):
	"""docstring for Calculadora"""
	def __init__(self, nombre):
		super(Calculadora, self).__init__()
		self.nombre = nombre
	def Suma(self,num1,num2):
			return num1+num2
	def Resta(self,num1,num2):
			return num1-num2
	def Multiplicacion(self,num1,num2):
			return num1*num2
	def Division(self,num1,num2):
			return num1/num2	
			

import os

 

def menu():

	

	os.system('cls')

	print ("Selecciona una opción")

	print ("\t1 - Suma")

	print ("\t2 - Resta")

	print ("\t3 - Multiplicacion")

	print ("\t4 - Division")

	print ("\t5 - Salir")

 

 

while True:
	menu()
	opcionMenu = input("Selecciona una opcion >> ")

 

	if opcionMenu=="1":

		print ("Digite el primer numero a sumar")
		numero1 = input()
		try:
			int(numero1)
		except ValueError:
			print("El numero debe de ser entero")
			continue
		print ("Digite el segundo numero a sumar")
		numero2 = input()
		try:
			int(numero2)
		except ValueError:
			print("El numero debe de ser entero")
			continue
		objCalculadora = Calculadora("miCal")
		res=objCalculadora.Suma(int(numero1),int(numero2))
		print("La suma de los numeros "+str(numero1) +" + " + str(numero2)+ " es " , res)

		input("pulsa una tecla para continuar")

	elif opcionMenu=="2":

		print ("Digite el primer numero a restar")
		numero1 = input()
		try:
			int(numero1)
		except ValueError:
			print("El numero debe de ser entero")
			continue
		print ("Digite el segundo numero a sumar")
		numero2 = input()
		try:
			int(numero2)
		except ValueError:
			print("El numero debe de ser entero")
			continue
		objCalculadora = Calculadora("miCal")
		res=objCalculadora.Resta(int(numero1),int(numero2))
		print("La resta de los numeros "+str(numero1) +" - " + str(numero2)+ " es " , res)

		input("pulsa una tecla para continuar")

	elif opcionMenu=="3":

		print ("Digite el primer numero a multiplicar")
		numero1 = input()
		try:
			int(numero1)
		except ValueError:
			print("El numero debe de ser entero")
			continue
		print ("Digite el segundo numero a sumar")
		numero2 = input()
		try:
			int(numero2)
		except ValueError:
			print("El numero debe de ser entero")
			continue
		objCalculadora = Calculadora("miCal")
		res=objCalculadora.Multiplicacion(int(numero1),int(numero2))
		print("La Multiplicacion de los numeros "+str(numero1) +" * " + str(numero2)+ " es " , res)

		input("pulsa una tecla para continuar")

	elif opcionMenu=="4":

		print ("Digite el primer numero a dividir")
		numero1 = input()
		try:
			int(numero1)
		except ValueError:
			print("El numero debe de ser entero")
			continue
		print ("Digite el segundo numero a sumar")
		numero2 = input()
		try:
			int(numero2)
		except ValueError:
			print("El numero debe de ser entero")
			continue
		objCalculadora = Calculadora("miCal")
		res=objCalculadora.Division(int(numero1),int(numero2))
		print("La Division de los numeros "+str(numero1) +" / " + str(numero2)+ " es " , res)

		input("pulsa una tecla para continuar")
	elif opcionMenu=="5":
	    
	    break	

	else:

		print ("")

		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")