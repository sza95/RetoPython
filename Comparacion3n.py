A = int(input("Ingrese el valor para A: "))
print("")
B = int(input("Ingrese el valor para B: "))
print("")
C = int(input("Ingrese el valor para C: "))



if A > B and A > C :
    print(f"A ({A}) es mayor que B ({B}) y C ({C})")
elif B > A and B > C:
    print(f"B ({B}) es mayor que A ({A}) y C ({C})")
elif C > A and C > B:
    print(f"C ({C}) es mayor que A ({A}) y B ({B})")