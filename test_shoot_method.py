# -*- coding: utf8 -*-

from metodos.runge_kutta import runge_kutta_fehlberg_sistema

def f(x, u, y):
	return (1 - x / 5.0) * u + x

def g(x, u, y):
	return y

h = 0.2
steps = int((3.0 - 1.0) / h)

tabla = runge_kutta_fehlberg_sistema(h, steps, f, g, 1.0, 2.0, -1.5)

for x, u, y in tabla:
	print "%.2f\t%.6f\t%.6f" % (x, u, y)