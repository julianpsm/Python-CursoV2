# Ciclos - for

numeros = [1, 2, 3, 4, 5]

total = 0

total = numeros[0] + numeros[1] + numeros[2] + numeros[3] + numeros[4]
print('Total de la suma de los números de 1 a 5:', total)

print()

total = 0

total += numeros[0]
total += numeros[1]
total += numeros[2]
total += numeros[3]
total += numeros[4]
# total += numeros[999]
print('Total de la suma de los números de 1 a 5:', total)

print()

numeros.append(6)
numeros.append(7)
numeros.append(8)
numeros.append(9)
numeros.append(10)

print('Contenido actual de la lista `numeros`:', numeros)

total += numeros[5]
total += numeros[6]
total += numeros[7]
total += numeros[8]
total += numeros[9]

print('Total de la suma de los números de 1 a 10:', total)

print()

# Uso explícito del ciclo for para resolver un problema que requiere iterar (recorrer) todos los elementos 
# de una colección (lista):

total = 0

for i in range(0, len(numeros)):
    total += numeros[i]

print('Total de la suma de los números de 1 a 10:', total)

print()

# Suma de los números pares que hay en la lista `numeros`:
print('Suma de los números pares que hay en la lista `numeros`')

suma_pares = 0

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        suma_pares += numeros[i]

print('La suma de los números pares que hay en la lista `numeros` es igual a', suma_pares)

print()

# Suma de los números impares que hay en la lista `numeros`:
print('Suma de los números impares que hay en la lista `numeros`:')

suma_impares = 0

for i in range(len(numeros)):
    if numeros[i] % 2 == 1:
        suma_impares += numeros[i]

print('La suma de los números impares que hay en la lista `numeros` es igual a', suma_impares)

print()

# Iteración con un ciclo for mejorado - iteración por los elementos de una colección:
print('Iteración con un ciclo for mejorado - iteración por los elementos de una colección:')

total = 0

for n in numeros:
    print('El valor actual de `n` es', n)
    total += n

print('Total de la suma de los números de 1 a 10:', total)

print()

# Suma de los números pares de una lista utilizando un ciclo for mejorado:
print('Suma de los números pares de una lista utilizando un ciclo for mejorado:')

suma_pares = 0

for n in numeros:
    if n % 2 == 0:
        suma_pares += n

print('La suma de los números pares que hay en la lista `numeros` es igual a', suma_pares)