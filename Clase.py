
import sys
import keyword

print("Versión de Python:", sys.version)

palabras_reservadas = keyword.kwlist
print("\nPalabras reservadas de Python:")
for palabra in palabras_reservadas:
    print("- " + palabra)