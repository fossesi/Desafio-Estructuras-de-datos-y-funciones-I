import sys

if sys.argv[0] != "word_count.py":
    print("debe escribir: python word_count.py")
    sys.exit(1)

with open("lorem_ipsum.txt", "r") as file:
    texto=file.read()

#  cuenta la cantidad de caracteres distintos del texto, incluyen letras mayúsculas, letras minúsculas, comas, puntos, espacios y saltos de línea
caracteres = set(texto)
print(f"El número de caracteres distintos es: {len(caracteres)}")

# cuenta la cantidad de palabras distintas del texto, tanto en mayúscula como en minúscula
palabras = set(texto.split(" "))
print(f"El número de palabras distintas es: {len(palabras)}")