from random import randint
computador=randint(0,10)
print('-=-'*20)
print('tente adivinhar um numero entre 0 e 5')
print('-=-'*20)
acertou= False
tent=0
while not acertou:
    jogador=int(input('qual seu palpite?'))
    tent+=1
    if jogador == computador:
        acertou = True
    else:
        print ('voce errou!! \ntente novamente:' )
print ('acertou com {} tentativas'.format(tent))