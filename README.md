# Gestão de Festivais

Projeto da unidade curricular de Ambientes de Desenvolvimento Colaborativo
da Universidade do Algarve.

## Objetivo

Desenvolver uma aplicação de consola em Python para gerir festivais.

## Estado atual

Funcionalidades implementadas:
- Criar eventos com validação dos dados.
- Guardar e carregar eventos em JSON.
- Eliminar eventos com confirmação.
- Registar despesas com categoria descrição e valor.
- Registar fornecedores e guardar os dados em JSON.
- Consultar o orçamento previsto e o total gasto por evento.

Os ficheiros eventos.json e fornecedores.json são criados
automaticamente durante a utilização e não são enviados para o GitHub.

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
## Receita dos bilhetes

Ficheiro: `receita.py` (autor: Miguel Palma)

Calcula automaticamente a receita dos bilhetes vendidos.

- Para cada evento mostra o número de bilhetes vendidos e a receita (€).
- No fim mostra a receita total de todos os eventos.
- Usa as vendas registadas no registo de bilhetes
  (campos `id_evento`, `quantidade`, `preco_unitario` e `total`).

Para testar esta parte isoladamente, com dados de exemplo:

```bash
python receita.py
```

## Registar participantes

Ficheiro: `participantes.py` (autor: Miguel Palma)

Permite inscrever participantes num evento e controlar o número de pessoas.

Como funciona:

1. O utilizador escolhe o evento pelo número da lista (0 cancela).
2. É mostrada a ocupação atual, por exemplo `Lugares ocupados: 2/3`.
3. Se o evento estiver lotado, a inscrição é recusada.
4. Caso contrário, são pedidos o nome e o contacto (telefone ou email).
   Nenhum dos campos pode ficar vazio.

Dados:

- Os participantes ficam dentro de cada evento, na lista `evento["participantes"]`.
- Cada participante tem `id` (código único), `nome` e `contacto`.
- São gravados no `eventos.json`, juntamente com o evento.

No menu principal: opção `8 - Registar participante`.

Para testar esta parte isoladamente, com eventos de exemplo:

```bash
python participantes.py
```

## Editar eventos

Ficheiro: `editar_eventos.py` (autor: Miguel Palma)

Permite alterar os dados de um evento que já existe.

Como funciona:

1. São mostrados os eventos existentes, numerados (1, 2, 3...).
2. O utilizador escolhe o número do evento a editar.
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

No menu principal: opção `3 - Editar evento`.

## Equipa

- Vasco Silva
- Tomas cruz
- Miguel Palma