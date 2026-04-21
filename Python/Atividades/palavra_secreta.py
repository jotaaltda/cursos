import os

palavra = 'Casa'.upper()
letras_acertadas = ''

tentativas = 0

while True:

    tentativas += 1
    verificacao = 0

    palpite = input('Digite uma letra: ').upper()

    if len(palpite) > 1:
        print('Digite apenas uma letra!\n')
        continue

    if palpite in letras_acertadas:
        print('Você já tentou essa letra!\n')
        continue

    print('Palavra: ', end='')

    for letra in palavra:

        if letra == palpite:
            letras_acertadas += palpite
            print(letra, end=' ')
        elif letra in letras_acertadas:
            print(letra, end=' ')
        else:
            print('*', end=' ')
    
    print('\n')

    for letra in palavra:

        if letra in letras_acertadas:
            verificacao += 1

    if verificacao == len(palavra):
            os.system('cls')
            letras_acertadas = ''
            print('Boa! Você acertou a palavra!\n')
            print(f'Número de tentativas: {tentativas}\n')
            opcao = input('Deseja jogar novamente? [S]im [N]ão: ').lower()
            print()

            if opcao == 's':
                os.system('cls')
                tentativas = 0
                continue
            elif opcao == 'n':
                os.system('cls')
                break
            else:
                continue

print('Jogo encerrado!')