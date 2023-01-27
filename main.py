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

first_name = input("Cual es tu nombre:")
age = input("Cuantos años tienes:")

print(first_name)
print(age)

# Forzamos el tipo

address: str = "Mi dirección"
address = 32
print(type(address))
