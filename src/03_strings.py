### STRINGS ###

my_string = "Mi String"
my_other_string = "Mi otro String"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string \n con salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste e un string con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un string | \n escapado"
print(my_scape_string)

### Formateo ###
print("===" * 30)

"""
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
"%.number of digitsf" - Floating point numbers with fixed precision
"""

name, surname, age = "Jaime", "Blanco", 35

print("mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"mi nombre es {name} {surname} y mi edad es {age}")

### DESEMPAQUETADO DE CARACTERES ###
print("===" * 30)

language = 'python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

### DIVISIÓN ###
print("===" * 30)

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)


#Reverse
print("===" * 30)

language_slice = language[::-1]
print(language_slice)

# Funciones
print("===" * 30)

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("Py"))
print("Py" == "py")
