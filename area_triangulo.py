import math

def run():

    base = float(input("Ingresa la medida de la base del triángulo en cm: "))
    height = float(input("Ingresa la medida de la altura del triángulo en cm: "))
    side_a = float(input("Ingresa la medida de un lado del triángulo (diferente a la base): "))
    side_b = float(input("Ingresa la medida del último lado del triángulo: "))

    #Calculo del área
    triangle_area = round(((base * height)/2),2)

    if base == side_b == side_a:
        triangle = "Equilátero"
    elif base==side_a or base==side_b:
        triangle = "Isósceles"
    else:
        triangle = "Escaleno"

    return print("El área del triángulo es {} y es un triángulo {}".format(triangle_area,triangle))

if __name__ == "__main__":
    run()
