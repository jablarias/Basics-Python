### functions ###

"""
Las funciones son bloques de código reutilizables que realizan una tarea específica. Se definen utilizando la palabra clave def, seguida del nombre de la función y paréntesis que pueden contener parámetros. Las funciones pueden devolver valores utilizando la palabra clave return. Las funciones son útiles para organizar el código, evitar la repetición y mejorar la legibilidad.
"""

def my_function():
    print("Esto es una función")
    
my_function()
my_function()
my_function()

def plus_two_values (first_number: int, second_number): #las funciones pueden recibir parámetros y devolver valores dinámicamente
    print(first_number + second_number)
    
plus_two_values(5, 7) # si los parametros son int ejecuta la operación y devuelve el resultado
plus_two_values("5", "7")# si son de tipo string los concatena
plus_two_values(1.57, 5.68) # si son de tipo float los suma
plus_two_values(1, 5.68) # si son de tipo int y float los suma

def plus_two_values_with_retur(first_value, second_value):
    return first_value + second_value


my_result = plus_two_values_with_retur(5 , 10)
print(my_result)

def print_name( name, surname):
    print(f"{name} {surname}")
    
print_name("Jaime", "Blanco ")

def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name}, {surname}, {alias}")
    
print_name_with_default ("Jaime", "Blanco")
print_name_with_default ("Jaime", "Blanco", "JabaDev")

def print_text(*text):
    print(text)

print_text("Hola", "Python", "JabaDev")
print_text("Hola Python")
