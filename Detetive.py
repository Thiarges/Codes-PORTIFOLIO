print("João estáva comendo uma coxinha, porém foi ao banheiro e quando voltou, SUMIU A COXINHA. Começaram uma investigação para saber quem foi esfomeado ladrão")
print("Os suspeitos sao: belleoni, lukinha, Laura, Caua, Chico, Julia.")
P = "P = Belleboni estava na sala de aula no momento do roubo da coxinha"
Q = "Q = Thiago estava na sala de aula no momento do roubo"
R = "R = Laura estava na biblioteca no momento do assassinato"
J = "J = O Caua comeu a coxinha de Jesus com maionese"
T = "T = Chico comeu a coxinha de Jesus"
U = "U = Julia comeu a coxinha de Jesus"
W = "W = Comeram a coxinha de Jesus com ketchup"
vet = [P, Q, R, J, T, U ,W]
A = "A coxinha de jesus, foi comida na sala de aula"
B = "Belleboni ou Thiago estavam na sala de aula no momento do roubo"
C = "Se Laura estava na biblioteca no momento do roubo, então Caua comeu a coxinha de jesus no DCE"
D = "Se Belleboni estava na sala de aula no momento do rouba, então o Chico roubou jesus"
E = "Se Laura não estava na biblioteca no momento doroubo, então Belleboni não estava na sala de aula quando o roubo ocorreu"
F = "Se Thiago estava na sala de aula no momento do roubo, então Julia o roubou."
fun = [A, B, C, D, E, F]
print("-="*30)
print("Situaçoes:")
y = int(input("Qunatas dicas você quer receber de 1 a 6? "))
while y > 6 or y < 1:
    print("FAZ CERTO BOBÃO,", end=' ')
    y = int(input("Qunatas dicas você quer receber de 1 a 6? "))
for i in range(0, y):
        print(fun[i])
r = input("Você gostaria de ter mais dicas? [S/N] ").upper().strip()
while r not in 'SN':
    print("\033[1;31;40m FAZ CERTO BOBÃO,", end=' ')
    r = input('\033[mResponda com [S ou N], Agradecido: ').upper().strip()
if r == 'S':
    for i in range(y, len(fun)):
        print(fun[i])
        r = input("Você gostaria de ter mais dicas? [S/N] ").upper().strip()
        while r not in 'SN':
            print("\033[1;31;40m FAZ CERTO BOBÃO,", end=' ')
            r = input('\033[mResponda com [S ou N], Agradecido: ').upper().strip()
        if r == 'S':
            fun[i]
        else:
            r = 'g'
            if fun[i] == 6:
                break
    else:
        r = 'g'

v = 0
z = "Julia"
print("Sabendo desses fatos, utilize os argumentos transormando em proposições usando regras de inferencia, para descobrir quem foi o esfomeado ladrão.")
while v == 0:
    k = input("Entao, quem é o pilantra?").strip().title()
    if k == z:
        print(f'\033[1;32;40m {"Parabens Sherlock Sholmes"}')
        v = 1
    else:
        print("Tenta de novo bobão")
l = input("\033[1;36;40m Você quer saber a resolução? [S/N] ").strip().upper()
while l not in 'SN':
    print("\033[1;31;40m FAZ CERTO BOBÃO,", end=' ')
    l = input('\033[mResponda com [S ou N], Agradecido: ').upper().strip()
if l == 'S':
    print("\033[1;36;40m 1 - P V Q    hip")
    print("2 - R -> J   hip")
    print("3 - P -> T   hip")
    print("4 - ~R -> ~P hip")
    print("5 - Q -> U   hip")
    print("6 - ~J       hip")
    print("7 - ~R       MT 2,6")
    print("8 - ~P       MP 4,7")
    print("9 - Q        SD 1,8")
    print("10 - \033[1;32;40m Conclusão: U MP 5,9")
print("\033[1;35;40mMuito Obrigado por jogar :)")
