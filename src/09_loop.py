### Loops ###

"""
Un loop es una estructura de control que permite ejecutar un bloque de código repetidamente mientras se cumpla una condición.
"""

# While loop
# Se ejecuta mientras la condición sea verdadera
my_condition = 0

while my_condition <= 10:
    print(my_condition)
    my_condition += 2  # Incrementa la condición para evitar un bucle infinito

else:
    print("Mi condición es mayor que 10")
    
print("la ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condición es 15 = se detiene la ejecution")
        break
    
    print(my_condition)
    
print("la ejecución continúa")

#For
# Se utiliza para iterar sobre una secuencia (como una lista, tupla o cadena) o un rango de números
# Se ejecuta una vez por cada elemento de la secuencia o rango


my_list = [35, 24, 62, 52, 35, 30, 30, 17]


for element in my_list:
    print(element)

my_tuple = (35, 1.77, "Jaime", "Blanco", "Jaime")

for element in my_tuple:
    print(element)

my_dict = {
    
    "Nombre": "Jaime",
    "Edad": 35,
    "Ciudad": "Buenos Aires",  
    "Pais": "Argentina",
    "Profesion": "Ingenier QA",
    "Lenguajes": {"Python", "Java", "C++"},
    1: 1.77,
} 

# for element in my_dict:
#     print(element)
#     if element == "Pais":
#         break
#     print("Se ejecuta")
# else:
#     print("el bucle for para mi diccionario a finalizado")
    
for element in my_dict:
    print(element)
    if element == "Pais":
        continue # no es muy aconsejado utilizarlo
    print("Se ejecuta")
    
else:
    print("el bucle for para mi diccionario a finalizado")