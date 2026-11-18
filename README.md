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

## Equipa

- Vasco Silva
- Tomas cruz
- Miguel Palma