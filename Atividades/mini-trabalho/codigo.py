''''
Autor do projeto: Wendel Spargoli Bernardo da Silva

Mini-trabalho da aula de Análise de Sistemas Orientado a Objetos do curso de Sistemas de Informação do UNI-RN

criação de um sistema de cadastro - Relação de jogos no estoque pessoal
'''
# Banco de dados dos jogos
Jogos = []

# Criação de Menu
def exibir_menu():
    print ("Bem vindo(a) à lista do seu repositório de jogos! O que você quer fazer hoje? \n 1 - Listar jogos \n 2 - Cadastrar jogos \n 0 - Sair");

#Listagem de jogos
def listar_tudo():
    if not Jogos:
        print("\n Não há jogos no momento!\n")
    else:
        print(f"\n Essa é a listagem de jogos atual:\n {Jogos}");
        

# Cadastro de novos jogos
def cadastro_novo():
    novo_jogo = input("Digite o nome do jogo a ser cadastrado: ");
    Jogos.append(novo_jogo);
    print("\n Novo jogo cadastrado com sucesso! \n")

# Menu principal
def principal():
    while True:
        exibir_menu();
        opcao = input("Escolha uma das opções informadas: ");
        if opcao == "1" or opcao == "01":
            listar_tudo();
        elif opcao == "2" or opcao == "02":
            cadastro_novo();
        elif opcao == "0" or opcao == "00":
            break;
        else:
            print ("\n Opção inválida. Escolha uma das opções sugerias!\n");
            return (exibir_menu());

principal()
