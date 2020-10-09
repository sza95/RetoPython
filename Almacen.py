A = int(input("Ingrese el valor para el producto A: "))
print("")
B = int(input("Ingrese el valor para el producto B: "))
print("")
C = int(input("Ingrese el valor para el producto C: "))
print("")
Mes = int(input("Ingrese el mes en el que esta: "))

D = A+B+C
descuento = (D*(15/100))
total = D-(descuento)

if Mes == 10:
    print(f"Como estamos en el mes de Octubre usted recibe un 15% de descuento en su compra {round(total)}")
elif Mes != 10:
    print(f"Como no estamos en el mes de Octubre usted no recibe descuento {round(D)}")


