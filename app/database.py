import sqlite3
import datetime as dt
import pandas as pd
import mysql.connector
from sqlalchemy  import create_engine


class Database:

    def __init__(self):
        #self.conn = sqlite3.connect(r'C:\Users\guilherme.dias\Documents\Thesimplewayofsaving_streamlit\db\twosf_db.sqlite3')
        pass
        
    def categorias_df(conn):
        cat_df = pd.read_sql_query('select * from categorias',con=conn)
        cat_df1 = cat_df[['categoria','despesa_receita']]
        cat_df1.rename(columns={'despesa_receita':'tipo'},inplace=True)
        cat_df1 = cat_df1.sort_values(['categoria'])
        return cat_df1
    
    def mysql():
        pkl = pd.read_pickle(r'.streamlit/db_cred.pkl')
        host = pkl['host'][0]
        user=pkl['user'][0]
        password=pkl['password'][0]
        database= pkl['database'][0]
        # Create a SQLAlchemy engine
        engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")
        return engine

