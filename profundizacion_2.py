# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica numérica y cadenas
'''
Enunciado:
Realice un programa que consulte por consola:
- El nombre completo de la persona
- El DNI de la persona
- La edad de la persona
- La altura de la persona

Finalmente el programa debe imprimir dos líneas de texto por separado
- En una línea imprimir el nombre completo y el DNI, aclarando de que
  campo se trata cada uno
        Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
- En la segunda línea se debe imprimir el nombre completo, edad y
  altura de la persona
  Nuevamente debe aclarar el campo de cada uno, para el que lo lea
  entienda de que se está hablando.
'''

from tkinter import N


print('Sistema de ingreso de datos')
# Empezar aquí la resolución del ejercicio
print("ingrese su nombre completo y apellido, luego presione Enter")
Nombre_completo = str(input())

print("Ingrese su DNI y presione Enter")
dni = int(input())

print("Ingrese su edad y presione Enter")
edad = int(input())

print("Ingrese su altura en metros y presione Enter")
altura = float(input())
print()
print("Nomre Completo:",Nombre_completo,"DNI:",dni)
print()
print("Nombre completo:",Nombre_completo)
print("DNI:",dni)
print("Edad:",edad)
print("Altura:",altura,"metros")
print()








