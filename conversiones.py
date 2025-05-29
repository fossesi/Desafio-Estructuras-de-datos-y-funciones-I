import sys

if len(sys.argv) < 5:
    print("el comando necesita cuatro argumentos: python conversiones.py 0.0 0.0 0.0 00000")
    sys.exit(1)

# Conversión
# Peso chileno a sol peruano: 0.0046
# Peso chileno a Peso argentino: 0.093
# Peso chileno a Dólar americano: 0.0013

conv_sol = float(sys.argv[1])
conv_peso_ar = float(sys.argv[2])
conv_usd = float(sys.argv[3])
cl_peso = int(sys.argv[4])

cl_sol = conv_sol * cl_peso
cl_arg = conv_peso_ar * cl_peso
cl_usd = conv_usd * cl_peso

print(f"Los {cl_peso} pesos equivalen a: ")
print(f"{cl_sol} Soles")
print(f"{cl_arg} Pesos Argentinos")
print(f"{cl_usd} Dólares")