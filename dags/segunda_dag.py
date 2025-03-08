## criando uma instância da class DAG -> minha_dag

import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

minha_dag = DAG(
    dag_id = "teste_2_dag",
    start_date = datetime.datetime(2025, 3, 8),
    schedule = "@daily",
    catchup = False
)
EmptyOperator(task_id = "tarefa", dag=minha_dag)