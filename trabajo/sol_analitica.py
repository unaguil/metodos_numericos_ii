# -*- coding: utf8 -*-
from math import sin, cos, pi, sqrt

def an_part1(n, x):
	return -x * cos(n * pi * x) + \
		sin(n * pi * x) / (n * pi)

def an_part2(n, x):
	return -cos(n * pi * x) / (n * pi) - 1 / (n * pi) * an_part1(n, x)

def calcular_an(n, x):
	return 2 / (3 * n * pi) * an_part1(n, 0.6) - an_part1(n, 0.0) + \
		an_part2(n, 1.0) - an_part2(n, 0.6)

def bn_part(n, x):
	numerador = (2 - pi*pi * n*n * (x - 1) * x) * cos(n * pi * x) + \
		pi * n * (2 * x -  1) * sin (n * pi * x)

	return numerador / (pi*pi*pi * n*n*n)

def calcular_bn(n, x):
	return 2 * (bn_part(n, 1.0) - bn_part(n, 0.0))

# calcula la posicion y(x, t) utilizando un sumatorio de n coeficientes
# x,t: posición e instante para el que se calcula la posición
# num_serie: numero de elementos de la serie que se incluyen en el calculo
def calcular_y(x, t, c, num_serie):
	y = 0

	for n in range(1, num_serie):
		y += (calcular_an(n, x) * cos(n * pi * c * t) + \
			calcular_bn(n, x) / (n * pi * c) * sin(n * pi * c * t)) * sin(n * pi * x) 

	return y

# obtiene la posición de la cuerda
# t: instante en el que se calcula la posición
# num_div: número de divisiones que se realizan en la cuerda
# c: constantes físicas de la cuerda c = sqrt(Tg/r)
def obtener_valores(t, num_div, c):
	x_values = []
	y_values = []

	dx = 1.0 / num_div
	
	num_serie = 100 # se utilizan 100 elementos de la serie para el cálculo

	x = 0
	for i in range(num_div + 1):
		x_values.append(x)
		y_values.append(calcular_y(x, t, c, num_serie))
		x += dx

	return (x_values, y_values)

if __name__ == '__main__':
	import matplotlib.pyplot as plt 
	import numpy as np

	T = 10000
	g = 9.8
	w = 500
	L = 1

	c = sqrt(T * g / w)

	fig, ax = plt.subplots()

	num_div_x = 10
	dt = 0.2259
	pasos = 25
	for s in range(pasos):
		t = dt * s
		if s == 0:
			x_values, y_values = obtener_valores(t, num_div_x, c)
			points, = ax.plot(x_values, y_values, marker='o', linestyle='-')
			ax.set_xlim(0, 1) 
			ax.set_ylim(-0.5, 0.5) 
		else:
			new_x_values, new_y_values = obtener_valores(t, num_div_x, c)
			points.set_data(new_x_values, new_y_values)

		plt.pause(0.005)


	for s in range(pasos):
		t = dt * s
		print "%d \t %0.4f" % (s, t),
		y_values = obtener_valores(t, num_div_x, c)[1]
		for i in range(len(y_values)):
			print "\t %.2f" % y_values[i],
		print ""
