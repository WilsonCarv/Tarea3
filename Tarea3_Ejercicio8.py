print("Digame cuantas palabras tiene la primera  lista")

cantidad= input()
contador=0
lista=[None] * ((int(cantidad)-1)-int(cantidad))
while int(cantidad)>contador:
	 print("Ingrese la palabra")
	 palabra1= input() 
	 lista.append(palabra1)
	 contador=contador+1
	 
     
     
     

print("La primera lista creada es" , lista)
print("Digame cuantas palabras tiene la Segunda  lista")

cantidadS= input()
contadorS=0
listaS=[None] * ((int(cantidadS)-1)-int(cantidadS))
while int(cantidadS)>contadorS:
	 print("Ingrese la palabra")
	 palabra1S= input() 
	 listaS.append(palabra1S)
	 contadorS=contadorS+1
	 
     
     
     

print("La segunda lista creada es" , listaS)
aparecen=[]

for i in lista:
		if i in listaS[::]:
			if  i not in aparecen[::]:
				aparecen.append(i)
			
			
			

print("Palabras que se repiten en las dos listas", aparecen)	
aparecenP=[]

for i in lista:
		if i not in listaS[::]:
			
			aparecenP.append(i)
			

print("Palabras que aparecen solo en la primera", aparecenP)
aparecenS=[]

for i in listaS:
		if i not in lista[::]:
			
			aparecenS.append(i)
			

print("Palabras que aparecen solo en la segunda", aparecenS)				


todos= aparecen + aparecenP + aparecenS		
print("Todos los elementos" , todos)				