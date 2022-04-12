from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print('=-'*20)
print('PEDRA PAPEL E TESOURA')
print('=-'*20)

nome = str(input("Vamos jogar? qual o seu nome: "))
sleep(1)
print ('''SUA opções: "
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input("Qual é a sua jogada? "))

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('=-'*20)
print(f"O computador escolheu {itens[computador]}")
print(f"O {nome} escolheu {itens[jogador]}")
print('=-'*20)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print(f"{nome} VENCEU")
    elif jogador == 2:
        print("O COMPUTADOR VENDEU")
    else:
        print("COMANDO INVÁLIDO")
elif computador == 1:
    if jogador == 0:
        print("O COMPUTADOR VENDEU")
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print(f"{nome} VENCEU")

elif computador == 2:
      if jogador == 0:
          print("O COMPUTADOR VENCEU")
      elif jogador == 1:
          print("O COMPUTADOR VENCEU")
      elif jogador == 2:
          print('EMPATE')

else:
      print("COMANDO INVÁLIDO")