#funcoes 
def area (l,c):
    a = l * c 
    print(f'a area de um terreno {l} x {c} é de {a} m2.')


print('controle de terreno')
print('-'*20)
l = float (input('LARGURA (m):'))
c = float (input('COMPRIMENTO (m):'))
area (l,c)