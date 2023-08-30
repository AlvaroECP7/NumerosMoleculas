masatomica_C=12
masatomica_H=1
masatomica_O=16
#masa_molar=masa_atomica*n
#masa molar reactivos
masa_molar_C6H5O6=(6 * masatomica_C)+(5 * masatomica_H)+(6 * masatomica_O)
masa_molar_O2=(masatomica_O*2)
#masa molar producto
masa_molar_CO2=(masatomica_C)+(masatomica_O * 2)
masa_molar_H2O=(masatomica_H * 2)+(masatomica_O)
#Coeficientes
coeficiente_1=4
coeficiente_2=17
coeficiente_3=24
coeficiente_4=10
masa_reactivos=(masa_molar_C6H5O6*coeficiente_1) + (masa_molar_O2*coeficiente_2)
masa_productos=(masa_molar_CO2*coeficiente_3) + (masa_molar_H2O*coeficiente_4)

print("reactivo1: " + str(masa_molar_C6H5O6*coeficiente_1))
print("reactivo2: " + str(masa_molar_O2*coeficiente_2))
print("producto1: " + str(masa_molar_CO2*coeficiente_3))
print("producto2: " + str(masa_molar_H2O*coeficiente_4))

print("Numero de masa total de los reactivos es: " + str(masa_reactivos))
print("Numero de masa total del producto es: " + str(masa_productos))

if abs(masa_reactivos - masa_productos) < 1e-6:
    print("La conservaci`on de masas se cumple" )
else :
    print("La conservaci`on NO se cumple" )    
