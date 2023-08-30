# Crea una matriz de 3x3 e imprime la suma de los elementos en su diagonal (traza).
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

suma = sum(matriz[i][i] for i in range(3))
suma2 = sum(matriz[i][2 - i] for i in range(3))


print("Matriz:")
for numero in matriz:
    print(numero)


print("\nSuma de la diagonal (135`):", suma)
print("\nSuma de la diagonal (45`):", suma2)