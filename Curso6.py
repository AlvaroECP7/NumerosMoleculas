resultado_1 = 1.321e-4 + 8.5e-2
resultado_1 = "{:.2e}".format(resultado_1)
resultado_1 = resultado_1.replace("e-", " * 10^")
print("Resultado 1: " +  resultado_1)


resultado_2 = 1.71e3 - 2.01e2
resultado_2 = "{:.2e}".format(resultado_2)
resultado_2 = resultado_2.replace("e+", " * 10^")
print("Resultado 2: " +  resultado_2)


resultado_3 = 7.4e5 * 7.2e4
resultado_3 = "{:.2e}".format(resultado_3)
resultado_3 = resultado_3.replace("e+", " * 10^")
print("Resultado 2: " +  resultado_3)


resultado_4 = 7.4e5 / 7.2e4
resultado_4 = "{:.2e}".format(resultado_4)
resultado_4 = resultado_4.replace("e+", " * 10^")
print("Resultado 2: " +  resultado_4)
