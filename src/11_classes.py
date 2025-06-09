### Classes ###

"""
Una clase es un molde para crear objetos. Un objeto tiene propiedades y comportamientos.

Una clase define las propiedades y comportamientos que tendrán los objetos creados a partir de ella. Las clases son fundamentales en la programación orientada a objetos (OOP) y permiten organizar el código de manera más estructurada y modular. En Python, se definen utilizando la palabra clave class, seguida del nombre de la clase y dos puntos. Las propiedades se definen dentro de la clase y se accede a ellas mediante el uso de self. Los métodos son funciones definidas dentro de una clase que operan sobre las propiedades del objeto.
Se usa camelcase para definir la clase
"""

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname):
       self.full_name = f"{name} {surname}"
       
    def walk(self):
        print(f"{self.full_name} está caminando")
        

my_person = Person("Jaime", "Blanco")
print(my_person.full_name)
my_person.walk()