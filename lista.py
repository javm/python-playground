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