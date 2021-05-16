def run():

    while True:

        lower_limit = int(input("Ingresa un número entero que será tu límite inferior: "))
        upper_limit = int(input("Ingresa un número entero que será tu límite superior "))
        comparation = int(input("Ingresa un número entero para validar si está en el rango: "))
        print(str(comparation))

        if lower_limit < comparation and upper_limit > comparation:
            break

if __name__ == "__main__":
    run()