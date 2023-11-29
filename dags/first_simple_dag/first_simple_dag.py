from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from dags.first_simple_dag.utils import log_successful_run


with DAG(
  dag_id= 'first_simple_dag',
  schedule= None,
  start_date= datetime(2018, 12, 9),
  is_paused_upon_creation= True,
  tags= ['MODO', 'Learning'],
  default_args=dict(log_level= "DEBUG")
) as dag:
  
  task_start_dag = EmptyOperator(
    task_id= "start_dag"
  )

  simple_log_task = PythonOperator(
    task_id= "simple_log_task",
    python_callable= log_successful_run,
    op_kwargs= dict(
      msg= "{{ ds }}"
    )
  )

  task_end_dag = EmptyOperator(
    task_id= "end_dag"
  )

  task_start_dag >> simple_log_task >> task_end_dag