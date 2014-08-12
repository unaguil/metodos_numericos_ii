# -*- coding: utf8 -*-
import matplotlib.pyplot as plt 
import numpy as np

from math import sqrt

from sol_analitica import get_values

T = 10
g = 9.8
w = 500
L = 1

c = sqrt(T * g / w)

num_div = 10
n_nodos = num_div + 1
dx = L / float(num_div)
dt = dx / c 

pasos = 40

tabla = []

#condiciones iniciales para la y
init_nodos = []
for i in range(n_nodos):
	x = dx * i
	if x < 0.6:
		init_nodos.append(x / 3.0)
	else:
		init_nodos.append(1 / 2.0 * (1 - x))

tabla.append(init_nodos)

# primer paso
nodos = []
for i in range(n_nodos):
	if i == 0 or i == (n_nodos - 1):
		nodos.append(init_nodos[i])
	else:
		x = dx * i
		nuevo_valor = (init_nodos[i + 1] + init_nodos[i - 1]) / 2.0 + dt * x * (x - 1)  
		nodos.append(nuevo_valor)

tabla.append(nodos)

# pasos siguientes
for p in range(1, pasos):
	nodos = []
	for i in range(n_nodos):
		if i == 0 or i == (n_nodos - 1):
			nodos.append(tabla[p][i])
		else:
			nuevo_valor = tabla[p][i + 1] + tabla[p][i - 1] - tabla[p - 1][i]
			nodos.append(nuevo_valor)
	tabla.append(nodos)

print "dt = %.4f" % dt
for i in range(len(tabla)):
	print i,
	for n in range(len(tabla[i])):
		print " %.2f" % tabla[i][n],
	print ""

fig, ax = plt.subplots()

for s in range(len(tabla)):
	if s == 0:
		x_values = [dx * i for i in range(n_nodos)]
		y_values = tabla[s]
		points, = ax.plot(x_values, y_values, marker='o', linestyle='-')
		ax.set_xlim(0, 1) 
		ax.set_ylim(-0.5, 0.5) 
	else:
		new_x_values = [dx * i for i in range(n_nodos)]
		new_y_values = tabla[s]
		points.set_data(new_x_values, new_y_values)

	plt.pause(0.005)

# print "Pasos",
# for i in range(5):
# 	print "\t %.2f" % (dx * i),

# print ""
# print ""
# for i in range(len(tabla)):
# 	print i,
# 	t = dt * i
# 	_, sol_analitica = get_values(t, num_div)
# 	for n in range(5):
# 		print "\t %.4f (%.4f)" % (tabla[i][n], abs(tabla[i][n] - sol_analitica[n])),
# 	print ""