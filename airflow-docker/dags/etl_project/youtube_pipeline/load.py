from .extract import Extract
from .transform import Transform
import pandas as pd
from sqlalchemy import create_engine
from airflow.hooks.base import BaseHook


def Load_CSV(clean_data, filepath):
    """
    Saves the cleaned and transformed YouTube data to a CSV file.

    :param clean_data: A pandas DataFrame containing cleaned and transformed YouTube video data.
    :param filepath: The full path (including filename) where the CSV should be saved.
    :returns: None
    :rtype: None
    """
    clean_data.to_csv(filepath, index=False)
    


def Load_SQL(clean_data):
    """
    Saves the cleaned and transformed YouTube data to a local PostgreSQL database.

    :param clean_data: A pandas DataFrame containing cleaned and transformed YouTube video data.
    """

    conn = BaseHook.get_connection("my_postgres_conn")
    conn_str = f"postgresql://{conn.login}:{conn.password}@{conn.host}:{conn.port}/{conn.schema}"
    engine = create_engine(conn_str)
    clean_data.to_sql('youtube_data', con=engine, if_exists='replace', index=False)

    
