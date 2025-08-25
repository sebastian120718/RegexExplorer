// Reto 1: Buscar enteros en un texto usando regex en Java
// Paso a paso:
// 1. Leer el texto de entrada.
// 2. Definir una expresión regular para encontrar números enteros.
// 3. Buscar todos los enteros en el texto.
// 4. Imprimir los resultados.

import java.util.regex.*;

public class Reto1 {
    public static void main(String[] args) {
        String texto = "En 1945, ocurrio la 2 guerra mundial llevandonos a hoy en dia al 2025, eso sin antes haber ocurrido una pandemia en 2020.";
        // Expresión regular para enteros (positivos y negativos)
        String patron = "-?\\b\\d+\\b";
        Pattern pattern = Pattern.compile(patron);
        Matcher matcher = pattern.matcher(texto);
        System.out.print("Enteros encontrados: ");
        while (matcher.find()) {
            System.out.print(matcher.group() + " ");
        }
        System.out.println();
        // Paso a paso:
        // 1. Cambia el texto de prueba.
        // 2. Modifica la expresión regular si es necesario.
        // 3. Ejecuta el programa y observa los resultados.
    }
}
