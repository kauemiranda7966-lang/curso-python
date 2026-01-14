print('gerador de PA')
print('-=-'*10)
primeiro=int(input('digite o primeiro termo: '))
razao=int(input('razao: '))
termo=primeiro
cont = 1
while cont <=10:
    print('{}>'.format(termo))
    termo+=razao
    cont+=1 