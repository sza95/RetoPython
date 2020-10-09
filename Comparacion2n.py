A = int(input("Ingrese el valor para A: "))
print("")
B = int(input("Ingrese el valor para B: "))

if A > B:
    print(f"A ({A}) es mayor que B ({B})")
elif A < B:
    print(f"B ({B}) es mayor que A ({A})")
elif A == B:
    print(f"A ({A}) y B ({B}) son iguales")