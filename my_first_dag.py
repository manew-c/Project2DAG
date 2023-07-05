# import library
from datetime import timedelta
# ไว้สร้างDAG
from airflow import DAG
# ไว้ใช้bash
from airflow.operators.bash_operator import BashOperator
# ไว้กำหนดวันเวลา
from airflow.utils.dates import days_ago 

#definine DAG arguments.
default_args = {
    'owner': 'manew001',
    'start_date': days_ago(0),
    'email': ['manew@fakemail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# define the DAG
dag = DAG(
    'my-first-dag',
    default_args=default_args,
    description='My first DAG',
    schedule_interval=timedelta(days=1),
)

# define the first task
extract = BashOperator(
    task_id='extract',
    bash_command='cut -d":" -f1,3,6 /etc/passwd > /home/project/airflow/dags/extracted-data.txt',
    dag=dag,
)
# define the second task
transform_and_load = BashOperator(
    task_id='transform',
    bash_command='tr ":" "," < /home/project/airflow/dags/extracted-data.txt > /home/project/airflow/dags/transformed-data.csv',
    dag=dag,
)
# task pipeline
extract >> transform_and_load

'''  คำสั่ง submitdag
cp my_first_dag.py $AIRFLOW_HOME/dags
airflow dags list
airflow dags list|grep "my-first-dag"
airflow tasks list my-first-dag    
'''