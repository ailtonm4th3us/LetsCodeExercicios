print('Bem vindo ao supermercado, produtos pagos a vista recebem 15% de desconto')

valor1 = int(input('Qual o valor do seu produto?: '))
passagem = str(input('debito ou credito?: '))


if passagem == 'credito':
    print(f'O valor do seu produto é: {valor1}, com o desconto, o valor ficará: {valor1 - (valor1 * 0.15)}')
elif passagem == 'debito':
    print(f'O total ficará: {valor1}')
else:
    print('Não fazemos fiado, senhor!!')