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


# TODO: Extraer los elementos pares de start