### Operadores Aritmeticos ###
print("===" * 30)

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)  # division normal
print(3 % 4)  # modulo
print(3 // 4) # division entera
print(2 ** 3) # potencia

# multiples operadores en una sola linea con int
print(3 + 4 * 5 - 2 / 3) # 3 + (4 * 5) - (2 / 3)
print(3 + 4 * 5 - 2 // 3) # 3 + (4 * 5) - (2 // 3)

# operadores con string
print("hola " + "Python "+"¿Qué tal?")
print("hola " * 3)
print("hola " + str(5)) 
print("hola " * 3 + "¿Qué tal?")
print("hola " * ( 2 ** 3 ) ) # 8 veces "hola "


my_float = 2.5 * 2
print("hola " * int(my_float)) # 5 veces "hola "
print("hola " * int(2.5)) # 2 veces "hola "

### operadores de comparacion ###
print("===" * 30)

print(3 > 4) # mayor que
print(3 < 4) # menor que
print(3 >= 4) # mayor o igual que
print(4 <= 4) # menor o igual que  
print(3 == 4) # igual que
print(3 != 4) # diferente de

# test

print("Hola" > "Python") 
print("Hola" < "Python")
print("aaaa" >= "abaa") # Ordenación alfabetica por ASCII
print(len("aaaa") >= len("abaa")) # Cuenta caracteres
print("Hola" <= "Python")  
print("Hola" == "Hola")
print("Hola" != "Python")

### Operadores Lógicos ###
# se puede incluir una divicion para que se vea reflejada en la terminal en esta linea de codigo?
print("===" * 30)# Asi separo cada contexto en la terminal
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not(3 > 4))
print(False == False)
 
