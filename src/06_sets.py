### SETS ###
"""
- Un set es una colección desordenada de elementos únicos."
"""

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Jaime", "Blanco", 35}
print(type(my_other_set))
print(len(my_other_set))

# print(my_other_set[1]) TypeError: 'set' object is not subscriptable

my_other_set.add("JabaDev")
print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("JabaDev") # No admite repetidos
print(my_other_set)

# Validamos si el elemento se encuentra dentro de la lista
print ("Blanco" in my_other_set)
print ("Blanc" in my_other_set)

my_other_set.remove("Blanco")
print (my_other_set)

my_other_set.clear() #Borramos los elementos de la lista
print(len(my_other_set)) 

del my_other_set 
# print(my_other_set) NameError: name 'my_other_set' is not defined 

my_set = {"Jaime", "Blanco", 35}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Python", "HTML", "CSS", "JavaScript" }

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"C#", "Swift"}))

print(my_new_set.difference(my_set))