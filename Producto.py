A = int(input("Ingrese el valor para A: "))
print("")
B = int(input("Ingrese el valor para B: "))
print("")
C = int(input("Ingrese el valor para C: "))

if A < 0:
    res = A*B*C
    print("")
    print(f"El resultado de esta operación es: {res}")
elif A > 0:
    res = A+B+C
    print("")
    print(f"El resultado de esta operación es: {res}")