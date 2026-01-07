💰 Gestor de Patrimônio (Em Desenvolvimento)
Projeto prático que está sendo desenvolvido durante minha jornada de estudos em Ciência de Dados. O objetivo é criar um assistente financeiro completo, evoluindo de uma aplicação CLI (Linha de Comando) modular para um Web App com Inteligência Artificial para recomendações de investimento.

🎯 Objetivo
Aplicar conceitos de Engenharia de Dados, Análise e Desenvolvimento de Software em um problema real: Gestão e Inteligência Financeira.

🔨 Funcionalidades

✅ Fase 1: Core & Lógica (Concluída)
Interface via Terminal (CLI): Menu interativo e navegável sem necessidade de reiniciar o script.

Arquitetura Modular: Separação da lógica de negócios em funções reutilizáveis (Clean Code).

Gestão de Gastos: Input e categorização de gastos Fixos e Variáveis.

Cálculo de Sobra Mensal: Lógica matemática automática (Renda - Despesas).

Tratamento de Erros: Validação de inputs para impedir quebra do sistema.

✅ Fase 2: Persistência & Pandas (Concluída)
Persistência de Arquivos: Sistema de salvamento e leitura de dados em JSON (para configurações e gastos fixos) e CSV (para histórico de movimentações).

Introdução ao Pandas: Substituição de listas nativas por DataFrames para manipulação eficiente de tabelas em memória.

Organização Profissional: Estruturação do projeto em diretórios (src para código, dados para arquivos).

🔄 Fase 3: Engenharia de Dados & SQL (Em Andamento)
Integração Python-SQL: Criação de scripts de laboratório (lab_sql.py) para manipulação de banco de dados via código.

Modelagem de Dados: Criação de tabelas relacionais com tipagem forte e chaves primárias automáticas (PRIMARY KEY AUTOINCREMENT).

Manipulação em Lote (CRUD): Inserção performática de dados (executemany) e rotinas de limpeza (DELETE).

Consultas Inteligentes: Filtragem avançada de dados financeiros utilizando cláusulas WHERE, operadores lógicos e busca textual (LIKE).

Integração SQL-Pandas: Leitura direta de queries SQL transformadas em DataFrames para visualização tabular imediata.

🚀 Roadmap
[x] Fase 1: Fundamentos (CLI & Lógica)

[x] Fase 2: Persistência & Pandas (CSV/JSON)

[🔄] Fase 3: Engenharia de Dados (SQL & SQLite) (Fase Atual)

[ ] Fase 4: Análise & Estatística (Agrupamentos e Médias)

[ ] Fase 5: Visualização de Dados (Dashboards)

[ ] Fase 6: Web App (Streamlit)

[ ] Fase 7: Inteligência Artificial (Recomendação de Investimentos)

🛠️ Tecnologias Utilizadas
Atualmente:

Python (Lógica, Estruturas de Dados, Modularização)

SQL / SQLite (Banco de Dados e Persistência)

Pandas (Leitura de Dados e Dataframes)

VS Code (Ambiente de Desenvolvimento)

Gemini (Estruturação de Roadmap e assistente)

Próximos Passos:

Visualização: Matplotlib, Seaborn

Web Framework: Streamlit

Machine Learning: Scikit-Learn

Desenvolvido por George Dantas como parte do portfólio de Ciência de Dados.
