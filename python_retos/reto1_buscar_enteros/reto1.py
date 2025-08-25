# Reto 1: Buscar enteros en un texto usando regex
# Paso a paso:
# 1. Leer el texto de entrada.
# 2. Definir una expresión regular para encontrar números enteros.
# 3. Buscar todos los enteros en el texto.
# 4. Imprimir los resultados.

import re

texto = "En 2023, había 15 estudiantes y 3 profesores."

# Expresión regular para enteros (positivos y negativos)
patron = r"-?\b\d+\b"

# Buscar todos los enteros
enteros = re.findall(patron, texto)

print("Enteros encontrados:", enteros)
# Paso a paso:
# 1. Cambia el texto de prueba.
# 2. Modifica la expresión regular si es necesario.
# 3. Ejecuta el script y observa los resultados.
