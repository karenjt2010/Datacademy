def run():

    count_player1 = 0
    count_player2 = 0

    while count_player1 < 2 and count_player2 < 2:
        player1 = input("Haz tu selección Jugador 1: \n Piedra: 1 \n Papel: 2 \n Tijera: 3 \n")
        player2 = input("Haz tu selección Jugador 2: \n Piedra: 1 \n Papel: 2 \n Tijera: 3 \n")

        if player1 == "1" and player2 == "3" or player1 == "2" and player2 == "1" or player1 == "3" and player2 == "2":
            print("Esta ronda es para el Jugador 1")
            count_player1 += 1
        elif player1 == player2:
            print("Esta ronda es empate")
        else:
            print("Esta ronda es para el Jugador 2")
            count_player2 += 1
    
    if count_player1 == 2:
        print("El ganador de este juego es el Jugador 1")
    else:
        print("El ganador de este juego es el Jugador 2")
        
if __name__ == "__main__":
    run()