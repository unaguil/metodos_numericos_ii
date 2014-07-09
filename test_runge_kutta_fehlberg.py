# -*- coding: utf8 -*-

from metodos.runge_kutta import runge_kutta_fehlberg_sistema
from metodos.runge_kutta import runge_kutta_sistema

def f(t, x, y):
	return x * y + t

def g(t, x, y):
	return t * y + x

print "Runge-Kutta-Fehlberg"
tabla = runge_kutta_fehlberg_sistema(0.1, 5, f, g, 0, 1, -1)

for t, x, y in tabla:
	print "%.6f\t%.6f\t%.6f" % (t, x, y)

print ""
print "Runge-Kutta"
tabla = runge_kutta_sistema(0.1, 5, f, g, 0, 1, -1)

for t, x, y in tabla:
	print "%.6f\t%.6f\t%.6f" % (t, x, y)