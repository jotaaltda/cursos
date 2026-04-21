while True:
    print('Digite a opção desejada!')
    print('1. Calcular!')
    print('2. Sair!')

    opcao = int(input(''))

    if opcao == 1:
        while True:
            numero_1 = float(input('Digite o primeiro número: '))
            operador = input('Digite a operação desejada: ')
            numero_2 = float(input('Digite o segundo número: '))

            if operador == "+":
                print(numero_1 + numero_2)
                print('[R]eset / [V]oltar para o menu: ')
            elif operador == "-":
                print(numero_1 - numero_2)
                print('[R]eset / [V]oltar para o menu: ')
            elif operador == "*":
                print(numero_1 * numero_2)
                print('[R]eset / [V]oltar para o menu: ')
            elif operador == "/":
                print(numero_1 / numero_2)
                print('[R]eset / [V]oltar para o menu: ')
            
    if opcao == 2:
        print('Volte sempre que desejar calcular algo novo!')
        break