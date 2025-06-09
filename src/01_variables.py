# Variables
# convenciones de nombres usadas en Python
# lower_case: se usa para variables y funciones
# snake_case: se usa para variables y funciones

str_variable = "My string variable"
print(str_variable)
print(type(str_variable))

int_variable = 10
print(int_variable)
print(type(int_variable))

#  transformar un int en str
my_int_to_str_variable = str(int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

flt_variable = 10.5
print(flt_variable)
print(type(flt_variable))

bool_variable = False
print(bool_variable)
print(type(bool_variable))


# concatenando variables en un print:
print(str_variable, int_variable, flt_variable, bool_variable)
print("Estes es el valor de :", bool_variable)

# Algunas funciones del sistema
print(len(str_variable))  # devuelve la longitud de una cadena

# Variables en una sola linea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Jaime", "Blanco", "Jablarias", 35
print("me llamo:",name, surname,"mi edad es:", age, "Y mi alias es:", alias)

# tipo input pide los datos en consola y los almacena en una variable
"""
name = input("¿Cuál es tu nombre?")
age = input("¿Cuál es tu edad?")
print("Hola", name, "tienes", age, "años")
"""

# Cambiamos el tipo de dato

name = 35
age = "Jaime"
print("Hola", name, "tienes", age, "años")

# ¿Forzamos el tipo de dato?

address: str = "Mi dirección"
address = '5'
address = 'True'
address = '10.5'
print(type(address))











