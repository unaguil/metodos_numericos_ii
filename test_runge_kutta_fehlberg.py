# -*- coding: utf8 -*-

from metodos.runge_kutta import runge_kutta_fehlberg_sistema

def f(t, x, y):
	return x * y + t

def g(t, x, y):
	return t * y + x

tabla = runge_kutta_fehlberg_sistema(0.1, 5, f, g, 0, 1, -1, True)

for t, x, y in tabla:
	print "%.6f\t%.6f\t%.6f" % (t, x, y)