import math
def line():

    variable_a=float(input("Ingrese el coeficiente A: "))
    variable_b=float(input("Ingrese el coeficiente B: "))
    variable_x1=float(input("Ingrese el coeficiente X1: "))
    variable_x2=float(input("Ingrese el coeficiente X2: "))
    print(f"El coeficiente A de su ecuación de la recta es: {variable_a}")
    print(f"El coeficiente B de su ecuación de la recta es: {variable_b}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {variable_x1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {variable_x2}")
    print()
    print("Para la siguiente ecuación:")
    print(f"\tY = {variable_a}X + {variable_b}")
    variable_y1=(float(variable_a*variable_x1)+variable_b) 
    variable_y2=(float(variable_a*variable_x2)+variable_b)
    print()
    print("Dados los siguientes puntos:")
    print(f"\tP1 ({variable_x1}, {variable_y1})")
    print(f"\tP2 ({variable_x2}, {variable_y2})")
    print()
    P1=[variable_x1,variable_y1]
    P2=[variable_x2,variable_y2]
    variable_distance= math.dist(P1,P2)
    print(f"La distancia entre ellos es: {variable_distance}")
