'''Integrantes da turma:
Pedro Henrique Serrato de Castro
Thiago Vinícius Pereira Borges
Eduardo de Abreu Neves
Franklin Jerônimo Belasque Bauch Vieira
Lucas Gabriel Nunes Geremias'''

from random import randint
from time import sleep

print('-=-' * 13)
print('Jogo Jokenpô (Pedra, Papel e Tesoura)')
print('-=-' * 13)
start = int(input('\nExiste dois modos de jogo que são: \n1 para humano-vs-humano \n2 para humano-vs-computador \nDigite qual modo gostaria de jogar de jogo: '))
#Modo de joga 1
if start == 1:
  cont_1 = 0
  cont_2 = 0
  opcao1 = '\n%s Suas opções: \n[1] Pedra \n[2] Papel \n[3] Tesoura \n[0] Sair \nQual opção você vai escolher? '
  opcao2 = '\n%s Suas opções: \n[1] Pedra \n[2] Papel \n[3] Tesoura \n[0] Sair \nQual opção você vai escolher? '
  nome1 = input('\nDigite seu nome para jogar como jogador 1: ')
  nome2 = input('Digite seu nome para jogar como jogador 2: ')
  jogador1 = int(input(opcao1 % (nome1)))
  jogador2 = int(input(opcao2 % (nome2)))
  while jogador1 != 0 and jogador2 != 0:
    if jogador1 <= 3 and jogador2 <= 3:
      sleep(0.5)
      print('\nJo')
      sleep(0.5)
      print('ken')
      sleep(0.5)
      print('pô')
      #PEDRA empata
      if jogador1 == 1 and jogador2 == 1:
        print('\nEMPATE, %s JOGOU PEDRA E %s TAMBÉM' % (nome1, nome2))
      #PAPEL empate
      elif jogador1 == 2 and jogador2 == 2:
        print('\nEMPATE, %s JOGOU PAPEL E %s TAMBÉM' % (nome1, nome2))
      #TESOURA empata
      elif jogador1 == 3 and jogador2 == 3:
        print('\nEMPATE, %s JOGOU TESOURA E %s TAMBÉM' % (nome1, nome2))
      #Pedra e Papel
      elif (jogador1 == 1 and jogador2 == 2) or (jogador1 == 2 and jogador2 == 1):
        if jogador1 == 1:
          cont_2 += 1
          print('\n%s GANHOU! %s JOGOU PEDRA E %s JOGOU PAPEL' % (nome2, nome1, nome2))
        elif jogador1 == 2:
          cont_1 += 1
          print('\n%s GANHOU! %s JOGOU PAPEL E %s JOGOU PEDRA' % (nome1, nome1, nome2))
      #Pedra e Tesoura
      elif (jogador1 == 1 and jogador2 == 3) or (jogador1 == 3 and jogador2 == 1):
        if jogador1 == 1:
          cont_1 += 1
          print('\n%s GANHOU! %s JOGOU PEDRA E %s JOGOU TESOURA' % (nome1, nome1, nome2))
        elif jogador1 == 3:
          cont_2 += 1
          print('\n%s GANHOU! %s JOGOU TESOURA E %s JOGOU PEDRA' % (nome2, nome1, nome2))
      #PAPEL e Tesoura
      elif (jogador1 == 2 and jogador2 == 3) or (jogador1 == 3 and jogador2 == 2):
        if jogador1 == 2:
          cont_2 += 1
          print('\n%s GANHOU! %s JOGOU PAPEL E %s JOGOU TESOURA' % (nome2, nome1, nome2))
        elif jogador1 == 3:
          cont_1 += 1
          print('\n%s GANHOU! %s JOGOU TESOURA E %s JOGOU PAPEL' % (nome1, nome1, nome2))
      print('PLACAR ESTÁ \n%d PARA %s \n%d PARA %s' % (cont_1, nome1, cont_2, nome2))
      jogador1 = int(input(opcao1 % (nome1)))
      jogador2 = int(input(opcao2 % (nome2)))
    else:
      print('\nNúmero inválido')
      jogador1 = int(input(opcao1 % (nome1)))
      jogador2 = int(input(opcao2 % (nome2)))
      continue
  if cont_1 > cont_2:
    print('\nFIM DE JOGO %s VENCEU COM: \n%d PARA %s \n%d PARA %s' % (nome1, cont_1, nome1, cont_2, nome2))
  elif cont_1 == cont_2:
    print('\nFIM DE JOGO FOI UM EMPATE COM: \n%d PARA AMBOS' % (cont_1))
  elif cont_1 < cont_2:
    print('\nFIM DE JOGO %s VENCEU COM: \n%d PARA %s \n%d PARA %s' % (nome2, cont_2, nome2, cont_1, nome1))
#Modo de joga 2
elif start == 2:
  cont_jogador = 0
  cont_computador = 0
  opcao = '\nSuas opções: \n[1] Pedra \n[2] Papel \n[3] Tesoura \n[0] Sair \nQual opção você vai escolher? '
  jogador = int(input(opcao))
  while jogador != 0:
    if jogador <= 3:
      sleep(0.5)
      print('\nJo')
      sleep(0.5)
      print('ken')
      sleep(0.5)
      print('pô')
      computador = randint(1, 3)
      #Pedra empata
      if jogador == 1 and computador == 1:
        print('\nEMPATE, VOCÊ JOGOU PEDRA E O COMPUTADOR TAMBÉM')
      #PAPEL empata
      elif jogador == 2 and computador == 2:
        print('\nEMPATE, VOCÊ JOGOU PAPEL E O COMPUTADOR TAMBÉM')
      #TESOURA empata
      elif jogador == 3 and computador == 3:
        print('\nEMPATE, VOCÊ JOGOU TESOURA E O COMPUTADOR TAMBÉM')
      #Pedra e Papel
      elif (jogador == 1 and computador == 2) or (jogador == 2 and computador == 1):
        if jogador == 1:
          cont_computador += 1
          print('\nPERDEU, VOCÊ JOGOU PEDRA E O COMPUTADOR JOGOU PAPEL')
        elif jogador == 2:
          cont_jogador += 1
          print('\nGANHOU, VOCÊ JOGOU PAPEL E O COMPUTADOR JOGOU PEDRA')
      #Pedra e Tesoura
      elif (jogador == 1 and computador == 3) or (jogador == 3 and computador == 1):
        if jogador == 1:
          cont_jogador += 1
          print('\nGANHOU, VOCÊ JOGOU PEDRA E O COMPUTADOR JOGOU TESOURA')
        elif jogador == 3:
          cont_computador += 1
          print('\nPERDEU, VOCÊ JOGOU TESOURA E O COMPUTADOR JOGOU PEDRA')
      #PAPEL e Tesoura
      elif (jogador == 2 and computador == 3) or (jogador == 3 and computador == 2):
        if jogador == 2:
          cont_computador += 1
          print('\nPERDEU, VOCÊ JOGOU PAPEL E O COMPUTADOR JOGOU TESOURA')
        elif jogador == 3:
          cont_jogador += 1
          print('\nGANHOU, VOCÊ JOGOU TESOURA E O COMPUTADOR JOGOU PAPEL')
      print('PLACAR ESTÁ \n%d PRA VOCÊ \n%d PRO COMPUTADOR' % (cont_jogador, cont_computador))
      jogador = int(input(opcao))
    else:
      print('\nNúmero inválido')
      jogador = int(input(opcao))
      continue
  if cont_jogador > cont_computador:
    print('\nFIM DE JOGO VOCÊ VENCEU COM: \n%d PRA VOCÊ \n%d PRO COMPUTADOR' % (cont_jogador, cont_computador))
  elif cont_jogador == cont_computador:
    print('\nFIM DE JOGO FOI UM EMPATE COM: \n%d PARA AMBOS' % (cont_jogador))
  elif cont_jogador < cont_computador:
    print('\nFIM DE JOGO VOCÊ PERDEU COM: \n%d PRA VOCÊ \n%d PRO COMPUTADOR' % (cont_jogador, cont_computador))
