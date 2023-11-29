from datetime import datetime

from airflow import DAG
from airflow.utils.trigger_rule import TriggerRule
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator 

from dags.understanding_dependencies.utils import define_branch_by_number

with DAG(
  dag_id= 'undestanding_branches',
  schedule= None,
  start_date= datetime(2018, 12, 9),
  is_paused_upon_creation= True,
  catchup= False,
  tags= ['MODO', 'Learning'],
  default_args=dict(log_level= "DEBUG")
) as dag:
  
  task_start_dag = EmptyOperator(
    task_id= "start_dag"
  )

  task_branch_operator_by_number = BranchPythonOperator(
    task_id= "branch_operator_by_number",
    python_callable= define_branch_by_number,
    op_kwargs=dict(number= 1)
  )

  task_parallel_01 = BashOperator(
    task_id= "parallel_01",
    bash_command= "exit 0"
  )
  task_parallel_02 = BashOperator(
    task_id= "parallel_02",
    bash_command= "exit 0"
  )
  task_parallel_03 = BashOperator(
    task_id= "parallel_03",
    bash_command= "exit 0"
  )
  task_end_dag = EmptyOperator(
    task_id= "end_dag",
    
    trigger_rule= TriggerRule.ALL_SUCCESS
  )

  task_start_dag >> task_branch_operator_by_number >> [
    task_parallel_01,
    task_parallel_02,
    task_parallel_03
  ] >> task_end_dag