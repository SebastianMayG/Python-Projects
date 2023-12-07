import random

def jugar():
    usuario = input("Elige entre: 'r' for rock, 'p' for paper, 's' for scissors: ").lower
    computer = random.choice(['r', 'p' , 's'])

    if usuario == computer:
        print("usuario: ", usuario , "computadora: " ,computer)
        return"Empate"

    elif is_win(usuario,computer):
        print("usuario: ", usuario , "computadora: " ,computer)
        return "Ganaste"
    
    print("usuario: ", usuario , "computadora: " ,computer)
    return "Perdiste"

def is_win(usuario,computer):
    if (usuario == 'r' and computer =='s') or (usuario == 's' and computer == 'p') or (usuario == 'p' and computer == 'r'):
        return True
    return False
