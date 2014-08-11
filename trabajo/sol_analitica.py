# -*- coding: utf8 -*-
from math import sin, cos, pi

def part1(n, x):
	return -x * cos(n * pi * x) + sin(n * pi * x) / (n * pi)

def part2(n, x):
	return -cos(n * pi * x) / (n * pi) - 1 / (n * pi) * part1(n, x)

def calcular_an(n, x):
	return 2 / (3 * n * pi) * part1(n, 0.6) - part1(n, 0) + part2(n, 1) - part2(n, 0.6)

def calcular_ux0(x, num):
	ux = 0

	for n in range(1, num):
		ux += calcular_an(n, x) * sin(n * pi * x)

	return ux

for i in range(11):
	x = i * 0.1
	print "%.2f \t %.2f" % (x, calcular_ux0(x, 100))