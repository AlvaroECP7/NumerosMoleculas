n_avogadro= 6.022 * (10**23)

def  n_moleculas(masa, masa_molar):
    moles=masa/masa_molar

    n_moleculas=moles*n_avogadro
    n_moleculas = "{:.2e}".format(n_moleculas)
    n_moleculas = n_moleculas.replace("e+", " * 10^")
    
    print("El numero de moleculas es: " +  n_moleculas)


masa = float(input("Inserta masa: "))
masa_molar= float(input("Inserte masa molar: "))
n_moleculas(masa, masa_molar)
    
                                  