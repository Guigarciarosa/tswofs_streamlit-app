CREATE TABLE categorias (
    id INT PRIMARY KEY AUTO_INCREMENT,
    categoria VARCHAR(60),
    despesa_receita VARCHAR(60),
    inserted_at TIMESTAMP
);
INSERT INTO categorias VALUES(1,'Alimentação','Despesa','2024-01-30 14:08:01.778132');
INSERT INTO categorias VALUES(2,'MEi','Despesa','2024-01-30 14:08:10.116726');
INSERT INTO categorias VALUES(3,'TIM','Despesa','2024-01-30 14:08:30.924520');
INSERT INTO categorias VALUES(4,'Combustível','Despesa','2024-01-30 14:09:15.293773');
INSERT INTO categorias VALUES(5,'Oferta','Despesa','2024-01-30 14:09:21.725770');
INSERT INTO categorias VALUES(6,'Netflix','Despesa','2024-01-30 14:09:43.048156');
INSERT INTO categorias VALUES(7,'Barbearia','Despesa','2024-01-30 14:09:56.364510');
INSERT INTO categorias VALUES(8,'Salário','Receita','2024-01-30 15:01:45.546504');
INSERT INTO categorias VALUES(9,'Medicamentos','Despesa','2024-01-30 15:02:25.516066');
INSERT INTO categorias VALUES(10,'Aula de Viola','Receita','2024-01-31 09:42:35.886292');
INSERT INTO categorias VALUES(11,'Automoveis','Despesa','2024-01-31 19:46:39.957405');
INSERT INTO categorias VALUES(12,'Fatura de Cartão','Despesa','2024-02-01 09:59:02.819861');
INSERT INTO categorias VALUES(13,'Nubank','Despesa','2024-02-01 10:57:13.892061');
INSERT INTO categorias VALUES(14,'C6','Despesa','2024-02-01 10:57:22.130951');
INSERT INTO categorias VALUES(15,'Inter','Despesa','2024-02-01 11:00:00.608365');
INSERT INTO categorias VALUES(16,'Neon','Despesa','2024-02-01 15:01:44.597528');
INSERT INTO categorias VALUES(17,'Venda Apple Watch','Receita','2024-02-01 15:18:54.786279');
INSERT INTO categorias VALUES(18,'Saldo','Receita','2024-02-01 15:22:20.206151');

CREATE TABLE usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(30),
        password VARCHAR(30),
        inserted_at TIMESTAMP
    );
INSERT INTO usuarios VALUES(1,'guilherme','1234','2024-01-30');
INSERT INTO usuarios VALUES(2,'guilherme','1234','2024-01-30');
INSERT INTO usuarios VALUES(3,'guilherme','123456','2024-01-30 16:42:16.870147');
INSERT INTO usuarios VALUES(4,'','','2024-01-31 00:19:27.113442');
INSERT INTO usuarios VALUES(5,'','','2024-01-31 09:43:18.854851');
INSERT INTO usuarios VALUES(6,'','','2024-01-31 19:46:03.856778');
INSERT INTO usuarios VALUES(7,'','','2024-02-01 22:33:45.037313');
CREATE TABLE lancamentos_despesas (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        id_categoria INTEGER,
        categoria VARCHAR(30),
        forma_de_pagamento VARCHAR(30),
        parcelamento INTEGER,
        qtd_parcelas INTEGER,
        valor_total_despesas NUMERIC,
        inserted_at TIMESTAMP,
        deletar BOOLEAN,
        FOREIGN KEY(id_categoria) REFERENCES categorias(id)
    );
CREATE TABLE lancamentos_receitas (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    id_categoria INT,
    categoria VARCHAR(30),
    data TIMESTAMP,
    valor_receita NUMERIC,
    deletar BOOLEAN,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id)
);
INSERT INTO lancamentos_receitas VALUES(1,10,'Aula de Viola','2024-02-01',0,NULL);
INSERT INTO lancamentos_receitas VALUES(2,8,'Salário','2024-02-06',1200,NULL);
INSERT INTO lancamentos_receitas VALUES(3,10,'Aula de Viola','2024-02-01',0,NULL);
INSERT INTO lancamentos_receitas VALUES(4,10,'Aula de Viola','2024-02-10',400,NULL);
INSERT INTO lancamentos_receitas VALUES(5,10,'Aula de Viola','2024-02-01',0,NULL);
INSERT INTO lancamentos_receitas VALUES(6,17,'Venda Apple Watch','2024-02-10',300,NULL);
INSERT INTO lancamentos_receitas VALUES(7,10,'Aula de Viola','2024-02-01',0,NULL);
INSERT INTO lancamentos_receitas VALUES(8,10,'Aula de Viola','2024-02-01',0,NULL);
INSERT INTO lancamentos_receitas VALUES(9,18,'Saldo','2024-02-01',809.5,NULL);
INSERT INTO lancamentos_receitas VALUES(10,10,'Aula de Viola','2024-02-01',0,NULL);
INSERT INTO lancamentos_receitas VALUES(11,10,'Aula de Viola','2024-02-01',0,NULL);
INSERT INTO lancamentos_receitas VALUES(12,10,'Aula de Viola','2024-02-01',0,NULL);
CREATE TABLE IF NOT EXISTS "lancamento_despesas" (
"categoria" TEXT,
  "data" TIMESTAMP,
  "forma_pagamento" TEXT,
  "parcelamento" TEXT,
  "qtd_parcelas" INTEGER,
  "valor_total_despesas" REAL,
  "valor_parcela" INTEGER,
  "inserted_at" TIMESTAMP
);
INSERT INTO lancamento_despesas VALUES('C6','2024-02-01 15:00:59.749261','Cartão de Crédito','Não',0,839.8799999999999955,0,'2024-02-01 15:00:59.749261');
INSERT INTO lancamento_despesas VALUES('Nubank','2024-02-01 15:01:18.272503','Cartão de Crédito','Não',0,1066.960000000000036,0,'2024-02-01 15:01:18.272503');
INSERT INTO lancamento_despesas VALUES('Inter','2024-02-01 15:01:31.092119','Cartão de Crédito','Não',0,711.8799999999999955,0,'2024-02-01 15:01:31.092119');
INSERT INTO lancamento_despesas VALUES('Alimentação','2024-02-01 15:02:08.880271','Cartão de Crédito','Não',0,91.26000000000000511,0,'2024-02-01 15:02:08.880271');
INSERT INTO lancamento_despesas VALUES('Nubank','2024-03-01 00:00:00','Cartão de Crédito','Não',0,1418.200000000000045,0,NULL);
INSERT INTO lancamento_despesas VALUES('Nubank','2024-04-01 00:00:00','Cartão de Crédito','Não',0,1076.86999999999989,0,NULL);
INSERT INTO lancamento_despesas VALUES('Nubank','2024-05-01 00:00:00','Cartão de Crédito','Não',0,1076.86999999999989,0,NULL);
INSERT INTO lancamento_despesas VALUES('Nubank','2024-06-01 00:00:00','Cartão de Crédito','Não',0,193.5399999999999921,0,NULL);
INSERT INTO lancamento_despesas VALUES('Nubank','2024-07-01 00:00:00','Cartão de Crédito','Não',0,126.8900000000000005,0,NULL);
INSERT INTO lancamento_despesas VALUES('Nubank','2024-08-01 00:00:00','Cartão de Crédito','Não',0,62.46999999999999887,0,NULL);
INSERT INTO lancamento_despesas VALUES('Nubank','2024-09-01 00:00:00','Cartão de Crédito','Não',0,62.46999999999999887,0,NULL);
INSERT INTO lancamento_despesas VALUES('Nubank','2024-10-01 00:00:00','Cartão de Crédito','Não',0,62.46999999999999887,0,NULL);
INSERT INTO lancamento_despesas VALUES('Nubank','2024-11-01 00:00:00','Cartão de Crédito','Não',0,62.46999999999999887,0,NULL);
INSERT INTO lancamento_despesas VALUES('Inter','2024-02-01 00:00:00','Cartão de Crédito','Não',0,711.8799999999999955,0,NULL);
INSERT INTO lancamento_despesas VALUES('Inter','2024-03-01 00:00:00','Cartão de Crédito','Não',0,277.259999999999991,0,NULL);
INSERT INTO lancamento_despesas VALUES('Inter','2024-04-01 00:00:00','Cartão de Crédito','Não',0,161.0699999999999932,0,NULL);
INSERT INTO lancamento_despesas VALUES('Inter','2024-05-01 00:00:00','Cartão de Crédito','Não',0,161.0699999999999932,0,NULL);
INSERT INTO lancamento_despesas VALUES('Inter','2024-06-01 00:00:00','Cartão de Crédito','Não',0,110.6200000000000045,0,NULL);
INSERT INTO lancamento_despesas VALUES('Inter','2024-07-01 00:00:00','Cartão de Crédito','Não',0,74.96999999999999887,0,NULL);
INSERT INTO lancamento_despesas VALUES('Inter','2024-08-01 00:00:00','Cartão de Crédito','Não',0,74.96999999999999887,0,NULL);
INSERT INTO lancamento_despesas VALUES('C6','2024-03-01 00:00:00','Cartão de Crédito','Não',0,736.1299999999999955,0,NULL);
INSERT INTO lancamento_despesas VALUES('C6','2024-04-01 00:00:00','Cartão de Crédito','Não',0,641.92999999999995,0,NULL);
INSERT INTO lancamento_despesas VALUES('C6','2024-05-01 00:00:00','Cartão de Crédito','Não',0,641.92999999999995,0,NULL);
INSERT INTO lancamento_despesas VALUES('C6','2024-06-01 00:00:00','Cartão de Crédito','Não',0,476.8500000000000227,0,NULL);
INSERT INTO lancamento_despesas VALUES('C6','2024-07-01 00:00:00','Cartão de Crédito','Não',0,476.8500000000000227,0,NULL);
INSERT INTO lancamento_despesas VALUES('C6','2024-08-01 00:00:00','Cartão de Crédito','Não',0,393.8000000000000113,0,NULL);
INSERT INTO lancamento_despesas VALUES('C6','2024-09-01 00:00:00','Cartão de Crédito','Não',0,393.8000000000000113,0,NULL);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('categorias',18);
INSERT INTO sqlite_sequence VALUES('usuarios',7);
INSERT INTO sqlite_sequence VALUES('lancamentos_receitas',12);
COMMIT;