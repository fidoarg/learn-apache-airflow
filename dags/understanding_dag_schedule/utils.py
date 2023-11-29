from textwrap import dedent
from custom.logging import logger

def log_dag_run_parameters(**context):

  data_interval_start = context['data_interval_start']
  data_interval_end = context['data_interval_end']
  logical_date = context['ds']
  execution_date = context['execution_date']

  msg = dedent(f"""
    data_interval_start: {data_interval_start}
    data_interval_end: {data_interval_end}
    logical_date: {logical_date}
    execution_date: {execution_date}

  """)

  logger.info(msg)