A = int(input("Ingrese la cantidad de niñas en el colegio: "))
print("")
B = int(input("Ingrese la cantidad de niños en el colegio: "))
print("")

C = A + B

niñas = round((A*100)/C)
niños = round((B*100)/C)

print(f"El total de niños y niñas es {C}, el porcentaje de niñas es {niñas}% y el de niños es {niños}%")