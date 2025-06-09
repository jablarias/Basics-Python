### TUPLES ###

"""Las tuplas son estructuras de datos inmutables, es decir, no se pueden modificar una vez creadas.
    Se definen utilizando paréntesis () y pueden contener elementos de diferentes tipos. Las tuplas son útiles para almacenar datos que no deben cambiar a lo largo del tiempo, como coordenadas geográficas o fechas. A diferencia de las listas, las tuplas no admiten operaciones de modificación, como agregar o eliminar elementos. Sin embargo, se pueden concatenar y repetir utilizando los operadores + y * respectivamente."""
    

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Jaime", "Blanco", "Jaime")
my_other_tuple = (35, 60, 30)


print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) index error
#print(my_tuple[-6]) index error

print(my_tuple.count("Jaime"))
print(my_tuple.index("Blanco"))
print(my_tuple.index("Jaime"))

# my_tuple [1]= 1.80 'tuple' object does not support item assigment

my_plus_tuple = my_tuple + my_other_tuple
print(my_plus_tuple)

print(my_plus_tuple[3:6])

# Para modificar un tupla lo mejor es convertirla a lista para poder mutarla

my_tuple = list(my_tuple)
print(type(my_tuple)) 

my_tuple[4] = "JabaDev"
my_tuple.insert(1, "Azul")
print(my_tuple)
#aquí podemos ver los nuevos valores de la lista
my_tuple = tuple(my_tuple)# Convertimos la lista a tupla
print(my_tuple)
print(type(my_tuple))

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined



