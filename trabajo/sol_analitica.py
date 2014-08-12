# -*- coding: utf8 -*-
import matplotlib.pyplot as plt 
import numpy as np

from math import sin, cos, pi

def an_part1(n, x):
	return -x * cos(n * pi * x) + sin(n * pi * x) / (n * pi)

def an_part2(n, x):
	return -cos(n * pi * x) / (n * pi) - 1 / (n * pi) * an_part1(n, x)

def calcular_an(n, x):
	return 2 / (3 * n * pi) * an_part1(n, 0.6) - an_part1(n, 0.0) + an_part2(n, 1.0) - an_part2(n, 0.6)

def bn_part(n, x):
	numerador = (2 - pi*pi * n*n * (x - 1) * x) * cos(n * pi * x) + pi * n * (2 * x -  1) * sin (n * pi * x)
	return numerador / (pi*pi*pi * n*n*n)

def calcular_bn(n, x):
	return 2 * (bn_part(n, 1.0) - bn_part(n, 0.0))

def calcular_y(x, t, c, num_serie):
	y = 0

	for n in range(1, num_serie):
		y += (calcular_an(n, x) * cos(n * pi * c * t) + calcular_bn(n, x) / (n * pi * c) * sin(n * pi * c * t)) * sin(n * pi * x) 

	return y

def get_values(t, num_div):
	x_values = []
	y_values = []

	dx = 1.0 / num_div
	
	x = 0
	for i in range(num_div + 1):
		x_values.append(x)
		y_values.append(calcular_y(x, t, 1.0, 100))
		x += dx

	return (x_values, y_values)

fig, ax = plt.subplots()

num_div_x = 50
dt = 0.025
steps = 100
for s in range(steps):
	t = dt * s
	if s == 0:
		x_values, y_values = get_values(t, num_div_x)
		points, = ax.plot(x_values, y_values, marker='o', linestyle='-')
		ax.set_xlim(0, 1) 
		ax.set_ylim(-0.5, 0.5) 
	else:
		new_x_values, new_y_values = get_values(t, num_div_x)
		points.set_data(new_x_values, new_y_values)

	plt.pause(0.005)