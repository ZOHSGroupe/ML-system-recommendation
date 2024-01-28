from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from my_ML_Pipeline.components.evaluate_model_stacking import evaluate_model_staking
from my_ML_Pipeline.components.evaluate_models_level0 import evaluate_models_level0
from my_ML_Pipeline.components.train_test_split import train_test_split
from my_ML_Pipeline.components.unbalanced_processing import unbalanced_data_procissing_to_balanced
from my_ML_Pipeline.components.train_model_stacking import train_model_staking


default_args = {
    'owner': 'airscholar',
    'start_date': datetime(2023, 1, 27, 12, 00)
}

with DAG(
    'flask_airflow_integration',
    default_args=default_args,
    description='DAG for Flask and Airflow integration to train model for each month',
    schedule_interval='@monthly',
    catchup=False
) as dag: 

    unbalanced_data_procissing_to_balanced_task_operator = PythonOperator(
        task_id='processing_unbalenced',
        python_callable=unbalanced_data_procissing_to_balanced,
        provide_context=True,
        dag=dag,
    )

    train_test_split_task_operator = PythonOperator(
        task_id='train_test_split',
        python_callable=train_test_split,
        provide_context=True,
        dag=dag,
    )

    train_model_staking_task_operator = PythonOperator(
        task_id='train_model_staking',
        python_callable=train_model_staking,
        provide_context=True,
        dag=dag,
    )

    evaluate_models_level0_task_operator = PythonOperator(
        task_id='evaluate_models_level0',
        python_callable=evaluate_models_level0,
        provide_context=True,
        dag=dag,
    )

    evaluate_model_staking_task_operator = PythonOperator(
        task_id='evaluate_model_staking',
        python_callable=evaluate_model_staking,
        provide_context=True,
        dag=dag,
    )

    unbalanced_data_procissing_to_balanced_task_operator >> train_test_split_task_operator >> train_model_staking_task_operator >> evaluate_models_level0_task_operator >> evaluate_model_staking_task_operator
