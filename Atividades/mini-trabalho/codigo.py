''''
Autor do projeto: Wendel Spargoli Bernardo da Silva

Mini-trabalho da aula de Análise de Sistemas Orientado a Objetos do curso de Sistemas de Informação do UNI-RN

criação de um sistema de cadastro de jogos
'''
# Banco de dados dos jogos
Jogos = [
    {"nome":"Zelda Breath of the Wild","Tempo de jogo": 98, "Preço": 389.90}, 
    {"nome":"Cyberpunk 2077","Tempo de jogo": 63, "Preço": 339.99}, 
    {"nome":"Divinity II","Tempo de jogo": 101, "Preço": 184.96},
];

# Criação de Menu
def exibir_menu():
    print ("\nBem-vindo(a) à sua lista de jogos! O que você quer fazer hoje? \n 1 - Listar jogos \n 2 - Cadastrar jogos \n 3 - Buscar jogo \n 4 - Alterar jogo \n 5 - Remover jogo \n 0 - Sair");

#Listagem de jogos
def listar_tudo():
    if not Jogos:
        print("\n Não há jogos no momento!\n")
    else:
        for jogo in Jogos:
            print(f"{jogo['nome']:>10}{jogo['Tempo de jogo']:>10}{jogo['Preço']:>10}");
        
# Cadastro de novos jogos
def cadastro_novo():
    nome_jogo = input("\n Digite o nome do jogo a ser cadastrado: ").strip(); 
    tempo_jogo = input("\n Digite o tempo de jogo a ser cadastrado (apenas números): ").strip();
    preco_jogo = input("\n Digite o preço do jogo a ser cadastrado (apenas números): ").strip();

    Jogos.append({"nome": nome_jogo, "Tempo de jogo": int(tempo_jogo), "Preço": float(preco_jogo)});
    print("\n Novo jogo cadastrado com sucesso! \n")

# Buscador
def buscar_jogo():
    # Termo de busca com redutor de espaços finais e iniciais (.strip())
    termo_busca = input("\nDigite o nome do jogo que quer encontrar:").strip();
    for jogo in Jogos:
        # Compara ignorando maiúsculas e minúsculas (.lower())
        if jogo["nome"].lower() == termo_busca.lower():
            print(f"Encontrei o jogo: {jogo['nome']} / Tempo de jogo: {jogo['Tempo de jogo']} / Preço: {jogo['Preço']}");
        else:
             print("Jogo não encontrado. Por favor, digite o nome corretamente!");

    # Problema encontrado: o código procura e gera respostas em loop. Para melhorar, quero que ele dê apenas a resposta do jogo encontrado.
    # Para implementação: Quero poder fazer a busca com partes do nome do jogo e não apenas com o nome completo (talvez utilizando o ".split()"?). Algo a setentar no futuro.

# Alteração de Registro
def alterar_jogo():
    if not Jogos:
        print("\nNão há jogos cadastrados para alterar!");
        return
    
    nome_busca = input("\nInforme o nome completo do jogo a ser alterado: ").strip();

    # Verificação do nome do jogo na lista:
    for jogo in Jogos:
        if jogo["nome"].lower() == nome_busca.lower():
            print("\nO que você deseja alterar? \n 1 - Nome \n 2 - Tempo de jogo \n 3 - Preço \n Para outras opções: \n 4 - Voltar");
            opcao_alteracao = input("\nEscolha uma das opções informadas: ").strip();

            if opcao_alteracao == "1" or opcao_alteracao == "01": #Alteração do nome
                novo_nome = input("\n Digite o novo nome do jogo: ").strip();
                jogo["nome"] = novo_nome;
                print("\n Alteração realizada com sucesso!");
                return(exibir_menu());
            elif opcao_alteracao == "2" or opcao_alteracao == "02": #Alteração do tempo de jogo
                novo_tempo = input("\n Digite o novo tempo de jogo (apenas números): ").strip();
                jogo["Tempo de jogo"] = int(novo_tempo);
                print("\n Alteração realizada com sucesso!");
                return
            elif opcao_alteracao == "3" or opcao_alteracao == "03": #Alteração do preço
                novo_preco = input("\n Digite o novo preço do jogo (apenas números): ").strip();
                jogo["Preço"] = float(novo_preco);
                print("\n Alteração realizada com sucesso!");
                return
            elif opcao_alteracao == "4" or opcao_alteracao == "04": #Voltar ao menu anterior
                return
            else:
                print("\nNúmero inválido!");
                alterar_jogo();
        else:
            print("\nEste nome é inválido!");
            alterar_jogo();
    

# Remoção de registro

# Menu principal
def principal():
    while True:
        exibir_menu();
        opcao = input("Escolha uma das opções informadas:");
        if opcao == "1" or opcao == "01":
            listar_tudo();
        elif opcao == "2" or opcao == "02":
            cadastro_novo();
        elif opcao == "3" or opcao == "03":
            buscar_jogo();
        elif opcao == "4" or opcao == "04":
            alterar_jogo();
        elif opcao == "0" or opcao == "00":
            break;
        else:
            print ("\n Opção inválida. Escolha uma das opções sugerias!\n");
            return (exibir_menu());

principal()
