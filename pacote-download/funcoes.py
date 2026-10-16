def lin():
    print('-'*50)


def valida_numero(msg):
    while True:
        valor = input(msg).strip()
        if valor.isdigit():
            return int(valor)
        lin()
        print('Inválido! Digite apenas a numeração.')
        lin()


def tipo_cafe(msg):
    while True:
        print('''- Tipo de café e Moagem -
(1) - Em grãos
(2) - Previamente moído''')
        tipo = valida_numero('Para que eu te diga a moagem ideal, me fala, qual o tipo do café?')
        lin()
        if tipo < 1 or tipo > 2:
            print('Número inválido. Escolha entre 1 e 2.')
            lin()
        elif tipo == 1:
            print(msg)
            lin()
            break
        else:
            print('''Café previamente moído costuma ter granulometria média. 
Para métodos mais sensíveis à moagem o resultado pode variar.
Como o café já vem moído, você não tem controle sobre a 
espessura da moagem. Isso pode deixar a extração menos 
precisa dependendo do método escolhido.
Além disso, café já moído perde frescor mais rápido.
Prefira usá-lo em até 2 semanas.''')
            lin()
            break


def dose_espresso():
    while True:
        print('''Doses:
(1) - Única
(2) - Dupla''')
        dose = valida_numero('Você vai preparar dose única ou dupla?')
        if dose < 1 or dose > 2:
            lin()
            print('Número inválido. Escolha entre 1 e 2.')
            lin()
            continue
        if dose == 1:
            lin()
            print('- Única -')
            print('Quantidade de pó: Utilizar entre 7 e 9 gramas de café moído.')
            print('Quantidade de bebida: de 25 a 30 ml. ')
            lin()
        else:
            lin()
            print('- Dupla -')
            print('Quantidade de pó: Utilizar entre 14 e 18 gramas de café moído.')
            print('Quantidade de bebida: de 50 a 60 ml. ')
            lin()
        print('''Para retornar, digite
(1) - Para voltar às doses
(2) - Para voltar ao menu inicial''')
        while True:
            continuar_dose = valida_numero('Para onde gostaria de voltar?')
            if continuar_dose < 1 or continuar_dose > 2:
                lin()
                print('Número inválido. Escolha entre 1 e 2.')
                lin()
                continue
            if continuar_dose == 1:
                lin()
                break
            else:
                lin()
                voltar = True
                return voltar

def calcula_proporcao(proporcao):
    print('''Observação importante para todos os métodos: 
Essas proporções são pontos de partida. O ideal é ajustar conforme o seu paladar,
o grão utilizado e o nível de torra. Cafés de torra mais clara geralmente pedem 
um pouco mais de água (ratio maior), enquanto torras mais escuras podem 
funcionar melhor com ratios menores. Use uma balança de precisão para garantir 
consistência nas suas extrações.''')
    lin()
    while True:
        print('- Proporção de água para pó de café -')
        ml = valida_numero('Quantos ml de bebida você gostaria?')
        cafe = ml/proporcao
        lin()
        print(f'Nesse método, para {ml}ml de água, serão necessários {cafe:.0f}g de café.')
        lin()
        print('''Retornar para:
(1) - Recalcular porção
(2) - Menu inicial''')
        while True:
            recalcular_retorno = valida_numero('Digite a opção desejada:')
            if recalcular_retorno < 1 or recalcular_retorno > 2:
                lin()
                print('Número inválido. Escolha entre 1 e 2.')
                lin()
                continue
            if recalcular_retorno == 1:
                lin()
                break
            else:
                lin()
                voltar = True
                return voltar