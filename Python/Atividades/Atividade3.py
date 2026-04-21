numero = input('Digite um número inteiro: ')

if '.' in numero:
    print('Isso não é um número inteiro!')
else:
    numeroint = int(numero)

    if (numeroint % 2) == 0:
        print('Esse número é PAR!')
    else:
        print('Esse número é ÍMPAR!')

# ===========================================================================================================

hora = input('Informe as horas: ')

soashoras = int(hora[0:2])

if soashoras >= 0 and soashoras <= 11:
    print("Tenha um bom dia!")
elif soashoras >= 12 and soashoras <= 17:
    print("Tenha um boa tarde!")
elif soashoras >= 18 and soashoras <= 23:
    print("Tenha um boa noite!")

# ===========================================================================================================

nome = input('Informe o seu primeiro nome: ')

totalletras = len(nome)

if totalletras <= 4:
    print('Seu nome é curto! :(')
elif totalletras >= 5 and totalletras <= 6:
    print('Seu nome é normal! :D')
elif totalletras > 6:
    print('Seu nome é muito grande! :()')