#number, string, character, boolean: True or False, lista
# Carmen sería string
# 'c' sería un caracter
# Crear una lista vacía y guardarla en una variable
l = []
# Imprime el tamaño de la lista
print("tamaño: ", len(l))

# Agrega un elemento a la lista
l.append('a')
print(l)
print("tamaño: ", len(l))

l.append('b')
print(l)

l.insert(1, 'c')
print(l)

l.insert(1, 'd')
print(l)

l.insert(0, 'e')
print(l)
print(len(l))


m = ['x', 'y'] + l
print(m)
print(l)

print(l.pop())
print(l[len(l) - 1])
print(l)

#Vaciamos la lista
n = l.copy()
while(len(l) > 0):
    print(l.pop())
    
print("l:", l)
print("n:", n)

l = n

print("l:", l)
print("n:", n)

m = [-11, 2, -1, 4, 5, 6]

# Crear una nueva lista que intercambie del lugar el primer elemento y el último

# Extraer el último elemento de la lista m

print(m[-1])
print(m[-2])

print(m[len(m) - 1])

# Imprimir la lista m en órden inverso

m.reverse()
print("m", m)

start = [3, 4]
start.extend(m)

# Para cada elemento en turno 'e' en la lista start
# imprime(e)

for e in start:
    print(e)

#funcion(a, b){
# haz con f1 lo que quieras
#}


for e in range(0, len(start), 2):
    print(start[e])



#numeros pares sin repeticion
#en lugar de imprimirlos meterlos en una lista
#


# TODO: Extraer los elementos pares de start
#para cada elemento en la lista start
#si el elemento en turno es par y no esta en lista pares 
#se saca de la lista start y se mete en la lista pares
#imprimir numeros pares
pares=[]
impares=[]
print('numeros pares')
for c in start:
    if (c%2==0) and not(c in pares):
        pares.append(c) 
    if (c%2==1) and not(c in impares):
        impares.append(c) 
print('pares:', pares)
print('impares:', impares)

#suma de estos numeros (los que hay en pares)
sumapares=0
for c in pares:
    sumapares=sumapares+c
print('sumapares:', sumapares)

#suma de estos numeros (los que hay en impares)
sumaimpares=0
for c in impares:
        sumaimpares=sumaimpares+c
print('sumaimpares:', sumaimpares)

lista1 = start.copy()

num = 4
# num in start
# pirmer indice = 0
# primer_numero = start[0]
# lista1 =
# 8, 6, 7, 9, 4, 2
# current
# indice

# fin = False
# index = 0


# mientras(not fin) repite:
#  current = lista1[index]
#  fin = compara(current, num) # current == num 
#  index = index + 1

# index = 5
# list1[index]

# t0     0           false
# t1     1      8    false
# t2     2       6    false

# index | current | fin
# 0     |    8    | False
# 1     |    6    | False
# 2     |    7    | False 
# 3     |    9    | False
# 4     |    4    | False
# 5               | True 
