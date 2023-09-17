nombre = "Marlon" 
numero_entero = 5
numero_flotante = 1.30
print(f"Hola {nombre} hagamos una suma ", f"la suma de {numero_entero}", f"mas {numero_flotante}", f"muestrame el resultado {numero_entero+numero_flotante}", sep="\n")

es_verdadero = bool(input("¿Es verdadera la respuesta? True/False: "))
print(f"la respuesta es {es_verdadero}")

# Límite de los enteros en Python:
# En Python, los enteros no tienen un límite fijo en cuanto a su tamaño. Esto significa que puedes trabajar con enteros extremadamente grandes sin preocuparte por desbordamientos de memoria.

# Ejemplo:
# num_entero_grande = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
# print(num_entero_grande)  # No hay problema en trabajar con enteros tan grandes.

# Límite de los flotantes en Python:
# Los números de punto flotante en Python utilizan el estándar IEEE 754 de doble precisión, que reserva 64 bits para representar números en coma flotante. Esto impone un límite en la precisión y el rango de los números de punto flotante.

# Ejemplo de límite de precisión:
# num_float = 0.1 + 0.1 + 0.1
# print(num_float)  # El resultado podría no ser exactamente 0.3 debido a limitaciones de precisión de los números en coma flotante.

# Límite de rango:
# Los números de punto flotante tienen un rango limitado. Puedes representar números muy grandes o muy pequeños, pero fuera de ese rango, se perderá precisión.

# Ejemplo de límite de rango:
# num_muy_grande = 1e308  # Esto es un número de punto flotante muy grande
# num_muy_pequeno = 1e-308  # Esto es un número de punto flotante muy pequeño

# Ten en cuenta que estos límites son inherentes a la representación de números en coma flotante en la mayoría de los lenguajes de programación y no son específicos de Python.





# Pedimos al usuario que ingrese el valor de n
n = int(input("Ingresa un valor entero positivo para n: "))

# Usamos la fórmula para la suma de los primeros n números pares
suma = n * (n + 1)

# Imprimimos el resultado
print(f"La suma de los primeros {n} números pares es {suma}.")