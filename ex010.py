larg=float(input("largura da parede:"))
alt=float(input("altura da parede"))
area= larg * alt
print("sua parede tem a dimensao de {}X{} e sua area é de {}".format(larg, alt, area))
tinta= area / 2 
print('para pintar essa parede voce vai precisar de {}L de tinta'.format(tinta))