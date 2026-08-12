# Trabalho para criação de um sistema de cadastro

## O que é?
* Um programa de console com menu, que cadastra, lista, busca, altera e remove registros
* Tudo em Python estruturado

## Entrega
* Individual ou em dupla
* Um arquivo .py enviado pelo Moodle
* Nome do(s) autor(es) em comentário na 1ª linha

## Por que este trabalho?
* Ele usa TUDO que revisamos hoje
* E será o código que você vai refatorar em Orientação a Objetos

## Requisitos obrigatórios
* Menu em laço, com opção de sair
  - while com sentinela · tratar opção inválida sem quebrar o programa

* Cadastrar registro
** Ler os dados com input(), converter os tipos e adicionar à lista com append()

* Listar todos os registros
** Percorrer com for e exibir em formato de tabela, usando alinhamento na f-string

* Buscar por um campo identificador
** Percorrer a lista e informar claramente quando não encontrar

* Alterar e remover um registro
** Localizar pelo identificador e confirmar a operação com o usuário

* Relatório com cálculo
** Ao menos um resumo: total de registros, média, maior e menor valor

* Validação das entradas
** Nada de programa que quebra: use try/except e valide faixas de valores

## Como será avaliado
* (2,0) Menu e fluxo do programa Laço, saída, opção inválida tratada
* (2,0) Cadastro e listagem Uso correto de lista, dicionário e f-string
* (2,0) Busca, alteração e remoção Lógica correta e mensagens claras
* (1,5) Relatório com cálculo Uso de len, sum, max, min ou laço acumulador
* (1,5) Uso de funções Cada operação em sua própria função, com parâmetros e retorno
* (1,0) Validação e legibilidade try/except, nomes claros e comentários pertinentes

## Como não travar: estratégia de execução
* Comece pelo menu, com as funções vazias
**Use pass no corpo. Rode e veja o menu funcionando antes de escrever qualquer lógica.
Implemente cadastrar e listar primeiro
Com essas duas você já consegue testar todas as outras funcionalidades.
Teste a cada função concluída
Nunca escreva 200 linhas para só então executar. Rode a cada 10 ou 15 linhas.
Faça cópias do arquivo conforme avança
revisao_v1.py, revisao_v2.py… Assim você nunca perde uma versão que funcionava.
Travou? Traga a mensagem de erro
Poste no fórum do Moodle ou me procure com o print do erro — não fique parado a semana toda.
