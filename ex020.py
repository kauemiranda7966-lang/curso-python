sex=str(input('digite seu sexo {M/f}'))
print(sex)
while sex not in 'MmFf':
    sex=str(input('dados invalidos.'))
print('sexo {} registrado com sucesso'.format(sex))