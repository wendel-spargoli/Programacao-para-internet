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
    print ("\nBem-vindo(a) à sua lista de jogos! O que você quer fazer hoje? \n 1 - Listar jogos \n 2 - Cadastrar jogos \n 3 - Buscar jogo \n 4 - Alterar jogo \n 5 - Remover jogo \n 6 - Jogo mais caro \n 0 - Sair");

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
                return;
            else:
                print("\nNúmero inválido!");
                alterar_jogo();
    print("\nEste nome é inválido!"); #Fora do laço porque dentro do "for" não permitia checar todos os jogos. No primeiro jogo, já passava para o "else"
    

# Remoção de registro
def remocao_jogo():
    print("\nQual jogo você gostaria de remover da lista?");
    termo_busca = input("\nDigite o nome completo do jogo a ser removido. (Se estiver em dúvidas de como está escrito, escreva 'listagem' para abrir a lista de jogos): ").strip();

    if termo_busca.lower() == "listagem": # Comando para o caso de a pessoa escolher listar os jogos.
        listar_tudo();
    

    for jogo in Jogos:
        if termo_busca.lower() == jogo["nome"].lower():
            Jogos.remove(jogo);
            print("\nJogo removido com sucesso!");
            return;

# Verificação de jogo de maior valor
def mais_caro():
    jogo_mais_caro = Jogos[0] # Definindo o primeiro item da lista como o mais caro para comparações

    for jogo in Jogos:
        if float(jogo["Preço"]) > float(jogo_mais_caro["Preço"]):
            jogo_mais_caro = jogo;
        print(f"\nO jogo mais caro da lista é {jogo_mais_caro['nome']}, no valor de R$ {jogo_mais_caro['Preço']:.2f} reais.");

# Validação das entradas

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
        elif opcao == "5" or opcao == "05":
            remocao_jogo();
        elif opcao == "6" or opcao == "06":
            mais_caro();
        elif opcao == "0" or opcao == "00":
            break;
        else:
            print ("\n Opção inválida. Escolha uma das opções sugerias!\n");
            return (exibir_menu());

principal()
