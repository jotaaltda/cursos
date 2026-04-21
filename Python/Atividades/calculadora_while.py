while True:
    print('Digite a opção desejada!')
    print('1. Calcular!')
    print('2. Sair!\n')

    opcao = int(input(''))
    print()

    if opcao == 1:
        while True:
            numero_1 = input('Digite o primeiro número ([S]air): ')

            if numero_1 == 'S' or numero_1 == 's':
                print()
                break
            else:
                numero_1 = float(numero_1)

            operador = input('Digite a operação desejada: ')
            numero_2 = float(input('Digite o segundo número: '))

            if operador == "+":
                resultado = numero_1 + numero_2
                print(resultado, '\n')
            elif operador == "-":
                resultado = numero_1 - numero_2
                print(resultado, '\n')
            elif operador == "*":
                resultado = numero_1 * numero_2
                print(resultado, '\n')
            elif operador == "/":
                resultado = numero_1 / numero_2
                print(resultado, '\n')
            
    if opcao == 2:
        print('Volte sempre que desejar calcular algo novo!')
        break