import sqlite3
import pandas as pd


def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn


def create_table(conn):
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS servicios (
        puerto INTEGER,
        nombre_servicio TEXT,
        ip TEXT
    );
    '''
    conn.execute(create_table_query)


def insert_data(conn, df):
    df.to_sql('servicios', conn, if_exists='replace', index=False)


def select_all_data(conn):
    select_query = 'SELECT * FROM servicios;'
    result = pd.read_sql_query(select_query, conn)
    return result


def update_data(conn, update_query):
    conn.execute(update_query)


def delete_data(conn, delete_query):
    conn.execute(delete_query)
