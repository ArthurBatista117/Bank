Sistema Bancário em Python

Descrição

Este é um sistema bancário simples desenvolvido em Python, que permite aos usuários criarem contas, acessarem seus saldos e realizarem transações como depósitos e saques.

Funcionalidades

Criar uma nova conta bancária

Acessar uma conta existente

Depositar valores na conta

Sacar valores da conta

Verificar saldo

Requisitos

Python 3.x instalado

Instalação

Para clonar o repositório e rodar o projeto, execute os seguintes comandos:

git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_PROJETO>
python main.py

Uso

Execute o arquivo main.py.

Escolha uma das opções do menu:

[1] Access your account para acessar uma conta existente.

[2] Create a new account para criar uma nova conta.

Siga as instruções exibidas na tela para realizar depósitos, saques e consultas de saldo.

Estrutura do Projeto

/
│── main.py      # Arquivo principal do sistema
│── Bank.py      # Classe principal que gerencia contas bancárias
│── accounts.csv # Banco de dados das contas (caso exista)

Exemplo de Uso

Criando uma Conta

Write your best email: usuario@email.com
Password: ******
Confirm: ******

Acessando uma Conta

Write your email: usuario@email.com
Password: ******

Depositando

You want a deposit here?(D) or a windrow(W)? D
Value: 500

Sacando

You want a deposit here?(D) or a windrow(W)? W
Value: 200

Licença

Este projeto está sob a licença MIT. Sinta-se livre para modificá-lo e usá-lo conforme necessário.
