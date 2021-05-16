def run():
    figure = input("Ingresa el número de la figura a la que deseas calcularle su volumen: \n 1. Cilindro \n 2. Cubo \n 3. Cono \n")

    if figure == "1":
        radius = float(input("Ingresa la medida del radio de la base(Recuerda: El radio mide la mitad del diámetro): "))
        height = float(input("Ingresa la altura del cilindro: "))
        volume = round(((3.141592653589793238462643383 * (radius**2))* height),2)
        print("El área del cilindro es " + str(volume))
    elif figure == "2":
        side = float(input("Ingresa el medida de uno de los lados del cubo: "))
        volume = round((side**3),2)
        print("El área del cubo es " + str(volume))
    elif figure == "3":
        radius = float(input("Ingresa la medida del radio de la base(Recuerda: El radio mide la mitad del diámetro): "))
        height = float(input("Ingresa la altura del cono: "))
        volume = round(((3.141592653589793238462643383 * (radius**2))*((1/3)* height)),2)
        print("El área del cono es " + str(volume))
    else: 
        print("Ingresa una opción correcta")

if __name__ == "__main__":
    run()