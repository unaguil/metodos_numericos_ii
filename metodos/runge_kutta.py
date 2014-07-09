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

def runge_kutta_sistema(h, n, f, g, t_0, x_0, y_0):
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
		k1 = h * f(t, x, y) #cálculo de los coeficientes
		l1 = h * g(t, x, y)

		k2 = h * f(t + h / 2, x + k1 / 2, y + l1 / 2)
		l2 = h * g(t + h / 2, x + k1 / 2, y + l1 / 2)

		k3 = h * f(t + h / 2, x + k2 / 2, y + l2 / 2)
		l3 = h * g(t + h / 2, x + k2 / 2, y + l2 / 2)

		k4 = h * f(t + h, x + k3, y + l3)
		l4 = h * g(t + h, x + k3, y + l3)

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


def runge_kutta_fehlberg_sistema(h, n, f, g, t_0, x_0, y_0, verbose=False):
	t = t_0
	x = x_0
	y = y_0

	tabla = [(t, x, y)]

	for i in range(n):
		k1 = h * f(t, x, y)
		l1 = h * g(t, x, y)

		k2 = h * f(t + h / 4, x + k1 / 4, y + l1 / 4)
		l2 = h * g(t + h / 4, x + k1 / 4, y + l1 / 4)

		k3 = h * f(t + 3 * h / 8, x + 3 * k1 / 32 + 9 * k2 / 32, y + 3 * l1 / 32 + 9 * l2 / 32)
		l3 = h * g(t + 3 * h / 8, x + 3 * k1 / 32 + 9 * k2 / 32, y + 3 * l1 / 32 + 9 * l2 / 32)

		k4 = h * f(t + 12 * h / 13, x + 1932 * k1 / 2197 - 7200 * k2 / 2197 + 7296 * k3 / 2197, y + 1932 * l1 / 2197 - 7200 * l2 / 2197 + 7296 * l3 / 2197)
		l4 = h * g(t + 12 * h / 13, x + 1932 * k1 / 2197 - 7200 * k2 / 2197 + 7296 * k3 / 2197, y + 1932 * l1 / 2197 - 7200 * l2 / 2197 + 7296 * l3 / 2197)

		k5 = h * f(t + h, x + 439 * k1 / 216 - 8 * k2 + 3680 * k3 / 513 - 845 * k4 / 4104, y + 439 * l1 / 216 - 8 * l2 + 3680 * l3 / 513 - 845 * l4 / 4104)
		l5 = h * g(t + h, x + 439 * k1 / 216 - 8 * k2 + 3680 * k3 / 513 - 845 * k4 / 4104, y + 439 * l1 / 216 - 8 * l2 + 3680 * l3 / 513 - 845 * l4 / 4104)

		k6 = h * f(t + h / 2, x - 8 * k1 / 27 + 2 * k2 - 3544 * k3 / 2565 + 1859 * k4 / 4104 - 11 * k5 / 40, y - 8 * l1 / 27 + 2 * l2 - 3544 * l3 / 2565 + 1859 * l4 / 4104 - 11 * l5 / 40)
		l6 = h * g(t + h / 2, x - 8 * k1 / 27 + 2 * k2 - 3544 * k3 / 2565 + 1859 * k4 / 4104 - 11 * k5 / 40, y - 8 * l1 / 27 + 2 * l2 - 3544 * l3 / 2565 + 1859 * l4 / 4104 - 11 * l5 / 40)

		if verbose: print "Step %d" % i
		if verbose: print "\t %.6f \t %.6f \t %.6f \t %.6f \t %.6f \t %.6f" % (k1, k2, k3, k4, k5, k6)
		if verbose: print "\t %.6f \t %.6f \t %.6f \t %.6f \t %.6f \t %.6f" % (l1, l2, l3, l4, l5, l6)

		x = x + 16 * k1 / 135 + 6656 * k3 / 12825 + 28561 * k4 / 56430 - 9 * k5 / 50 + 2 * k6 / 55
		y = y + 16 * l1 / 135 + 6656 * l3 / 12825 + 28561 * l4 / 56430 - 9 * l5 / 50 + 2 * l6 / 55

		t += h

		tabla.append((t, x, y))

	return tabla
