print("Digame cuantas palabras tiene la lista")

cantidad= input()
contador=0
lista=[None] * ((int(cantidad)-1)-int(cantidad))
while int(cantidad)>contador:
	 print("Ingrese la palabra")
	 palabra1= input() 
	 if palabra1 not in lista:
	 	 lista.append(palabra1)
	 contador=contador+1
	 
     
     
     

print("La lista creada es" , lista)