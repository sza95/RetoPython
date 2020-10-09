A = int(input("Ingrese el valor para A: "))
print("")

if A <= 0:
    print("Error: El número ingresado es menor a 0")
    exit()
elif A > 0:
    cuadrado = A**A
    raiz = A**0.5
    print(f"Del número A ({A}), su potencia es {cuadrado} y su raíz es {raiz}")