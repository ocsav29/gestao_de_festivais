# Gestão de Festivais

Projeto da unidade curricular de Ambientes de Desenvolvimento Colaborativo
da Universidade do Algarve.

## Objetivo

Desenvolver uma aplicação de consola em Python para gerir festivais.

## Estado atual

Menu inicial implementado.

## Funcionalidades previstas

- Criar, consultar, editar e eliminar eventos.
- Registar despesas e acompanhar o orçamento.
- Registar fornecedores e associá-los aos eventos.
- Registar bilhetes vendidos e calcular receitas.
- Registar participantes.
- Consultar um resumo financeiro de cada evento.

## Como executar

É necessário ter o Python 3 instalado.

No terminal, dentro da pasta do projeto, executar:

```bash
python main.py
```

No Windows também pode ser utilizado:

```bash
py main.py
```

## Editar eventos

Ficheiro: `editar_eventos.py` (autor: Miguel Palma)

Permite alterar os dados de um evento que já existe.

Como funciona:

1. São mostrados os eventos existentes com o respetivo id.
2. O utilizador escolhe o id do evento a editar.
3. Para cada campo é mostrado o valor atual entre `[ ]`.
   Carregar só em Enter mantém esse valor.
4. O evento só é alterado no fim, depois de todos os valores serem válidos.
   O id nunca é alterado.

Validações:

- Nome, descrição e local não podem ficar vazios.
- Data no formato DD/MM/AAAA e tem de ser uma data real.
- Capacidade tem de ser um número inteiro maior que zero.
- Orçamento tem de ser um número igual ou superior a zero
  (aceita vírgula ou ponto, ex.: 1500,50).

Para testar esta parte isoladamente, com eventos de exemplo:

```bash
python editar_eventos.py
```

## Equipa

- Vasco Silva
- Tomas cruz
- Miguel Palma