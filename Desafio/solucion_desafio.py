import re
texto=(input("escribe un texto entre estas ' ':"))

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




