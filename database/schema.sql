-- Tabela responsável por armazenar categorias financeiras
CREATE TABLE categorias (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL, -- Nome da categoria (ex: MERCADO, SALARIO)
    tipo VARCHAR(10) NOT NULL -- ENTRADA ou SAIDA
);

-- Tabela responsável por armazenar transações
CREATE TABLE transacoes (
  id SERIAL PRIMARY KEY,
  data DATE NOT NULL,
  tipo VARCHAR(10) NOT NULL, -- ENTRADA ou SAIDA
  sub_tipo VARCHAR(8) NOT NULL, -- FIXO ou VARIAVEL
  descricao VARCHAR(50) NOT NULL, -- Descrição da transação (EX. Uber, fastfood, conta de luz)
  valor NUMERIC (10,2) NOT NULL,
  categoria_id INTEGER NOT NULL,
  FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);

--Inserir primeira transaçao
INSERT INTO transacoes (data, tipo, sub_tipo, descricao, valor, categoria_id)
VALUES ('2026-06-08', 'ENTRADA', 'FIXO', 'SALARIO DO MÊS', 2050, 1);
SELECT * FROM transacoes

--exibe nome da categoria ao invés do ID
SELECT transacoes.data, transacoes.descricao, transacoes.valor, transacoes.tipo, categorias.nome
FROM transacoes
INNER JOIN categorias
ON transacoes.categoria_id = categorias.id
