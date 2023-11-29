from datetime import datetime
import time

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

from dags.understanding_groups_and_mapped_tasks.utils import generate_input, compute_input
with DAG(
  dag_id= "mapped_tasks_dag",
  schedule= None,
  start_date= datetime(2018, 12, 9)
) as dag:
  
  task_start_dag = EmptyOperator(
    task_id= "start_dag"
  )

  task_generate_input = PythonOperator(
    task_id= "generate_input",
    python_callable= generate_input,
    op_kwargs=dict(
      number_of_inputs= 2
    )
  )

  task_compute_inputs = PythonOperator.partial(
    task_id= "compute_inputs",
    python_callable= compute_input
  ).expand(
    op_kwargs= task_generate_input.output
  )

  task_end_dag = EmptyOperator(
    task_id= "end_dag"
  )

  task_start_dag \
  >> task_generate_input >> task_compute_inputs \
  >> task_end_dag