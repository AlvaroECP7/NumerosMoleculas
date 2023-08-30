elementos_quimicos = set()
terminar = False

while not terminar:
    entrada = input("Introduce un elemento químico en español (o 'fin' para terminar): ")

    if entrada.lower() == "fin":
        terminar = True
    else:
        try:
            elementos_quimicos.add(entrada)
        except:
            print("Error: Elemento químico no válido. Introduce un elemento válido.")


print("\nTotal de elementos ingresados:", len(elementos_quimicos))
