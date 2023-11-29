from datetime import datetime
import time

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

with DAG(
  dag_id= "upstream_dag",
  schedule_interval= "0 4  * * *",
  start_date= datetime(2018, 12, 9),
  catchup= False
) as dag:
  
  task_start_dag = EmptyOperator(
    task_id= "start_dag"
  )

  task_do_something = PythonOperator(
    task_id= "do_something",
    python_callable= lambda minutes: time.sleep(minutes*60),
    op_kwargs=dict(
      minutes= 3
    )
  )

  task_end_dag = EmptyOperator(
    task_id= "end_dag"
  )

  task_start_dag \
  >> task_do_something \
  >> task_end_dag