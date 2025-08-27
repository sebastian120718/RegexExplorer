import re
texto=('Mi edad es -20 y mi hermano tiene 15.   El valor de Pi es 3.1416, y la temperatura promedio es -2.5 grados.   Hoy es True que estoy feliz, pero False que estoy cansado.   Mi nombre es "Matheo" y mi hobby es "Programar en Python".   Tengo varias listas: [1, 2, 3], [10,20], y también una lista negativa [-5, -10, -15].')

patron_entero = r"-?\b\d+\b"
enteros = re.findall(patron_entero, texto)
print("Enteros encontrados:", enteros)


patron_flotante = r"-?\b\d+\.\d+\b"
flotantes = re.findall(patron_flotante, texto)
print("flotantes encontrados:", flotantes)




patron_booleanos = r"\b(True|False)\b"
booleans = re.findall(patron_booleanos, texto, re.IGNORECASE)
print("booleanos encontrados encontrados:", booleans)



patron_strings = r'"(.*?)"'
strings = re.findall(patron_strings, texto)
print("strings encontrados:", strings)



patron_lista = r"\[\s*\d+(?:\s*,\s*\d+)*\s*\]"
listas = re.findall(patron_lista, texto)
print("listas encontrados:", listas)




