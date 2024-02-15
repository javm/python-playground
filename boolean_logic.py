# x >= 0  es equivalente (x > 0)->A OR (x=0)->B
# Tabla de verdad del OR
# A  | B | (A OR B)
# F  | F | F
# V  | F | V
# F  | V | V
# V  | V | V


def is_positive(x):
  # si x > 0 entonces regresa True
  # sino regresa False
  if x >= 0:
    return True
  else:
    return False

# a = input("Enter a number to check if this is positive: ")
# print("is positive?", is_positive(int(a)))

# Tabla de verdad del AND, tanto A como B son verdaderos
# A  | B | (A AND B)
# F  | F | F
# V  | F | F
# F  | V | F
# V  | V | V

# not (A AND B) equivalente a (notA OR notB)

def is_even(x):
  return x % 2 == 0

def is_positive_even(x):
  if x == 0:
    return True
  if x > 0 and is_even(x):
    return True
  else:
    return False

#b = input("Enter a number to check if this is a positive even:")
#print("is positive?", is_positive(int(b)))
#print("is positive even?", is_positive_even(int(b)))
#print("is negative odd", not is_positive_even(int(b)))


# pH LevelSolution Category
# 0-4 Strong acid
# 5-6 Weak acid
# 7 Neutral
# 8-9 Weak base
# 10-14 Strong base

def is_in(x, a, b):
  return x >= a and x <= b

# Input pH (el argumento un valor)
def ph_text(ph):
  # si ph esta entre 0 y 4 regresa 'String acid'
  if is_in(ph, 0, 4):
    print("Strong acid")
    return
  if is_in(ph, 5, 6):
    print("Weak acid")
    return
  if ph == 7:
    print("Neutral")
    return
  if ph == 8 or ph == 9:
    print("Weak base")
    return
  if is_in(ph, 10, 14):
    print("Strong base")
    return
  
ph_val = input("Introduce the ph value: ")
ph_text(int(ph_val))  
