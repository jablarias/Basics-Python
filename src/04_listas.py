### Listas ###
print("===" * 30)

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 35, 30, 30, 17] # el valor 30 se repite

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Jaime", "Blanco"]
print(my_other_list)

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])  
print(my_other_list[-4])
print(my_other_list.count("Blanco"))
print(my_list.count(30))
# print(my_other_list[4]) IndexError
# print(my_other_list[5]) IndexError


age, height, name, surname = my_other_list
print(name)
print(surname)
print(age)
print(height)

print(my_list + my_other_list)
# print(my_list - my_other_list)

my_other_list.append("JabaDev") # appened sirve para agregar elementos a la lista en este caso  a my_other_list
print(my_other_list)

my_other_list.insert(1, "azul") # Inserta el calor dado en la lista segun el indice asignado
print(my_other_list)

my_other_list.remove("azul") # remueve el item indicado de la lista
print(my_other_list)

my_list.remove(30) # Elimina el primer elemento que a encontrado según el valor dado
print(my_list)

print(my_list.pop()) # Sirve para sacar el ultimo elemento de la lista por defoult
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)

print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)


print(my_new_list[1:3])



"""
my_list = "Hola Python"                                                            
print(my_list)              
print(type(my_list))   
### Esto cambia el valor de la variable por lo que la variable my_list deja de ser una lista para convertirse en un string

"""
