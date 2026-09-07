''''
Autor do projeto: Wendel Spargoli

Parte 2 do Mini-trabalho refatoração do código para POO

criação de um sistema de cadastro de jogos
'''

# Classe jogos (superclasse)
class Jogo:
    def __init__(self, nome, tempo_jogo, preco):
        self.nome = nome;
        self.tempo_jogo = tempo_jogo;
        self.__preco = preco; # preço marcado como privado para evitar alterações indesejadas

    def get_preco(self): # Método para leitura de dado privado
        return self.__preco

    def __str__(self): # Função para formatar a estring a ser usada
            return f"{self.nome} - {self.tempo_jogo}hrs jogadas em média - {self.get_preco()} reais."

# Subclasse para identificação de jogos digitais
class jogo_digital(Jogo):
    def __init__(self, nome, tempo_jogo, preco, tamanho, loja):
        super().__init__(nome, tempo_jogo, preco);
        self.tamanho = tamanho
        self.loja = loja

    def __str__(self): # formatação da estring, puxando dados da mãe
        return f"{super(). __str__()} - {self.tamanho}Gb - comprado no {self.loja}."

# Subclasse para identificação de jogos físicos
class jogo_fisico(Jogo):
    def __init__(self, nome, tempo_jogo, preco, formato, plataforma):
        super().__init__(nome, tempo_jogo, preco);
        self.formato = formato
        self.plataforma = plataforma

    def __str__(self): # formatação da estring, puxando dados da mãe
        return f"{super(). __str__()} - {self.formato} - para ser jogado no {self.plataforma}."

# Lista de jogos
Jogos = [] # Lista em aberto para o cadastro

# Criação de Menu
def exibir_menu():
    print ("\nBem-vindo(a) à sua lista de jogos! O que você quer fazer hoje? \n 1 - Listar jogos \n 2 - Cadastrar jogos \n 3 - Buscar jogo \n 4 - Alterar jogo \n 5 - Remover jogo \n 6 - Jogo mais caro \n 0 - Sair");

# 1 - Listagem de Jogos
''''
def listar_tudo():
    if not Jogos:
        print("\n Não há jogos no momento!\n")
    else:
        for jogo in Jogos:
            print(f"{jogo['nome']:>10}{jogo['Tempo de jogo']:>10}{jogo['Preço']:>10}");
'''

# 2 - Cadastro de jogos
def cadastro_jogo():
    print("\nBem-vindo(a) ao cadastro de jogos! \nPor favor, insira as seguintes informações:\n");
    nome = input("Digite o nome do jogo: ").strip(); #Utilização do "strip()" para eliminar os espaços do início e fim
    tempo_jogo = input("Digite o tempo médio de jogo (em horas): ").strip();
    preco = input(float("Digite o valor do jogo em reais: ")).strip().replace(",","."); # Utilizei a IA para me ajudar a entender como substituir a vírgula pelo ponto, caso o usuário escreva o valor com vírgula e o código precise ler.

    print("\nEscolha a categoria que a qual seu jogo pertence: \n").stip();
    categoria = input("\n 1 - Jogo digital \n2 - Jogo físico")
    if categoria == ["01", "1"]:
        tamanho = input(float("\nInforme o tamanho aproximado do jogo: ")).strip().replace(",",".");
