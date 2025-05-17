import os 
import pandas as pd
from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from etl_project.youtube_pipeline.extract import Extract
from etl_project.youtube_pipeline.transform import Transform
from etl_project.youtube_pipeline.load import Load_CSV, Load_SQL

api_key = os.environ.get('YOUTUBE_API_KEY')

if not api_key:
    raise ValueError("YOUTUBE_API_KEY environment variable is not set")

default_args = {
    'owner': 'Brixsir',
    'email': 'brixterstudent@gmail.com',
    'start_date': datetime(2025, 4, 10)
}

def extract_task(api, **kwargs):
    raw_data = Extract(api)
    file_path = "/tmp/youtube_raw_data.parquet"
    raw_data.to_parquet(file_path)

    kwargs['ti'].xcom_push(key='file_path', value=file_path)

def transform_task(**kwargs):
    ti = kwargs['ti']
    file_path = ti.xcom_pull(key='file_path', task_ids='Extract_task')
    raw_data = pd.read_parquet(file_path)

    transformed_data = Transform(raw_data)
    transformed_path = "/tmp/youtube_transformed_data.parquet"
    transformed_data.to_parquet(transformed_path)

    ti.xcom_push(key='transformed_path', value=transformed_path)

def load_task(**kwargs):
    ti = kwargs['ti']
    transformed_path = ti.xcom_pull(key='transformed_path', task_ids='Transform_task')
    transformed_data = pd.read_parquet(transformed_path)

    # Save CSV in the dags directory which is mounted to the host
    output_path = '/opt/airflow/dags/clean_youtube_data.csv'

    Load_CSV(transformed_data, output_path)
    print(f"CSV file saved at: {output_path}")
    Load_SQL(transformed_data)

with DAG('youtube_etl_workflow', default_args=default_args, schedule='@hourly') as youtube_etl_dag:

    task1_extract = PythonOperator(
        task_id='Extract_task',
        python_callable=extract_task,
        op_kwargs={'api': api_key}
    )

    task2_transform = PythonOperator(
        task_id='Transform_task',
        python_callable=transform_task
    )

    task3_load = PythonOperator(
        task_id='Load_task',
        python_callable=load_task
    )
# -- Draft
    #task4_email = EmailOperator(
        #task_id='Email_task',
        #to='@gmail.com',
        #subject='youtube_data',
        #html_content='attached is the csv for youtube_data',
        #files=['clean_youtube_data.csv']
    #)
    # >> task4_email

    task1_extract >> task2_transform >> task3_load 
