'''Integrantes da turma:
Pedro Henrique Serrato de Castro
Thiago Vinícius Pereira Borges
Eduardo de Abreu Neves
Franklin Jerônimo Belasque Bauch Vieira
Lucas Gabriel Nunes Geremias'''

import random

print('-=-' * 10)
print('Jogo de Cálculos Matematicos ')
print('-=-' * 10)
print('Você terá que responder 4 pergunta sem errar nenhuma se não terá que refazer novamente, BOA SORTE!')
start = input('\nVamos começar? (Sim/Não): ').upper()  # Lendo Sim ou Não e colocando em maiúculo

if start == 'SIM' or start == 'S':  # Se digitar Sim ou S iniciar o jogo
    print('Carregando...\n')

    cont = 0
    bool = True
    certo = '\nParabéns você acertou! Agora próxima pergunta.\n'
    errado = '\nVocê errou! Tente na próxima, iremos reniciar o Jogo de Cálculos Matematicos.\n'

    while bool == True:  # Início da repetição WHILE
        cont += 1  # Contador do número de tentativas

        # Variáveis de randomização
        a1 = random.randint(1, 1000)
        a2 = random.randint(1, 1000)
        a3 = a1 + a2

        s1 = random.randint(1, 1000)
        s2 = random.randint(1, 1000)
        s3 = s1 - s2

        m1 = random.randint(1, 1000)
        m2 = random.randint(1, 500)
        m3 = m1 * m2

        d1 = random.randint(100, 1000)
        d2 = random.randint(1, 50)
        d3 = d1 / d2
        d3 = int(d3)  # Comando feito para manter o resultado da divisão sem casas depois da vírgula

        resultado1 = int(input("Quanto é %d + %d\nResposta: " % (a1, a2)))
        if resultado1 == a3:
            print(certo)
        else:
            print(errado)
            continue  # retornará ao topo do loop

        resultado2 = int(input("Quanto é %d - %d\nResposta: " % (s1, s2)))
        if resultado2 == s3:
            print(certo)
        else:
            print(errado)
            continue  # retornará ao topo do loop

        resultado3 = int(input("Quanto é %d * %d\nResposta: " % (m1, m2)))
        if resultado3 == m3:
            print(certo)
        else:
            print(errado)
            continue  # retornará ao topo do loop

        resultado4 = int(input("Quanto é %d / %d\nResposta: " % (d1, d2)))
        if resultado4 == d3:
            print('Parabéns você acertou.\n')
            bool = False  # Sair da estrutura de repetição do WHILE
        else:
            print(errado)
            continue  # retornará ao topo do loop
    print('Parabéns você terminou o Jogo de Cálculos Matematicos, tendo %d tentativas.' % (cont))

elif start == 'NÃO' or start == 'N':  # Se digitar Não ou N o jogo não inicia
    print('\nVocê desistiu do Jogo de Cálculos Matematicos!')
    quit()  # Encerrar a execução

else:  # Se digitar uma palavra diferente o jogo não reconhece
    print('\nResposta inválida!')
    quit()  # Encerrar a execução
