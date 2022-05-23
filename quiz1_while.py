#Input 


C1 = int(input("Digite la Capital de Pedro($): "))
C2 = int(input("Digite la Capital de Juan($): "))
C3 = int(input("Digite la Inversion($): "))

meses = 0

#processing

while ((C1 + C2) < C3):
    C1 = C1 + (C1 * 0.03)
    C2 = C2 + (C2 * 0.04)
    meses = meses + 1

#input

print("Según el interes de Pedro de " + str(round(C1, 2)) + " y del interes de Juan de " + str(round(C2, 2)) + " ,el tiempo para que se pueda hacer la inversión de " + str(C3) + " es de " + str(meses) + " meses.")