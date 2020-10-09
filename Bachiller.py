respuesta = input("¿Tiene usted titulo de bachiller? ")

if respuesta == "Sí":
    print("Usted se puede matricular en el curso")
elif respuesta == "No":
    prueba = input("¿Hizo usted la prueba de acceso?")
    if prueba == "Sí":
        print("Usted se puede matricular en el curso")
    elif prueba == "No":
        print("Lo sentimos pero usted no es apto para el curso, intentelo de nuevo en un futuro")