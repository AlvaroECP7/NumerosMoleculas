# Busca la temperatura de fusión en Celsius de 5 metales y guárdalos en una lista. Imprime las temperaturas en Kelvin
temperaturas_Celsius = [1238, 260.32, 3064.18, 952, 1567.7]


def celsius_a_kelvin (celsius):
    return celsius + 273


print("Temperaturas de fusión en Kelvin:")
for temperatura_C in temperaturas_Celsius:
    temperatura_K = celsius_a_kelvin(temperatura_C)
    print(f"{temperatura_C} °C = {temperatura_K:.2f} K")
