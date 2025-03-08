## com decorador @
# Maneira recomendada!

#Ordenando tasks com métodos: chain

from time import sleep
from airflow.decorators import dag, task
from airflow.models.baseoperator import chain
from datetime import datetime

@dag(
        dag_id = "minha_segunda_dag",
        description = "etl de exemplo para estudo",
        schedule = "* * * * *",
        start_date = datetime(2025, 3, 8),
        catchup = False #backfill
)
def pipeline():

    @task
    def primeira_atividade():
        return "minha primeira atividade!"

    @task
    def segunda_atividade(response):
        print(response)
        sleep(2)

    @task
    def terceira_atividade():
        print("minha terceira atividade!")
        sleep(2)

    @task
    def quarta_atividade():
        print("a pipeline rodou")


    task1 = primeira_atividade()
    task2 = segunda_atividade(task1)
    task3 = terceira_atividade()
    task4 = quarta_atividade()

    #task1 >> task2 >> task3 >> task4

    chain(task1, task2, task3, task4)

pipeline()
