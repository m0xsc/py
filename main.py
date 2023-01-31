# Variables

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print

print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)


# Funciones del sistema

print(len(my_int_to_str_variable)) # Cuenta los caracteres de la varibale

# Variables en una sola línea

name, surname, alias, age = "m0", "xsc", "m0xsc", 70
print("Me llamo", name, surname, "tengo", age, "años", "y mi alias es", alias)

# Inputs

#first_name = input("Cual es tu nombre:")
#age = input("Cuantos años tienes:")

#print(first_name)
#print(age)

# Forzamos el tipo

address: str = "Mi dirección"
address = 32
print(type(address))


# Operadores Aritmeticos

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3)

#print("Hola " + 5) # Error #
print("Hola " * 5) 
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print("Hola " * int(my_float))

# Operadores Comparativos

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Zola") # Ordenación alfabética por ASCII
print(len("Hola") <= len("Python")) # Cuenta caracteres
print("Hola" == "Python")
print("Hola" != "Python")

# Operadores lógicos

print(3 > 4 and "Hola" > "Python")
print(3 < 4 or "Hola" > "Python")
#print(3 > 4 not "Hola" > "Python")

# Strings

my_string = "Mi String"

print(len(my_string)) # len() sirve para medir la longitud

my_new_line_string = "Este es un String \ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulacion"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "m0", "xsc", 70

print("Mi nombre es {} {} y mi edad es {}" .format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))

# Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3]
print(language_slice)

# Funciones

print(language.capitalize()) # Ha puesto la primera letra de la palabra python en mayuscula
print(language.upper()) # Aparece python todo en mayusculas
print(language.count("t")) # Cuenta las letras
print(language.isnumeric()) # Compurba y nos dice si python es un nuemero
print("1".isnumeric()) # Nos dice si 1 es un nuemero
print(language.lower()) # Aparece python todo en minusculas
print(language.lower().isupper()) # Pasa todo a minusculas y luego comprueba si es esta en mayusuclas
print(language.startswith("py")) # Te dice si empieza con x letras


# Listas

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "m0", "xsc"]
print(type(my_other_list)) # Me dice de que clase es el print que vamos a hacer

print(my_other_list[0]) # Acceder a un dato determinado poniendo su posicion
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])

age, height, name, surname = my_other_list
print(name)

print(my_list + my_other_list)

my_other_list.append("m0xsc") # Agrega un elemento a la lista
print(my_other_list)

my_other_list.insert(1, "Amarillo") # Agrega un elemento a la lista en una posicion determinada
print(my_other_list)

my_other_list.remove("Amarillo") # Elimina un valor de la lista
print(my_other_list)

my_list.remove(30) # Elimina un valor de la lista
print(my_list)

my_list.pop() # Quita el ultimo elemento de la lista, tambien puede eliminar un elemento especifico
print(my_list)

print(my_list.pop()) # Quita el ultimo elemento de la lista y me lo devuelve
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

my_list.clear() # Limpia la lista por completo
print(my_list)

my_new_list = my_list.copy() # Crea una nueva variable y copia la lista

my_list = "Hola Python"
print(type(my_list))

# Tuplas

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "m0", "xsc")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count(35)) # Cuenta el numero de veces que se repite el valor en la tupla
print(my_tuple.index("xsc")) # Te dice donde esta posicionado este valor en la tupla

#my_tuple[1] = 1.80 # Error (es inmutable, es decir, no se puede cambiar el valor establecido)
#print(my_tuple)

# Sets

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_other_set = {"m0", "xsc", 35}
print(type(my_other_set))

my_other_set.add("m0xsc")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

#uso del union falta aqui

# Diccionarios
