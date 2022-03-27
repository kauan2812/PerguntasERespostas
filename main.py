perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto e 2 + 2? ',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto e 3 * 2? ',
        'respostas': {
            'a': '4',
            'b': '10',
            'c': '6',
        },
        'resposta_certa': 'c',
    },
}

respostas_certas = 0

# pk => pergunta keys // pv => pergunta values
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas:')

    # rk => respostas keys // rv => respostas values
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('Acertou.')
        respostas_certas += 1
    else:
        print('Errou.')

    print() # Pular uma linha entre as perguntas

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Voce acertou {respostas_certas} perguntas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%')