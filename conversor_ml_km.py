from os import initgroups


def run():
    option = input("Seleccione la medida de longitud a la que desea convertir su valor: \n Kilómetros: 1 \n Millas: 2 \n")

    if option == "1":
        value = float(input("Ingrese la cantidad de millas que desea convertir a kilómetros: "))
        distance = round((value * 1.609344),2)
        print(str(value) + " millas equivalen a " + str(distance) + " kilometros")
    elif option == "2":
        value = float(input("Ingrese la cantidad de kilómetros que desea convertir a millas: "))
        distance = round((value / 1.609344),2)
        print(str(value) + " kilometros equivalen a " + str(distance) + " millas")

if __name__ == "__main__":
    run()