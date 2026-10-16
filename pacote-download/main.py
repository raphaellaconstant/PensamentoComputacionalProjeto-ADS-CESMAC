from funcoes import lin, valida_numero, tipo_cafe, dose_espresso, calcula_proporcao
from dados import metodos_coados, lista_menu
lin()
print(f'{"Bem vinda(o) ao":^50}')
print(f'{"CALCULANDO O CAFEZINHO!":^50}')
lin()
print('Vamos calcular a proporção ideal para o seu café!')
lin()
while True:
    print('MENU DE MÉTODOS:')
    for indice, item in enumerate(lista_menu):
        print(f'({indice + 1}) - {item}')
    lin()
    escolha = valida_numero('Escolha a numeração correspondente ao método de preparo:')
    lin()
    if escolha < 1 or escolha > 8:
        lin()
        print('Número inválido. Escolha entre 1 e 8.')
        lin()
        continue
    if escolha == 8:
        print('Encerrando...')
        break
    elif escolha == 1:
        while True:
            print('= Espresso =')
            tipo_cafe('''MOAGEM FINA é essencial no Espresso porque a água passa 
pelo pó em poucos segundos, sob pressão. Se a moagem for 
grossa, a água passa rápido demais e não extrai o sabor 
corretamente.''')
            voltar = dose_espresso()
            if voltar == True:
                break
    elif escolha == 2:
        print('= Cafeteira Italiana =')
        print('Quantidade de pó: Utilizar o café moído até que o compartimento de pó esteja preenchido totalmente.')
        print('Observação: É importante não compactar o pó de café.')
        print('Quantidade de bebida: Encha de água até chegar na altura da válvula. Não ultrapassar ela. ')
        lin()
        tipo_cafe('''MOAGEM MÉDIA-FINA, um pouco mais grossa 
que a do Espresso. Isso porque a pressão da Moka é mais baixa, 
então uma moagem muito fina pode entupir o filtro e deixar 
o café com sabor amargo.''')
    elif escolha in [3,4,5,6,7]:
        while True:
            metodo = metodos_coados[escolha - 3]
            print(f'= {metodo["nome"]} =')
            tipo_cafe(metodo['mensagem_moagem'])
            voltar = calcula_proporcao(metodo['proporcao'])
            if voltar == True:
                break