print("Digame cuantas palabras tiene la lista")

cantidad= input()
contador=0
lista=[None] * ((int(cantidad)-1)-int(cantidad))
while int(cantidad)>contador:
	 print("Ingrese la palabra")
	 palabra1= input() 
	 lista.append(palabra1)
	 contador=contador+1
     
     
     

print("La lista creada es" , lista)
print("Digame cuantas palabras tiene la lista a eliminar")

cantidadE= input()
contadorE=0
listaE=[None] * ((int(cantidadE)-1)-int(cantidadE))
while int(cantidadE)>contadorE:
	 print("Ingrese la palabra")
	 palabra1E= input() 
	 listaE.append(palabra1E)
	 contadorE=contadorE+1
     
     
     

print("La lista de palabras que se va a eliminar es " , listaE)
if len(lista)>=len(listaE):
	contador=0
	for i in lista:
		if lista[contador] in listaE[::]:
			dato=listaE[contador]
			indice= lista.index(dato)
			lista.pop(indice)
			contador= contador+1
			continue
			

else:
	print("No se puede eliminar tantos elementos de la lista")
print("La nueva lista es", lista)	