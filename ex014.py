vel=float(input('qual a velocidade do carro?'))

multa=(vel-80)*7

if vel > 80:
    print('voce execedeu o limite de 80Km/h! voce foi multado em R${}'.format(multa))
else:
    print('velocidade adequada, dirija com cuidado')

    # aula 29 curso em video python
