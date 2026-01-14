# CALCULADORA

valor1=int(input('digite um numero:'))
operadores=('+','-','*','/' )
print('[ +, - , * , / ]')
op=input('escolha um operador:')
valor2=int(input('escolha o segundo valor:'))
if op == '+':
    resultado = valor1 + valor2
elif op == '-':
    resultado = valor1 - valor2
elif op == '*':
    resultado = valor1 * valor2
elif op == '/':
    if valor2!=0:
        resultado = valor1 / valor2 
    else:
        resultado = 'erro! divisao por zero.'
else:
    resultado = 'operador invalido!:'

print('o resultado é {}'.format(resultado))














