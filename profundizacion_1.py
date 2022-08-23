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

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio
print("Ingrese primer numero real")
primer_real = float(input())

print("ingrese su segundo numero real")
segundo_real = float(input())

suma = primer_real + segundo_real
resta = primer_real - segundo_real
multiplicacion = primer_real * segundo_real
division = primer_real / segundo_real
potencia = primer_real ** segundo_real


print("La suma entre", primer_real, "y", segundo_real, "es:", suma)

print("la resta entre", primer_real, "y", segundo_real, "es:", resta)

print("la multiplicacion entre", primer_real, "y", segundo_real, "es:", multiplicacion)

print("la division entre", primer_real, "y", segundo_real, "es:", division)

print("El resultado de elevar", primer_real, "a la", segundo_real, "potencia, es:", potencia)

