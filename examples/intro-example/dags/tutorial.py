from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime as dt
from datetime import timedelta

# Default _DAG_ parameters
default_args = {'owner': 'airflow', 'depends_past': False, 'start_date': dt(2020, 3, 23),
                'retries': 0}

# Create a DAG object that is scheduled to run every minute
dag = DAG('show_aws_config', default_args = default_args, schedule_interval = '30 07 * * * ')


# Create a task and associate it to the db
task = BashOperator(task_id = 'show',
                    bash_command = 'aws configure list',
                    dag = dag)