# Imprime los numero del 1 al 10
# range(1, 11) --> [1, 2, 3, 4, 5, 6, ...10]
# para cada numero 'n' en range(1,11)
#   imprime(n)

for n in range(1, 11):
  print(n)

print("\nCreando lista e imprimendo...")
l = [4, 5, 3, 1]
for m in l:
  print(m)


# Imprimir el doble (multiplicado por 2) de cada uno de los números en la lista
# i-> f -> s
# f(i) -> s
print("\nImprime el doble de cada uno de los números de la lista")
for m in l:
  print(2*m)



print("\nImprime cada uno de los caracteres en la cadena de caracteres")  
s = "Carmen Framil Heredia"
for c in s:
  print(c)

print("\nImprime la lista l 5 veces separando cada numero con un 'for'")

for i in range(0,5):
  for e in l:
    print(e)
  print("\n")


print("\nImprime la lista l 5 veces separando cada numero con un 'while'")
j = 0
# mintras (se cupmpla la condicion):
#  ejecuta bloque
while(j < 5):
  for e in l:
    print(e)
  print("\n")
  j = j + 1
