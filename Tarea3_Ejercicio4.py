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
print("Palabra a eliminar :")
eleminar = input()

if eleminar in lista:
	contador=0
	for i in lista:
		if lista[contador]== eleminar:
			del lista[contador]	
			contador=contador+1
			continue

	print("La lista es ahora ", lista)
else:
	print("El elemnto no se encuentra en la lista")	