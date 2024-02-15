# Hearth deasea risk
age = input("Enter the age here: ")
age = int(age)

bmi = input("Enter the BMI here:")
bmi = float(bmi)

young = age < 45
slim = bmi < 22.0

if young:
  if slim:
    risk = 'low'
  else:
    risk = 'medium'
else:
  if slim:
    risk = 'medium'
  else:
    risk = 'high'
    
print("The risk is: " + risk)