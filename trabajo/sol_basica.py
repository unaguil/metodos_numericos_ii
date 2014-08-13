# -*- coding: utf8 -*-
import matplotlib.pyplot as plt 
import numpy as np

from math import sqrt

from sol_analitica import obtener_valores

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

#condiciones iniciales
init_nodos_y = []
for i in range(n_nodos):
	x = dx * i
	#posiciónes iniciales
	if x < 0.6:
		init_nodos_y.append(x / 3.0)
	else:
		init_nodos_y.append(1 / 2.0 * (1 - x))

tabla_y.append(init_nodos_y)

tabla_dydt = []

# pasos temporales
for p in range(pasos):
	# posiciones
	nodos_y = []
	if p == 0:
		# primer paso
		for i in range(n_nodos):
			if i == 0 or i == (n_nodos - 1):
				nodos_y.append(tabla_y[p][i]) #posicion
			else:
				x = dx * i
				nueva_y = (tabla_y[p][i + 1] + tabla_y[p][i - 1]) / 2.0 + dt * x * (x - 1)  
				nodos_y.append(nueva_y)
	else:
		# pasos siguientes
		for i in range(n_nodos):
			if i == 0 or i == (n_nodos - 1):
				nodos_y.append(tabla_y[p][i])
			else:
				nueva_y = tabla_y[p][i + 1] + tabla_y[p][i - 1] - tabla_y[p - 1][i]
				nodos_y.append(nueva_y)

	tabla_y.append(nodos_y)

	nodos_dydt = []
	for i in range(n_nodos):
		nueva_dydt = (tabla_y[-1][i] - tabla_y[-2][i]) / dt
		nodos_dydt.append(nueva_dydt)

	tabla_dydt.append(nodos_dydt)

print "dx = %.4f" % dx
print "dt = %.4f" % dt
# print "f = %.2f" % (1 / (20 * 0.0071))

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
# print "\\end{tabular}"

columns = [3, 4, 5, 6]
print "\\begin{tabular}{%s }" % (" c" * (len(columns) + 1))
print "\hline"
print "Paso",
for i in columns:
	print "& %.2f" % (dx * i),
print "\\\\"	
print "\hline"
print "\hline"
for i in range(len(tabla_y) - 1):
	print i,
	for n in columns:
		print "& %.2f (%.2f)" % (tabla_y[i][n], tabla_dydt[i][n]),
	print "\\\\"
print "\\end{tabular}"

# # fig, ax = plt.subplots()

# # for s in range(len(tabla_y)):
# # 	if s == 0:
# # 		x_values = [dx * i for i in range(n_nodos)]
# # 		y_values = tabla_y[s]
# # 		points, = ax.plot(x_values, y_values, marker='o', linestyle='-')
# # 		ax.set_xlim(0, 1) 
# # 		ax.set_ylim(-2.0, 2.0) 
# # 	else:
# # 		new_x_values = [dx * i for i in range(n_nodos)]
# # 		new_y_values = tabla_y[s]
# # 		points.set_data(new_x_values, new_y_values)

# # 	plt.pause(0.005)

# columns = 5
# print "\\begin{tabular}{%s }" % (" c" * columns)
# print "\hline"
# print "Paso",
# for i in range(1, columns):
# 	print "& %.2f" % (dx * i),
# print "\\\\"	
# print "\hline"
# print "\hline"
# for i in range(len(tabla_y)):
# 	print i,
# 	t = dt * i
# 	_, sol_analitica = obtener_valores(t, num_div, c)
# 	for n in range(1, columns):
# 		print "& %.4f (%.4f)" % (tabla_y[i][n], abs(tabla_y[i][n] - sol_analitica[n])),
# 	print "\\\\"
# print "\\end{tabular}"