import random
from os import system
from emoji import emojize

def boas_vindas():
    print('Bem vindo ao jogo de Pedra, Papel e Tesoura!!!')
    nome = input("Digite seu nome para uma melhor experiência: ")
    return nome

def jogo():
    jogador = boas_vindas()
    continua = 1

    while continua != 0:
        system('cls')
        opcoes = ['pedra' , 'papel' , 'tesoura']

        print(f'Olá, {jogador}!! Vamos Jogar!!')

        op_jogador = int(input("Escolha a opção que desja:\n[1] - Pedra\n[2] - Papel\n[3] - Tesoura\n"))
        op_computador = random.choice(opcoes)

        if op_jogador == 1 and op_computador == 'tesoura' or op_jogador == 2 and op_computador == 'pedra' or op_jogador == 3 and op_computador == 'tesoura':
            print(emojize(f'Parabéns, {jogador}!! Você venceu :winking_face_with_tongue:' , language='alias'))
        else:
            print(emojize('Você foi derrotado :disappointed_face:' , language='alias'))

        continua = int(input('Para sair - Digite 0\nPara continuar - Digite Qualquer outro número\n'))
    print(emojize("Obrigado por Jogar!! :thumbsup:" , language='alias'))
        



jogo()

