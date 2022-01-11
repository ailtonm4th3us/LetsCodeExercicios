nome = str(input('Qual é seu nome?: '))
idade = int(input('Qual sua idade?: '))

if 12 <= idade <= 60:
    sexo = str(input('Qual é seu sexo?: '))
    if sexo == 'masculino' or sexo == 'feminino' or sexo == 'outro':
        salario = float(input('Qual é sua faixa salarial?: '))
        print(f'você tem idade, sexo e faixa salarial que precisamos')
    else:
        print('Você não cumpre os requisitos')
else:
    print('Você não cumpre os requisitos')


#if 12 <= idade <= 60 and salario >= 0 and sexo == 'masculino' or sexo == 'feminino' or sexo == 'outro':
#    print('Você está OK')
#else:
#    print('Você não está OK')
