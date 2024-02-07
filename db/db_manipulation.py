import sqlite3

def create_table_categorias_despesas():
    conn = sqlite3.connect(r'../db/twosf_db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(
    """create table categorias(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categoria VARCHAR(60),
            despesa_receita VARCHAR(60),
            inserted_at TIMESTAMP
        )"""
    )
#create_table_categorias_despesas()

def delete_table():
    conn = sqlite3.connect(r'../db/twosf_db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(
    """drop table lancamento_despesas"""
    )
#delete_table()

def create_table_usuarios():
    conn = sqlite3.connect(r'../db/twosf_db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(
    """ create table usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(30),
        password VARCHAR(30),
        inserted_at TIMESTAMP
    )"""
    )
    cursor.fetchall()
#create_table_usuarios()
    
def create_table_lancamentos_despesas():
    conn = sqlite3.connect(r'../db/twosf_db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(
    """ create table lancamentos_despesas (
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
    )"""
    )
    cursor.fetchall()
    conn.close()

#create_table_lancamentos_despesas()

def create_table_lancamento_receitas():
    conn = sqlite3.connect(r'../db/twosf_db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(
    """ create table lancamentos_receitas (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        id_categoria INTEGER,
        categoria VARCHAR(30),
        data TIMESTAMP,
        valor_receita NUMERIC,
        deletar BOOLEAN,   
        FOREIGN KEY(id_categoria) REFERENCES categorias(id)
    )"""
    )
    cursor.fetchall()
    conn.close()
#create_table_lancamento_receitas()

import subprocess

def create_sqlite_dump(database_path, output_file):
    try:
        # Use subprocess to execute sqlite3 command
        with open(output_file, 'w') as outfile:
            subprocess.run(["sqlite3", database_path, ".dump"], check=True, text=True, stdout=outfile, shell=True)
        print(f"Dump created successfully and saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error creating dump: {e}")

# Replace 'your_database.db' and 'dump.sql' with your actual database file and desired dump file
#create_sqlite_dump(r'../db/twosf_db.sqlite3', 'dump.sql')
