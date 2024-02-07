import pandas as pd
import streamlit as st
from database import Database
from sqlalchemy import text
import datetime as dt

class Pages:

    def __init__(self) -> None:
        pass
       
    def lancamento_despesas(conn,categorias_df):
        # Inicializa os valores no início do script
        if 'cate' not in st.session_state:
            st.session_state.cate = ""
        if 'data' not in st.session_state:
            st.session_state.data = None
        if 'forma_pagamento' not in st.session_state:
            st.session_state.forma_pagamento = ""
        if 'parcelamento' not in st.session_state:
            st.session_state.parcelamento = None
        if 'qtd_parcelas' not in st.session_state:
            st.session_state.qtd_parcelas = None
        if 'valor_total_despesas' not in st.session_state:
            st.session_state.valor_total_despesas = None
        if 'valor_parcela' not in st.session_state:
            st.session_state.valor_parcela = None
        if 'submitted' not in st.session_state:
            st.session_state.submitted = False

        st.title('The Simple Way Of Saving')

        despesas = categorias_df[categorias_df['tipo'] == 'Despesa']
        a = despesas['categoria'].unique()

        # criar o campo de orçamento
        with st.form("Lançamento Financeiro",clear_on_submit=True):
            # selecionar Categorias de Gasto
            cate = st.selectbox('Categorias', [*a])
            data = st.date_input('Data Pagamento')
            forma_pagamento = st.selectbox('Forma de Pagamento', ['Cartão de Crédito', 'Pix'])

            if forma_pagamento == 'Cartão de Crédito':
                parcelamento = st.selectbox('Parcelamento', ['Não', 'Sim'])
                if parcelamento == 'Sim':
                    qtd_parcelas = st.selectbox('Quantidade', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
                    valor_total_despesas = st.number_input('Valor Total da Despesa')
                    vpr = qtd_parcelas * valor_total_despesas
                    valor_parcela = st.number_input("Valor Parcela", vpr)
                
                else:
                    valor_total_despesas = st.number_input('Valor Total da Despesa')
                    valor_parcela = 0
                    qtd_parcelas = 0
            else:
                parcelamento = 0
                qtd_parcelas = 0
                valor_parcela = 0
                valor_total_despesas = st.number_input('Valor da Despesa')

            # Verifica se o botão "Salvar" foi clicado
            submit_form = st.form_submit_button("Salvar")

            # Chama a função apenas se o botão foi clicado
            if submit_form:
                # Criação do DataFrame e salvamento
                data = dt.datetime.today()
                df = pd.DataFrame(
                    {
                        'categoria': [cate],
                        'data': [data],
                        'forma_pagamento': [forma_pagamento],
                        'parcelamento': [parcelamento],
                        'qtd_parcelas': [qtd_parcelas],
                        'valor_total_despesas': [valor_total_despesas],
                        'valor_parcela': [valor_parcela],
                        'inserted_at': [data]
                    }
                )

                df.to_sql(
                    'lancamento_despesas',
                    con=conn,
                    index=False,
                    if_exists='append'
                )


    def cadastro_categorias(conn,categoria_df):
    
        with st.form('Categorias',clear_on_submit=True):
            categoria = st.text_input('Categoria')
            despesa_receita = st.selectbox('Tipo', ['Receita','Despesa'])
            sv_cate = st.form_submit_button('Salvar')

            if sv_cate:
                data = dt.datetime.today()
                df = pd.DataFrame({
                        'categoria': [categoria],
                        'despesa_receita':[despesa_receita],
                        'inserted_at': [data]
                    }
                )

                df.to_sql(
                    'categorias',
                    con=conn,
                    index=False,
                    if_exists='append'
                )

    def cadasto_usuarios(conn):
        with st.form('Cadastro Usuários',clear_on_submit=True):
            nome = st.text_input('Nome')
            senha = st.text_input('Senha',type='password')
            st.form_submit_button('Cadastrar')
            data =  dt.datetime.today()
            user = pd.DataFrame({
                'nome':[nome],
                'password':[senha],
                'inserted_at': [data]
            })

            user.to_sql(
                'usuarios',
                con=conn,
                if_exists='append',
                index=False
            )
    
    def lancamentos_receitas(categorias_df, engine):
        despesas = categorias_df[categorias_df['tipo'] == 'Receita']
        a = despesas['categoria'].unique()

        # criar o campo de orçamento
        with st.form("Lançamento Financeiro", clear_on_submit=True):
            # selecionar Categorias de Gasto
            cate = st.selectbox('Categorias', [*a])
            data_date = st.date_input('Data e Hora Recebimento', value=None)  # Combined date and time input
            valor = st.number_input('Valor Receita')
            buton = st.form_submit_button('Salvar')
            
            # Get the ID corresponding to the selected category
            id_cat = pd.read_sql_query(f"SELECT id FROM categorias WHERE categoria='{cate}'", con=engine)
            id_categoria = id_cat['id'][0]  # Assuming there's only one ID for each category
            
            # Check if a value was selected for data_date
            if data_date is not None:
                data_string = data_date.strftime('%Y-%m-%d %H:%M:%S')
                
                # Define the SQL query with values directly inserted
                query = f"""
                        INSERT INTO lancamentos_receitas (id_categoria, categoria, data, valor_receita)
                        VALUES ({id_categoria}, '{cate}', '{data_string}', {valor})
                        """
        
                # Execute the SQL query using SQLAlchemy's execute method
                with engine.connect() as connection:
                    connection.execute(text(query))
                    
    def total_receitas(conn):
        receitas = pd.read_sql_query(f"select * from lancamentos_receitas",con=conn)
        receitas['data'] = receitas['data'].astype('datetime64[ns]')
        receitas['mes'] = receitas['data'].dt.month
        soma_por_mes = receitas.groupby(['mes'])['valor_receita'].sum().reset_index()['valor_receita'][0]
        return soma_por_mes
    
    def total_despesas(conn):
        despesas = pd.read_sql_query(f"select * from tswos_dev.lancamento_despesas",con=conn)
        despesas['data'] = despesas['data'].astype('datetime64[ns]')
        despesas['mes'] = despesas['data'].dt.month
        valor_total = despesas['valor_total_despesas'].sum()
        return valor_total
    
    def despesas(conn):
        despesas_df = pd.read_sql_query(
            'select * from lancamentos_despesas',
            con=conn
            )
        despesas_df['data'] = despesas_df['data'].astype('datetime64[ns]')
        despesas_df['mes'] = despesas_df['data'].dt.month
        today = dt.date.today()
        despesas_df_loc = despesas_df[despesas_df['mes'] == today.month]
        #despesas_df.drop(columns={'inserted_at'},inplace=True)
        despesas_df_1 = despesas_df_loc[['categoria','valor_total_despesas']]
        return despesas_df_1
    
    def receitas(conn):
        receitas_df = pd.read_sql_query(
            'select * from lancamentos_receitas',
            con=conn
            )
        receitas_df['data'] = receitas_df['data'].astype('datetime64[ns]')
        receitas_df['mes'] = receitas_df['data'].dt.month
        #receitas_df.drop(columns={'inserted_at'},inplace=True)
        
        return receitas_df
    
    def dashboard(receitas):
        col1,col2,col3 = st.columns(3, gap='Large')
        # ender_filter = st.multiselect('Selecione o Mês', options=list(dados['mes'].unique()), default=list(dados['mes'].unique()))
        col1.subheader("Receitas")
        col1.markdown(f"<h1 style='color:green; border: 3px solid white; padding: 8px; text-align: center'>R${receitas}</h1>", unsafe_allow_html=True)

        # Display Despesas in col2 with a border and a larger font size
        col2.subheader('Despesas')
        col2.markdown(f"<h1 style='color:red; border: 3px solid white; padding: 8px; text-align: center'>R${receitas}</h1>", unsafe_allow_html=True)
        
        col3.subheader('Resultado')
        col3.markdown(f"<h1 style='color:red; border: 3px solid white; padding: 8px; text-align: center'>R${receitas}</h1>", unsafe_allow_html=True)

    def budget(categorias_df, engine):
        with st.form("Orçamento", clear_on_submit=True):
            # selecionar Categorias de Gasto
            despesas = categorias_df[categorias_df['tipo'] == 'Despesa']
            a = despesas['categoria'].unique()
            cate = st.selectbox('Categorias', [*a])
            valor = st.number_input('Valor Limite para essa categoria')
            buton = st.form_submit_button('Salvar')

            # Assuming data is not required for budget allocation timestamp
            
            # Format current datetime as string for insertion into the database
            data_string = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            table = pd.DataFrame(
                {
                    'categoria':[cate],
                    'data':[data_string],
                    'valor':[valor]
                }
            ).to_sql(
                'orcamento',
                con=engine,
                if_exists='append',
                index=False
            )


    def actual_budget(engine):
        ab = pd.read_sql_query(
            """
            SELECT categoria, data,valor as valor_maximo FROM tswos_dev.orcamento
            """,
            con=engine
        )
    

        receitas = pd.read_sql_query(
            """
            SELECT * FROM tswos_dev.lancamentos_receitas lc
            """,
            engine
        )
        receitas['data'] = receitas['data'].astype('datetime64[ns]')
        receitas['mes'] = receitas['data'].dt.month
        receitas = receitas[receitas['mes'] == dt.date.today().month]

        valor_receita_mes = receitas['valor_receita'].sum()

        ab = ab.groupby(['categoria','valor_maximo'])['data'].max().reset_index()
        ab['percentual_da_receita'] = ab['valor_maximo'] / valor_receita_mes
        #ab['percentual_da_receita'] = ab['percentual_da_receita'].round(2)
        ab = ab[ab['valor_maximo'] != 0]
        # Sort the DataFrame by the 'data' column in descending order
        ab_sorted = ab.sort_values(by='data', ascending=False)

        # Drop duplicate rows based on the 'categoria' column, keeping only the first occurrence
        ab_unique = ab_sorted.drop_duplicates(subset='categoria', keep='first')

        # Reset the index of the resulting DataFrame
        ab_unique_reset = ab_unique.reset_index(drop=True)
        ab_unique_reset['valor_maximo_1'] = ab_unique_reset['valor_maximo'].apply(lambda x: f'R$ {x:,.0f}')
        ab_unique_reset['percentual_da_receita'] = ab_unique_reset['percentual_da_receita'].apply(lambda x: f'{x:.2f}%')
        ab_unique_reset['valor_maximo'] = ab_unique_reset['valor_maximo'].astype('float64') 
        # Display the resulting DataFrame
        ab_unique_reset.rename(columns={
            'valor_maximo_1':'Valor Maximo',
            'data':'Data',
            'percentual_da_receita':'Percentual Receita'
        },inplace=True)
        

        return ab_unique_reset
