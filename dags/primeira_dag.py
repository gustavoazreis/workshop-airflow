## com with -> iniciando e fechando a DAG

import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id = "teste_1_dag",
    start_date = datetime.datetime(2025, 3, 8),
    schedule = "@daily",
    catchup = False
):
    EmptyOperator(task_id = "tarefa")