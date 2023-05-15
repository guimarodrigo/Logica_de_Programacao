
# Após passar na primeira fase de uma peneira de vôlei, os candidatos aprovados são separados em grupos diferentes, 
#de acordo com suas alturas, para serem testados para posições específicas. Faça um programa que, 
#dada a altura de um determinado candidato, diga para qual posição ele deverá fazer o teste.

# Caso o jogador tenha menos de 180cm, o programa deve imprimir REPROVADO
# Caso tenha entre 180cm e 185cm, o programa deve imprimir LÍBERO
# Caso tenha entre 186cm e 195cm, o programa deve imprimir PONTEIRO
# Caso tenha entre 196cm e 205cm, o programa deve imprimir OPOSTO
# Caso tenha mais de 205cm, o programa deve imprimir CENTRAL
import os
print ('***************************************************************')
print ('***************************************************************')

saida = ''

while saida != 'sair':

    altura_usuario = float(input('Digite sua altura: '))

    if altura_usuario < 1.80:
        print ('REPROVADO')
    elif 1.80 <= altura_usuario <=1.85:
        print ('LÍBERO')
    elif 1.86 <= altura_usuario <=1.95:
        print ('PONTEIRO')
    elif 1.96 <= altura_usuario <=2.05:
        print ('OPOSTO')
    else:
        print ('CENTRAL')

    saida = input('Você quer sair? (digite sair)')
    os.system('cls')
    continue 