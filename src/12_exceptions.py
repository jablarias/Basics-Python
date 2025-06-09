### Exceptions Handling ####

"""
Una excepción es un evento que interrumpe el flujo normal de un programa. Las excepciones pueden ser causadas por errores en el código, como intentar dividir por cero, acceder a un índice fuera de rango en una lista o intentar abrir un archivo que no existe. Cuando ocurre una excepción, Python genera un objeto de excepción y lo lanza (raise). Si no se maneja adecuadamente, la excepción puede hacer que el programa se detenga abruptamente.

El manejo de excepciones en Python se realiza mediante el uso de bloques try y except. El bloque try contiene el código que puede generar una excepción, mientras que el bloque except contiene el código que se ejecutará si se produce una excepción. También se pueden usar bloques finally para ejecutar código que debe ejecutarse independientemente de si se produjo una excepción o no. Esto es útil para liberar recursos, cerrar archivos o realizar tareas de limpieza.
"""

number_one = 5 
number_two = 1
number_two = "1"

# Try / Except

try:
    print('number_one' + 'number_two')
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
    
    
# Try / Except / else

try:
    print('number_one' + 'number_two')
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error")
    
else:
    # Se ejecuta si no se produce una excepción
    print("La ejecución continua correctamente")
    
finally: #Opcional
    # Se ejecuta siempre
    print("La ejecución continua")
    
    
    
try:
    print('number_one' + 'number_two')
    print("No se ha producido un error")
except TypeError:
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error")
    
    

    



