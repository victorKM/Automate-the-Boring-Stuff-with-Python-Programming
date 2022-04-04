import random 
randomnumber = random.randint(1,20)

print('Agora voce precisa adivinhar o numero de 1 a 20 em 7 tentativas!')

for i in range (1,8):
    print('Coloque o numero:')
    myNumber = int(input())

    if myNumber < randomnumber:
        print('Muito abaixo')
    elif myNumber > randomnumber:
        print('Muito acima')
    else:
        break

if (myNumber == randomnumber):
    print('Parabens voce acertou!')
else:
    print('Infelizmente você não conseguiu, era o numero' + str(randomnumber))