### Dictionaries ###

""" Los diccionarios son estructuras de datos que almacenan pares de clave-valor.
    Cada clave es única y se utiliza para acceder a su valor correspondiente. Los diccionarios son mutables, lo que significa que se pueden modificar después de su creación. Se definen utilizando llaves {} y los pares de clave-valor se separan por comas. Las claves pueden ser de cualquier tipo inmutable, como cadenas, números o tuplas, mientras que los valores pueden ser de cualquier tipo.
"""

my_dict = dict()
print(my_dict) # {}
print(type(my_dict)) # <class 'dict'>


my_other_dict = {
    
    "Nombre": "Jaime",
    "Edad": 35,
    "Ciudad": "Buenos Aires",
    "Pais": "Argentina",
    "Profesion": "Ingenier QA",
    1: "Python",
}

my_dict = {
    
    "Nombre": "Jaime",
    "Edad": 35,
    "Ciudad": "Buenos Aires",  
    "Pais": "Argentina",
    "Profesion": "Ingenier QA",
    "Lenguajes": {"Python", "Java", "C++"},
    1: 1.77,
} 

print(my_dict) # 
print(my_other_dict) # 
print(type(my_other_dict)) # <class 'dict'>

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])
my_dict["Nombre"] = "Juan"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Direccion"] = "Av. Corrientes 1234"
print(my_dict["Direccion"])

print(my_dict)

del my_dict["Direccion"] # Eliminar una clave y su valor OJO no hay vuelta atras
print(my_dict)

print("Juan" in my_dict) # False porque busca el valor
print("Nombre" in my_dict) # True porque busca la clave

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = my_dict.copy() # Copia el diccionario
print(my_new_dict) #
print(my_dict) #

my_list = ["Nombre", "piso", 1]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, ("Jaime","Blanco"))#no es posible asignar valores a las claves desde la operacion fromkeys
print((my_new_dict))

print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))

print(list(my_new_dict.values()))



