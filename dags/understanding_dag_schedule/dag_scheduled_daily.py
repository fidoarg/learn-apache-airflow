from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

from dags.understanding_dag_schedule.utils import log_dag_run_parameters


with DAG(
  dag_id= 'dag_scheduled_daily',
  schedule= "@daily",
  start_date= datetime(2018, 12, 9),
  is_paused_upon_creation= True,
  catchup= False,
  tags= ['MODO', 'Learning'],
  default_args=dict(log_level= "DEBUG")
) as dag:
  
  task_start_dag = EmptyOperator(
    task_id= "start_dag"
  )

  task_log_parameters = PythonOperator(
    task_id= "log_parameters",
    python_callable= log_dag_run_parameters,
    show_return_value_in_logs= False
  )

  task_end_dag = EmptyOperator(
    task_id= "end_dag"
  )

  task_start_dag >> task_log_parameters >> task_end_dag