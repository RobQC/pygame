#! /usr/bin/env python
# -*- endcoding: utf-8 -*-
# demo.py - nuestro primer programtica en python XD

import random

numero = random.randint(1,100)

tentativas = 0
opcion = 0

while opcion != numero:
	opcion = input("escriba un numero del 1 al 100: ")
	tentativas += 1
	if opcion > numero:
		print "Mayor"
	elif opcion < numero:
		print "Menor"

print "Acerto! El numero sorteado era: ", numero
print "Usted uso ",tentativas," tentativas"
