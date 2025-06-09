### Conditionals ###

"""Los condicionales son estructuras de control que permiten ejecutar un bloque de código si se cumple una condición determinada. En Python, los condicionales se implementan utilizando la instrucción if, seguida de una expresión booleana y un bloque de código indentado. También se pueden utilizar las instrucciones elif y else para manejar múltiples condiciones y casos alternativos.
"""

# ejemplo de condicional simple

my_condition = False

if my_condition:
    print("Se ejecuta la condición del if")
    
my_condition = 5 * 5
    
if my_condition == 10:
    print("Se ejecuta la condición del segundo if") # se ejecuta por que es un true
    
if my_condition >= 10:
    print("Se ejecuta la condición del tercer if")
    
if my_condition > 10:
    print("Es mayor que 10 tercer if")# no se ejecuta porque es falso
else:
    print("No es mayor que 10")# Imprime este Camino porque 10 no es mayor que 10

    
if my_condition > 10 and my_condition < 20:
    print("Es > que 10 ó < que 20")
    
elif my_condition == 25:
    print("Es igual a 25")
    
else:
    print("Es <= a 10 ó >= 20 ")
    
    
print("la ejecución continua") 


my_string = "Mi cadena de texto esta llena"

if my_string:
    print ("Mi cadena de texto está vacia")

if my_string == "Mi cadena de texto esta llena":
    print ("Mi cadena de texto está vacia")
    
if my_string == "Mi cadena de textoooooooo":
    print ("Mi cadena de texto está vacia")