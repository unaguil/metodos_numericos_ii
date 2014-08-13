# -*- coding: utf8 -*-
import matplotlib.pyplot as plt 
import numpy as np

from math import sqrt

from sol_analitica import get_values

T = 10000
g = 9.8
r = 500
L = 1

c = sqrt(T * g / r)

num_div = 10
n_nodos = num_div + 1
dx = L / float(num_div)
dt = dx / c 

pasos = 25

tabla_y = []

#condiciones iniciales para la y
init_nodos = []
for i in range(n_nodos):
	x = dx * i
	if x < 0.6:
		init_nodos.append(x / 3.0)
	else:
		init_nodos.append(1 / 2.0 * (1 - x))

tabla_y.append(init_nodos)

#pasos temporales
for p in range(pasos):
	nodos = []
	if p == 0:
		# primer paso
		for i in range(n_nodos):
			if i == 0 or i == (n_nodos - 1):
				nodos.append(init_nodos[i])
			else:
				x = dx * i
				nuevo_valor = (init_nodos[i + 1] + init_nodos[i - 1]) / 2.0 + dt * x * (x - 1)  
				nodos.append(nuevo_valor)
	else:
		#pasos siguientes
		for i in range(n_nodos):
			if i == 0 or i == (n_nodos - 1):
				nodos.append(tabla_y[p][i])
			else:
				nuevo_valor = tabla_y[p][i + 1] + tabla_y[p][i - 1] - tabla_y[p - 1][i]
				nodos.append(nuevo_valor)

	tabla_y.append(nodos)

print "dx = %.4f" % dx
print "dt = %.4f" % dt
print "f = %.2f" % (1 / (20 * 0.0071))

# print "\\begin{tabular}{%s }" % (" c" * (len(tabla_y[0]) + 1))
# print "\hline"
# print "Paso",
# for i in range(len(tabla_y[0])):
# 	print "& %.2f" % (dx * i),
# print "\\\\"	
# print "\hline"
# print "\hline"
# for i in range(len(tabla_y)):
# 	print i,
# 	for n in range(len(tabla_y[i])):
# 		print "& %.2f" % tabla_y[i][n],
# 	print "\\\\"
# print "\hline"
# print "\\end{tabular}"

# fig, ax = plt.subplots()

# for s in range(len(tabla_y)):
# 	if s == 0:
# 		x_values = [dx * i for i in range(n_nodos)]
# 		y_values = tabla_y[s]
# 		points, = ax.plot(x_values, y_values, marker='o', linestyle='-')
# 		ax.set_xlim(0, 1) 
# 		ax.set_ylim(-2.0, 2.0) 
# 	else:
# 		new_x_values = [dx * i for i in range(n_nodos)]
# 		new_y_values = tabla_y[s]
# 		points.set_data(new_x_values, new_y_values)

# 	plt.pause(0.005)

columns = 5
print "\\begin{tabular}{%s }" % (" c" * columns)
print "\hline"
print "Paso",
for i in range(1, columns):
	print "& %.2f" % (dx * i),
print "\\\\"	
print "\hline"
print "\hline"
for i in range(len(tabla_y)):
	print i,
	t = dt * i
	_, sol_analitica = get_values(t, num_div, c)
	for n in range(1, columns):
		print "& %.4f (%.4f)" % (tabla_y[i][n], abs(tabla_y[i][n] - sol_analitica[n])),
	print "\\\\"
print "\\end{tabular}"