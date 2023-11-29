from datetime import datetime, timedelta

from airflow import DAG
from airflow.sensors.external_task import ExternalTaskSensor
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator

with DAG(
  dag_id= "downstream_dag",
  schedule_interval= '40 4  * * *',
  catchup= False,
  start_date= datetime(2018, 12, 9)
) as dag:
  
  task_start_dag = EmptyOperator(
    task_id= "start_dag"
  )

  sensor_checks_something = ExternalTaskSensor(
    task_id= "check_upstream_dag",
    external_dag_id= "upstream_dag",
    external_task_id= "end_dag",
    execution_delta= timedelta(minutes= 40),
    mode= "poke",
    poke_interval= 30,
    timeout= 240
  )

  task_do_something = BashOperator(
    task_id= "do_something",
    bash_command= "echo {{ dag['dag_id'] }}"
  )

  task_end_dag = EmptyOperator(
    task_id= "end_dag"
  )

  task_start_dag \
  >> sensor_checks_something >> task_do_something \
  >> task_end_dag