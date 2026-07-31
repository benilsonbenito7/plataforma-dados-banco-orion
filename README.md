# plataforma de dados para o banco orion
##descricao do meu projecto:
Essa é uma plataforma que recebe dados das operações bancárias (clientes, contas, cartões, empréstimos e transações), armazena esses dados, faz tratamento e organização usando engenharia de dados, e transforma tudo em informações úteis para análise e tomada de decisão.

###Fluxo:
Operações do Banco
(clientes, pagamentos, transferências, empréstimos)

          ↓

Banco Operacional
(PostgreSQL)

          ↓

Pipeline de Dados
(PySpark + Databricks)

          ↓

Camada Bronze
(dados brutos)

          ↓

Camada Silver
(dados limpos e validados)

          ↓

Camada Gold
(métricas e indicadores)

          ↓

Relatórios / Dashboard / APIs Analíticas
