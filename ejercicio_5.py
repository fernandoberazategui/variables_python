# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese dos palabras y arme combinaciones con ella
print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())

# De la primera palabra tome las primeras tres letras, utilice el operador :
# De la segunda palabra tome las primeras dos letras, utilice el operador :
# Formar una nueva palabra con los recortes solicitados
# Imprima en pantalla los resultados
palabra_1[0:2]

palabra_2[0:1]

nueva_palabra = palabra_1[0:3] + palabra_2[0:2]

print("La nueva palabra formada con las 3 primeras letras de la primer palabra, seguidas de las dos primeras letras de la segunda palabra, es:", nueva_palabra.title())
