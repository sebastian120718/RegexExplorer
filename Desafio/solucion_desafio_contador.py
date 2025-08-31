import re

texto =("""Mi edad es -20 y mi hermano tiene 15.  El valor de Pi es 3.1416, y la temperatura promedio es -2.5 grados.  Hoy es True que estoy feliz, pero False que estoy cansado.  Mi nombre es "Matheo" y mi hobby es "Programar en Python".  Tengo varias listas: [1, 2, 3], [10,20], y [100,200,300]. : """)

# Enteros
patron_entero = r"-?\b\d+\b"
enteros = re.findall(patron_entero, texto)
print("Enteros encontrados:", enteros, "| Cantidad:", len(enteros))

# Flotantes
patron_flotante = r"-?\b\d+\.\d+\b"
flotantes = re.findall(patron_flotante, texto)
print("Flotantes encontrados:", flotantes, "| Cantidad:", len(flotantes))

# Booleanos
patron_booleanos = r"\b(True|False)\b"
booleans = re.findall(patron_booleanos, texto, re.IGNORECASE)
print("Booleanos encontrados:", booleans, "| Cantidad:", len(booleans))

# Strings
patron_strings = r'"(.*?)"'
strings = re.findall(patron_strings, texto)
print("Strings encontrados:", strings, "| Cantidad:", len(strings))

# Listas
patron_lista = r"\[\s*\d+(?:\s*,\s*\d+)*\s*\]"
listas = re.findall(patron_lista, texto)
print("Listas encontradas:", listas, "| Cantidad:", len(listas))
