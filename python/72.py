numeros = ('zero', 'um', 'dois', 'tres', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'catorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')

while True:
    resposta = int(input('Digite um numero de 0 a 20: '))
    if 0 <= resposta <= 20:
        print(f'Voce digitou o numero {numeros[resposta]}')
        quer_sair = not input('Voce quer rodar o programa novamente? ') \
          .lower() \
          .startswith('s')
        if quer_sair:
          break
    else:
        print('Tente novamente. ', end="")

