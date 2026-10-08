import random

numero_secreto = random.randint(1, 20)

print('Pense em um número de 1 á 20. Tente acertar em 20 tentativas')

for tentativa in range(1, 6):
    palpite = int(input('Seu palpite'))

    if palpite < numero_secreto:
        print(f'Muito baixo! Tente um número maior')
    elif palpite < numero_secreto:
        print(f'Muito alto! Tente um número menor')
    else print(f'Acertou em {tentativa} tentativas!')
else:
    print(f'Acabaram as tentativas! O número secreto era: {numero_secreto}!')