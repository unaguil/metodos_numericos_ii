# -*- coding: utf-8 -*-

l = 80  # longitud de la cuerda
dx = 10 # incremento espacial

intervalos = l / dx # número de intervalos
num_nodos = intervalos + 1 # número de nodos

pasos = 20 # pasos de tiempo

# crear tabla resultados
tabla = []

# nodos estado inicial 
init_nodos = [0.00, 0.30, 0.60, 0.50, 0.40, 0.30, 0.20, 0.10, 0.00]
tabla.append(init_nodos)

# primer paso
nodos = []
for i in range(num_nodos):
	if i == 0 or i == (num_nodos - 1):
		nodos.append(init_nodos[i])
	else:
		nuevo_valor = (init_nodos[i + 1] + init_nodos[i - 1]) / 2.0 
		nodos.append(nuevo_valor)

tabla.append(nodos)

# pasos siguientes
for p in range(1, pasos):
	nodos = []
	for i in range(num_nodos):
		if i == 0 or i == (num_nodos - 1):
			nodos.append(tabla[p][i])
		else:
			nuevo_valor = tabla[p][i + 1] + tabla[p][i - 1] - tabla[p - 1][i]
			nodos.append(nuevo_valor)
	tabla.append(nodos)

print "Pasos"
for i in range(len(tabla)):
	print i, 
	for n in range(len(tabla[i])):
		print "\t %.2f" % tabla[i][n],
	print ""