import streamlit as st
import pandas as pd
import datetime as dt
from database import Database
from pages import Pages
from streamlit_card import card

# Criar a instancia do banco de Dados
#db = Database()
# Criar a Conexão com o Banco
#conn = db.conn
db = Database()
engine = Database.mysql()

categorias_df = Database.categorias_df(conn=engine)

class App:

    def __init__(self) -> None:
        pass

st.sidebar.title("Menu")
lancamento = st.sidebar.selectbox(
    '',['Cadastro Categorias','Cadastro Usuários','Lancamento Despesas','Lancamento Receita','Orçamento']
)


if lancamento == 'Lancamento Despesas':
   Pages.lancamento_despesas(engine,categorias_df)


elif lancamento == 'Cadastro Categorias':
    Pages.cadastro_categorias(engine,categorias_df)
    st.markdown('<style>div.Widget.row-widget.stDataFrame { height: 600px; font-size: 16px; }</style>', unsafe_allow_html=True)
    t = categorias_df.sort_values(['categoria'])
    style_options = """
            <style>
                th {
                    font-size: 25px;
                    text-align: center
                }
                td {
                    font-size: 20px;
                    text-align: center
                }

                tr {
                    font-size: 20px;
                    text-align: center
                }
            </style>
        """
    # Adiciona o estilo usando st.markdown
    st.markdown(style_options, unsafe_allow_html=True)

    # Exibe o DataFrame usando st.table
    st.table(t)
    
elif lancamento == 'Cadastro Usuários':
    Pages.cadasto_usuarios(engine)

elif lancamento == 'Receita':
    Pages.receitas(engine)


    
elif lancamento == "Lancamento Receita":
    dados = Pages.lancamentos_receitas(categorias_df,engine)

    dft = st.dataframe(
        dados,
        width=950,
        height=350,
        hide_index=True
    )

elif lancamento == 'Orçamento':
    
    #col1 = st.columns(1)

    # Assuming despesas is a list or DataFrame
    #col1[0].write(despesas)
    st.markdown("""<h1> Orçamento </h1>""",unsafe_allow_html=True)
    st.markdown("""<h2> Defina o Percentual de Gastos com Cada Categoria </h2>""",unsafe_allow_html=True)
    orcamento = Pages.budget(categorias_df,engine)
    
    df = Pages.actual_budget(engine=engine)
    despesas = Pages.despesas(engine)
    s = pd.merge(
            df,
            despesas,
            how='left',
            on='categoria'
    )
    
    s['Resultado'] = s['valor_maximo'] - s['valor_total_despesas']
    s.drop(columns={'valor_maximo'},inplace=True)
    st.dataframe(s, width=950, height=350, hide_index=True)