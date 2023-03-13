import psycopg2

from config import params_postgres


def conecta():
    conn = psycopg2.connect(
        database=params_postgres['database'],
        user=params_postgres['user'],
        password=params_postgres['password'],
        host=params_postgres['host'],
        port=params_postgres['port']
    )
    return conn