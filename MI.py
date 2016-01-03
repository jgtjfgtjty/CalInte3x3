#-*- coding: utf-8 -*-
__autor__ = "Diego Morell"

#Calculo de matrices e integrales

print "Matrices: m, Integrales: i"
pr = raw_input(":")

if pr == "m":
	#operación de matrices
	#multiplicación de matrices 3 x 3
	print ("a",	"b", "c",)
	print ("d",	"e", "f",)	
	print ("g",	"h", "i",)

	print "Dame para cada letra el numero que le corresponde"
	a = input("a = :")
	b = input("b = :")
	c = input("c = :")
	d = input("d = :")
	e = input("e = :")
	f = input("f = :")
	g = input("g = :")
	h = input("h = :")
	i = input("i = :")

	print "¿Asi?"

	print (a, b, c,)
	print (d, e, f,)	
	print (g, h, i,) 

	respuesta print ":"

	if respuesta == "si":
		print "¿Cual está mal?"
		  

elif pr == "i":
	#operación de integrales
	#formula general: u**n = u**n + 1/n + 1 + c 
	print "Dame un número"
	u = input(":")
	print "¿A que está elevado?"
	n = input(":")

	def calculo_integral(u,n): #función del calculo que recibe como parametros un número cualquiera y su exponente
		numerador = u**(n + 1) #se calcula el numerador y el denominador por partes para que sea mas fácil
		denominador = n + 1

		resultado = numerador / denominador 
		print resultado 

	calculo_integral(u,n)