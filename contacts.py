import csv

class Address():
    '''Street, Street number, Interior number, Zipcode, municipality, city, state or Province, country'''
    def __init__(self, 
                 street, 
                 exterior_number, 
                 interior_number=None,
                 neighborhood=None, 
                 zipcode=None,
                 municipality=None,
                 city=None,
                 state=None,
                 country=None
                 ):
        self.street=street
        self.exterior_number=exterior_number 
        self.interior_number=interior_number 
        self.neighborhood=neighborhood
        self.zipcode=zipcode
        self.municipality=municipality
        self.city=city
        self.state=state
        self.country=country
        
    def __str__(self):
        return self.street + " " + self.exterior_number + " " + (self.interior_number or "") + self.neighborhood + " " + self.zipcode

# self = {name, number, address}
#
class Person():
    '''Person class defines a person'''
    def __init__(self, name, number, address):
        self.name = name
        self.number = number
        self.address = address
    def __str__(self):
        return self.name + ': ' + self.number + '; ' + str(self.address)

class Contacts():
    '''Contacts class defines a list of contacts'''
    def __init__(self):
        self.contacts = []
    def add(self, person):
        self.contacts.append(person)
        
    def getNamesBeginsWith(self, letter):
        results = []
        # para cada self.contacts c
        # if c.name empieza con letter
        # agrega c en results
        for c in self.contacts:
            if c.name[0] == letter:
                results.append(c)
        return results
        
    def printAll(self):
        #para cada contacto en la lista contacts: 
        #imprimir nombre y número
        self.contacts.sort(key=lambda x: x.name, reverse=True)
        for c in self.contacts:
            print(c)
            

address1 = Address(street='Calle 10', exterior_number='Lote 20',neighborhood='La Veleta',
                   zipcode='077760', municipality='Tulum', city='Tulum', state='Quintana Roo',
                   country='México')

address2 = Address(street='Calle Amapola', exterior_number='10', neighborhood='Huetor Vega', 
                   zipcode='18198', municipality='Granada', city='Granada', state='Andalucia',
                   country='España')

person1 = Person('Antonio', '984 127 5287', address1)
person2 = Person('Carmen', '602 431 203', address2)
person3 = Person('Lupe', '616 635 807', address2)
contacts = Contacts()

contacts.add(person3) 
contacts.add(person2)
contacts.add(person1)
#contacts.printAll()

letter = "L"
starts_with = contacts.getNamesBeginsWith(letter)

print("Imprimiendo nombres que inician con " + letter)

# Para cada elemento x en starts_with
#     imprime(x)
for p in starts_with:
    print(p)

# Aquí vamos a leer linea por linea
with open("./contacts.csv", "r") as contacts_file:
    csvreader = csv.reader(contacts_file)
    index = 0

    for row in csvreader:
        if index > 0:
            print(row)
        index = index + 1

    
# [['Nombre', 'Telefono', 'Calle'], ['Carmen', '602 431 203', 'Calle Amapola'], row2]
