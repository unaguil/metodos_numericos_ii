# -*- coding: utf8 -*-
from math import sqrt

T = 10000 # características de la cuerda
g = 9.8
r = 500
L = 1
c = sqrt(T * g / r)

num_div = 10 # número de divisiones de la cuerda
n_nodos = num_div + 1 # número de nodos totales
dx = L / float(num_div) # intervalo entre nodos
dt = dx / c # duración de un paso de tiempo
pasos = 25 # número de pasos que se van a calcular

tabla_y = [] # inicialización de la tabla de resultados
# cálculo de las condiciones iniciales
init_nodos_y = []
for i in range(n_nodos):
	x = dx * i
	if x < 0.6: # función dividida en dos partes 
		init_nodos_y.append(x / 3.0)
	else:
		init_nodos_y.append(1 / 2.0 * (1 - x))

tabla_y.append(init_nodos_y) # se añaden los resultados a una tabla

tabla_dydt = [] # inicialización de la tabla de derivadas
for p in range(pasos): # pasos temporales
	nodos_y = [] #inicializar posiciones
	if p == 0:
		for i in range(n_nodos): # primer paso
			if i == 0 or i == (n_nodos - 1):
				nodos_y.append(tabla_y[p][i]) # posiciones de los extremos
			else:
				# cálculo de la nueva posición nodo
				x = dx * i
				nueva_y = (tabla_y[p][i + 1] + tabla_y[p][i - 1]) / 2.0 + dt * x * (x - 1)  
				nodos_y.append(nueva_y) #la posición se añade a la lista de nodos
	else:
		for i in range(n_nodos): # pasos siguientes (n > 1)
			if i == 0 or i == (n_nodos - 1):
				nodos_y.append(tabla_y[p][i]) # posiciones de los extremos
			else:
				# cálculo de la nueva posición del nodo
				nueva_y = tabla_y[p][i + 1] + tabla_y[p][i - 1] - tabla_y[p - 1][i]
				nodos_y.append(nueva_y)

	tabla_y.append(nodos_y) # las nuevas posiciones se añaden a la tabla

	nodos_dydt = [] # calculo de la velocidad de la cuerda
	for i in range(n_nodos):
		nueva_dydt = (tabla_y[-1][i] - tabla_y[-2][i]) / dt
		nodos_dydt.append(nueva_dydt)

	tabla_dydt.append(nodos_dydt) # las nuevas velocidades se añaden a la tabla

def imprimir_tabla_frecuencia():
	print "\\begin{tabular}{%s }" % (" c" * (len(tabla_y[0]) + 1))
	print "\hline"
	print "Paso",
	for i in range(len(tabla_y[0])):
		print "& %.2f" % (dx * i),
	print "\\\\"	
	print "\hline"
	print "\hline"
	for i in range(len(tabla_y)):
		print i,
		for n in range(len(tabla_y[i])):
			print "& %.2f" % tabla_y[i][n],
		print "\\\\"
	print "\\end{tabular}"

def imprimir_valores():
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

def generar_grafica():
	fig, ax = plt.subplots()

	for s in range(len(tabla_y)):
		ax.set_xlabel('dx=0.1 cm dt=%.4f s (n=%d, t=%.3f s)' % (dt, s, (s * dt)))
		if s == 0:
			x_values = [dx * i for i in range(n_nodos)]
			y_values = tabla_y[s]
			points, = ax.plot(x_values, y_values, marker='o', linestyle='-')
			ax.set_xticks(np.arange(0, 1.1, 0.1))
			ax.set_yticks(np.arange(-0.4, 0.41, 0.1)) 
		else:
			new_x_values = [dx * i for i in range(n_nodos)]
			new_y_values = tabla_y[s]
			points.set_data(new_x_values, new_y_values)

		if s in [0, 5, 10, 17]:
			plt.savefig("string-%s.png" % s)

		plt.pause(0.005)

def imprimir_precision():
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
		_, sol_analitica = obtener_valores(t, num_div, c)
		for n in range(1, columns):
			print "& %.4f (%.4f)" % (tabla_y[i][n], abs(tabla_y[i][n] - sol_analitica[n])),
		print "\\\\"
	print "\\end{tabular}"

if __name__ == '__main__':
	import matplotlib.pyplot as plt 
	import numpy as np
	from sol_analitica import obtener_valores

	print "dx = %.4f" % dx
	print "dt = %.4f" % dt
	print "f = %.2f" % (1 / (20 * 0.0071))

	imprimir_tabla_frecuencia()

	imprimir_valores

	imprimir_precision()

	generar_grafica()