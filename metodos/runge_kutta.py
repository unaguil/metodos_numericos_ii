# -*- coding: utf8 -*- 

import math

def runge_kutta(h, n, f, x_0, y_0, verbose=False):
	x = x_0
	y = y_0

	for i in range(n):
		k1 = h * f(x, y)
		k2 = h * f(x + h / 2, y + k1 / 2)
		k3 = h * f(x + h / 2, y + k2 / 2)
		k4 = h * f(x + h, y + k3)

		if verbose: print "%.1f \t %.5f \t %.4f \t %.4f \t %.4f \t %.4f" % (x, y, k1, k2, k3, k4)

		y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
		x += h

	return x, y

def runge_kutta_sistema(h, n, f, g, x_0, y_0, t_0):
	''' Implementación del método de Runge-Kutta para sistemas de dos
		ecuaciones diferenciales.
		Devuelve una lista de tuplas (t, x, y) con los resultados de
		la integración paso a paso.
		h : paso de integración
		n : número de pasos de la integración
		f : función f(x, y, t)
		g : función g(x, y, t)
		x_0, y_0, t_0 : condiciones iniciales
 	'''
	t = t_0 # condiciones iniciales del sistema
	x = x_0
	y = y_0

	tabla = [(t, x, y)]

	#bucle para obtener una muestra de n valores
	for i in range(n):
		k1 = h * f(x, y, t) #cálculo de los coeficientes
		l1 = h * g(x, y, t)

		k2 = h * f(x + k1 / 2, y + l1 / 2, t + h / 2)
		l2 = h * g(x + k1 / 2, y + l1 / 2, t + h / 2)

		k3 = h * f(x + k2 / 2, y + l2 / 2, t + h / 2)
		l3 = h * g(x + k2 / 2, y + l2 / 2, t + h / 2)

		k4 = h * f(x + k3, y + l3, t + h)
		l4 = h * g(x + k3, y + l3, t + h)

		#incremento de las variables dependientes (x, y)
		# y de la independiente (t)
		x = x + (k1 + 2 * k2 + 2 * k3 + k4) / 6
		y = y + (l1 + 2 * l2 + 2 * l3 + l4) / 6
		t += h

		#comprobación de comportamiento anómalo
		if math.isnan(x) or math.isnan(y):
			print 'Comportamiento anómalo detectado: t = ', t
			break

		#los resultados son almacenados en una lista de elementos (t, x, y)
		tabla.append((t, x, y))

	return tabla

def runge_kutta_fehlberg(h, n, f, x_0, y_0, verbose=False):
	x = x_0
	y = y_0

	for i in range(n):
		k1 = h * f(x, y)
		k2 = h * f(x + h / 4, y + k1 / 4)
		k3 = h * f(x + 3 * h / 8, y + 3 * k1 / 32 + 9 * k2 / 32)
		k4 = h * f(x + 12 * h / 13, y + 1932 * k1 / 2197 - 7200 * k2 / 2197 + 7296 * k3 / 2197)
		k5 = h * f(x + h, y + 439 * k1 / 216 - 8 * k2 + 3680 * k3 / 513 - 845 * k4 / 4104)
		k6 = h * f(x + h / 2, y - 8 * k1 / 27 + 2 * k2 - 3544 * k3 / 2565 + 1859 * k4 / 4104 - 11 * k5 / 40)

		if verbose: print "%.1f \t %.7f \t %.7f \t %.7f \t %.7f \t %.7f \t %.7f \t %.7f" % (x, y, k1, k2, k3, k4, k5, k6)

		y = y + 16 * k1 / 135 + 6656 * k3 / 12825 + 28561 * k4 / 56430 - 9 * k5 / 50 + 2 * k6 / 55
		error = k1 / 360 - 128 * k3 / 4275 - 2197 * k4 / 75240 + k5 / 50 + 2 * k6 / 55

		x += h

	return (x, y, error)