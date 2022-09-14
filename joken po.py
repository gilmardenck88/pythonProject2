from random import randint
from time import sleep
print('SEJA BEM VINDO(A)(E) AO JOKENPO ')
contjog2 = 0
contjog1 = 0




op = str(input('Digite [11] se voce deseja jogar com um colega\n'
           'Digite [12]  se voce deseja jogar com o computador\n'
           'Digite [13] se voce deseja assitir um jogo computador X computador\nQual sua opção: '))
while op != '11' and op != '12' and op != '13':
    print('Digite um valor valido: ')
    op = str(input('Digite [11] se voce deseja jogar com um colega\n'
                   'Digite [12]  se voce deseja jogar com o computador\n'
                   'Digite [13] se voce deseja assitir um jogo computador X computador\nQual sua opção: '))



print('para esocolher pedra  🤛 digite [1]\n'
      'para esocolher papel ✋ digite [2]\n'
      'para esocolher tesoura ✌ digite [3]')

computador1 = 0
computador = randint(1, 3)
nome1 = str(input('Digite seu nome Jogador 1: ')).upper()
nome2 = str(input('Digite seu nome Jogador 2: ')).upper()


while op == '11':


    jogador1 = int(input(f'Digite sua jogada {nome1}: '))
    while jogador1 != 1 and jogador1 != 2 and jogador1 != 3:
        print('Opçao inválida. Digite outra opçao: ')
        jogador1 = int(input(f'Digite sua jogoda {nome1}: '))
    jogador2 = int(input(f'Digite sua jogada {nome2}: '))
    while jogador2 != 1 and jogador2 != 2 and jogador2 != 3:
        print('Opçao inválida. Digite outra opçao: ')
        jogador2 = int(input(f'Digite sua jogada {nome2}: '))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    if jogador1 == 1 and jogador2 == 2:

        contjog2 += 1
        contjog1 += 0
        print(f'{nome1} jogou pedra 🤛  e {nome2} jogou papel ✋, {nome2} ganhou')
    elif jogador1 == 1 and jogador2 == 1:

        contjog2 += 0
        contjog1 += 0
        print(f'{nome1} jogou pedra 🤛  e {nome2} jogou pedra 🤛 , Empate')
    elif jogador1 == 1 and jogador2 == 3:

        contjog2 += 0
        contjog1 += 1
        print(f'{nome1} jogou pedra 🤛 e {nome2} jogou tesoura ✌, {nome1} ganhou')
    elif jogador1 == 2 and jogador2 == 1:

        contjog2 += 0
        contjog1 += 1
        print(f'{nome1} jogou Papel ✋ e {nome2} jogou pedra 🤛 , {nome1} ganhou')
    elif jogador1 == 2 and jogador2 == 2:

        contjog2 += 0
        contjog1 += 0
        print(f'{nome1} jogou Papel ✋ e {nome2} jogou papel ✋, Empate')
    elif jogador1 == 2 and jogador2 == 3:

        contjog2 += 1
        contjog1 += 0
        print(f'{nome1} jogou Papel ✋ e {nome2} jogou tesoura ✌, {nome2} ganhou')
    elif jogador1 == 3 and jogador2 == 1:

        contjog2 += 1
        contjog1 += 0
        print(f'{nome1} jogou tesoura ✌ e {nome2} jogou pedra 🤛 , {nome2} ganhou')
    elif jogador1 == 3 and jogador2 == 2:

        contjog2 += 0
        contjog1 += 1
        print(f'{nome1} jogou tesoura ✌ e {nome2} jogou papel ✋, {nome1} ganhou')
    elif jogador1 == 3 and jogador2 == 3:

        contjog2 += 0
        contjog1 += 0
        print(f'{nome1} jogou tesoura ✌ e {nome2} jogou tesoura ✌, {nome2}  empate')
    print(f'Placar atual: {nome1} -> {contjog1} e {nome2} -> {contjog2}')
    seguir = ' '
    while seguir not in 'S/N':
        seguir = str(input('Voce deseja continuar jogando:[S/N]')).strip().upper()[0]
    if seguir == 'N':
        break





while op == '12':

    jogador1 = int(input(f'Digite sua jogoda {nome1}: '))
    while jogador1 != 1 and jogador1 != 2 and jogador1 != 3:
        print('Opçao inválida. Digite outra opçao: ')
        jogador1 = int(input(f'Digite sua jogoda {nome1}: '))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!!')
    computador = randint(1, 3)
    if jogador1 == 1 and computador == 2:

        contjog2 += 1
        contjog1 = 0
        print(f'{nome1} jogou pedra 🤛  e {nome2} jogou papel ✋, {nome2} ganhou')
    elif jogador1 == 1 and computador == 1:

        contjog2 += 0
        contjog1 += 0
        print(f'{nome1} jogou pedra 🤛  e {nome2} jogou pedra 🤛 , Empate')
    elif jogador1 == 1 and computador == 3:

        contjog2 += 0
        contjog1 += 1
        print(f'{nome1} jogou pedra 🤛  e {nome2} jogou tesoura ✌, {nome1} ganhou')
    elif jogador1 == 2 and computador == 1:

        contjog2 += 0
        contjog1 += 1
        print(f'{nome1} jogou Papel ✋ e {nome2} jogou pedra 🤛 , {nome1} ganhou')
    elif jogador1 == 2 and computador == 2:

        contjog2 += 0
        contjog1 += 0
        print(f'{nome1} jogou Papel ✋ e {nome2} jogou papel ✋, Empate')
    elif jogador1 == 2 and computador == 3:

        contjog2 += 1
        contjog1 += 0
        print(f'{nome1} jogou Papel ✋ e {nome2} jogou tesoura ✌, {nome2} ganhou')
    elif jogador1 == 3 and computador == 1:

        contjog2 += 1
        contjog1 += 0
        print(f'{nome1} jogou tesoura ✌ e {nome2} jogou pedra 🤛 , {nome2} ganhou')
    elif jogador1 == 3 and computador == 2:

        contjog2 += 0
        contjog1 += 1
        print(f'{nome1} jogou tesoura ✌ e {nome2} jogou papel ✋, {nome1} ganhou')
    elif jogador1 == 3 and computador == 3:

        contjog2 += 0
        contjog1 += 0
        print(f'{nome1} jogou tesoura ✌ e {nome2} jogou tesoura ✌, {nome2}  empate')
    print(f'Placar atual: {nome1} -> {contjog1} e {nome2}  -> {contjog2}')


    seguir = ' '
    while seguir not in 'S/N':
        seguir = str(input('Voce deseja continuar jogando:[S/N]')).strip().upper()[0]
    if seguir == 'N':
        break
while op == '13':
    computador1 = randint(1, 3)
    computador = randint(1, 3)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')



    if computador1 == 1 and computador == 2:
        nome1 = computador1
        nome2 = computador
        contjog2 += 1
        contjog1 += 0
        print(f'{nome1}  jogou pedra 🤛  e {nome2} jogou papel ✋, {nome2} ganhou')
    elif computador1 == 1 and computador == 1:

        contjog2 += 0
        contjog1 += 0
        print(f'{nome1} jogou pedra 🤛  e {nome2} jogou pedra 🤛 , Empate')
    elif computador1 == 1 and computador == 3:

        contjog2 += 0
        contjog1 += 1
        print(f'{nome1} jogou pedra 🤛  e {nome2} jogou tesoura ✌, {nome1} ganhou')
    elif computador1 == 2 and computador == 1:

        contjog2 += 0
        contjog1 += 1
        print(f'{nome1} jogou Papel ✋ e {nome2} jogou pedra 🤛 , {nome1} ganhou')
    elif computador1== 2 and computador == 2:

        contjog2 += 0
        contjog1 += 0
        print(f'{nome1} jogou Papel ✋ e {nome2} jogou papel ✋, Empate')
    elif computador1 == 2 and computador == 3:

        contjog2 += 1
        contjog1 += 0
        print(f'{nome1} jogou Papel ✋ e {nome2} jogou tesoura ✌, {nome2} ganhou')
    elif computador1 == 3 and computador == 1:
        contjog2 += 1
        contjog1 += 0
        print(f'{nome1} jogou tesoura e {nome2} jogou pedra 🤛 , {nome2} ganhou')
    elif computador1 == 3 and computador == 2:
        contjog2 += 0
        contjog1 += 1
        print(f'{nome1} jogou tesoura ✌ e {nome2} jogou papel ✋, {nome1} ganhou')
    elif computador1 == 3 and computador == 3:
        contjog2 += 0
        contjog1 += 0
        print(f'{nome1} jogou tesoura ✌ e {nome2} jogou tesoura ✌,  EMPATE!!!!!')
    print(f'Placar atual: {nome1} -> {contjog1} e {nome2} -> {contjog2}')


    seguir = ' '
    while seguir not in 'S/N':
        seguir = str(input('Voce deseja continuar jogando:[S/N]')).strip().upper()[0]
    if seguir == 'N':
        break
print('===================================FIM DE JOGO==============================================')
sleep(1)
print(f'**************O PLACAR FINAL É  {nome1}: {contjog1}  e {nome2}: {contjog2}**************')
print('============================================================================================')
print(' Muito obrigado!!! Espero que tenha gostado do   jogo!!!')
print('****CRÉDITOS****')
print('**Eduardo Moura\n'
      f'**Gilmar Denck Junior\n'
      f'**Vittorio Caprioli\n'
      f'**AndrÉ Akim')





