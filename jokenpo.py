
import os
jogador1 = ''
jogador2 = ''

pedra =1
papel =2
tesoura =3

saida = ''


while saida != 'sair': 
    print('alterando')
     
    print ("       __    ______    __  ___  _______  __   __   ______     ______   \n")
    print ("      |  |  /  __  \\  |  |/  / |   ____||  \\ |  | |   _  \\   /  __  \\  \n")
    print ("      |  | |  |  |  | |  '  /  |  |__   |   \\|  | |  |_)  | |  |  |  | \n")
    print (".--.  |  | |  |  |  | |    <   |   __|  |  . `  | |   ___/  |  |  |  | \n")
    print ("|  `--'  | |  `--'  | |  .  \\  |  |____ |  |\\   | |  |      |  `--'  | \n")
    print (" \\______/   \\______/  |__|\\__\\ |_______||__| \\__| | _|       \\______/  \n")
    
    jogador1 = int(input ('pedra = 1 \npapel = 2 \ntesoura = 3 \nDigite um número correspondente: ' ))
    jogador2 = int(input ('Digite outro número correspondente: ' ))

    if jogador1 == jogador2:
        print('EMPATE')
    elif jogador1 == 1 and jogador2 == 3:
        print('jogador 1 ganhou!')
    elif jogador1==3 and jogador2==2:
        print('jogador 1 ganhou!')
    elif jogador1 == 2 and jogador2 == 1:
        print('jojgador 1 ganhou!')
    else:
        print('jogador 2 ganhou!')

    saida = input('Quer sair? (digite sair)')
    os.system('cls')
    continue 
    
