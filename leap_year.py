def leap_year():
    year=int(input("Ingrese un año:"))
    if (year%100==0 and year %400==0):
        print("El año ingresado es bisiesto")
    elif (year%4==0 and year%100!=0):
        print("El año no es bisiesto")
    else:
        print("El año ingresado no es bisiesto")
