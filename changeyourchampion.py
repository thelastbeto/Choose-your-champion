import os

campeoes = [
                {'nome': 'Yorick', 'categoria': 'Toplane', 'ativo': False},
                {'nome': 'GankPlank', 'categoria': 'Toplane', 'ativo': False},
                {'nome': 'Graves', 'categoria': 'Jungle', 'ativo': False},
                {'nome': 'Malphite', 'categoria': 'Toplane', 'ativo': False}, 
                {'nome': 'Veigar', 'categoria': 'Midlane', 'ativo': False}, 
                {'nome': 'Fiora', 'categoria': 'Toplane', 'ativo': False},
                {'nome': 'Sett', 'categoria': 'Toplane', 'ativo': False},
                {'nome': 'Lucian', 'categoria': 'Botlane', 'ativo': False}, 
                {'nome': 'Nami', 'categoria': 'Botlane', 'ativo': False},
                {'nome': 'Vayne', 'categoria': 'Botlane', 'ativo': False}, 
                {'nome': 'Lux', 'categoria': 'Midlane', 'ativo': False}                           
            ]

categorias = ['Toplane', 'Jungle', 'Midlane', 'Botlane']
   

def exibir_nome_do_programa():
    print("Campeões da PoolLane\n")

def exibir_opcoes():
    print('1.Cadastrar Campeão');
    print('2.Listar Campeões Cadastrados');
    print('3.Ative o Campeão');
    print('4.Sair do aplicativo \n');
    
def main():
     exibir_nome_do_programa()
     exibir_opcoes()
     escolher_opcao()
    
def exibir_subtitulos(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu_principal():
    retorno = input('\nDeseja voltar ao menu principal? ').upper()
    if retorno == 'SIM':
        main()
    else:
        finalizar_app()

def opcao_invalida():
    print('Opção Inválida \n')
    
    
def cadastrar_novo_campeao():
    '''A função é responsável por cadastrar um novo campeão na Pool'''
    exibir_subtitulos('Cadastro de novos campeões')
    nome_do_campeao = input('Digite o nome do campeão que deseja cadastrar \n')

    
    # Verifica se o campeão já está cadastrado
    for campeao in campeoes:
        if campeao['nome'] == nome_do_campeao:
            print('O campeão já foi cadastrado anteriormente. Informe um novo campeão')
            main()
    # Se não encontrou, continua com o cadastro
    
    categoria = input(f'Digite o nome da lane que o campeão {nome_do_campeao} mais atua! \nLanes disponíveis: Toplane, Jungle, Midlane, Botlane \n')
        # Verifica se a categoria está mapeada
    if categoria not in categorias:
        print('A categoria não existe. Selecione uma válida: Toplane, Jungle, Botlane, Midlane')
        voltar_ao_menu_principal()
    
    dados_do_campeao = {'nome':nome_do_campeao, 
                            'categoria':categoria, 
                            'ativo':False}
    campeoes.append(dados_do_campeao)
    print(f'O Campeão {nome_do_campeao} foi cadastrado com sucesso')
    voltar_ao_menu_principal()

def listar_campeoes():
    exibir_subtitulos('Listando campeões cadastrados')
    
    print(f'{'Nome do campeão'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}')
    for campeao in campeoes:
        nome_campeao = campeao['nome']
        categoria = campeao['categoria']
        ativo = 'ativado' if campeao['ativo'] else 'desativado'
        print(f'{nome_campeao.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()
    
def ativar_campeao():
    exibir_subtitulos('Alternando estado do campeão')
    nome_campeao = input('Digite o nome do campeão que você deseja alternar o estado ')
    campeao_encontrado = False
    
    for campeao in campeoes:
        if nome_campeao == campeao['nome']:
            campeao_encontrado = True
            campeao['ativo'] = not campeao['ativo']
            mensagem = f'O Campeão {nome_campeao} foi ativado com sucesso!!' if campeao['ativo'] else f'O Campeão {nome_campeao} foi desativado com sucesso!!' #Funcao ternaria
            print(mensagem)
            
    if not campeao_encontrado:
        print(f'O Campeão {nome_campeao} não foi encontrado! Informe um outro campeão ou faça o cadastro do campeão desejado no primeiro menu!')
    voltar_ao_menu_principal()
    
def finalizar_app():
    exibir_subtitulos('Finalizando aplicação')

def escolher_opcao():

    try:
        # Armazenando a opção escolhida pelo usuário;
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'A opção escolhida é a {opcao_escolhida}')   
        match opcao_escolhida:  
            case 1:
                cadastrar_novo_campeao()
            case 2:
                listar_campeoes()
            case 3:
                ativar_campeao()
            case 4:
                finalizar_app()
            case _:
                print('Opção Inválida \n\n')
                escolher_opcao()
    except:
        opcao_invalida()

    
if __name__ == '__main__':
    main()
    
