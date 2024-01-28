
import kfp
from kfp.v2 import dsl
from kfp.v2.dsl import (
    component,
)
import os
script_dir = os.path.dirname(os.path.realpath(__file__))
input_file_yml = os.path.join(script_dir, '..', 'system_recomendation_insurance_pipelinev2.yaml')

from components.clustering_to_sepervised import clusturing_and_save_supervised_data
from components.evaluate_model_stacking import evaluate_model_staking
from components.evaluate_models_level0 import evaluate_models_level0
from components.preparation_data import preparation_data_for_clusturing
from components.train_model_stacking import train_model_staking
from components.train_test_split import train_test_split
from components.unbalanced_processing import unbalanced_data_procissing_to_balanced
@component(
    packages_to_install=['pandas == 2.1.3','numpy == 1.26.2'],
    base_image="python:3.8"
)
def preparation_data_for_clusturingv2():
    preparation_data_for_clusturing
    
    
    
    
    
@component(
    packages_to_install=['pandas == 2.1.3','numpy == 1.26.2','scikit-learn==1.3.2'],
    base_image="python:3.8"
)
def clusturing_and_save_supervised_datav2():
    clusturing_and_save_supervised_data
    
    
@component(
    packages_to_install=['pandas == 2.1.3','numpy == 1.26.2','scikit-learn==1.3.2'],
    base_image="python:3.8"
)
def unbalanced_data_procissing_to_balancedv2():
    unbalanced_data_procissing_to_balanced
    

@component(
    packages_to_install=['pandas == 2.1.3','numpy == 1.26.2','scikit-learn==1.3.2'],
    base_image="python:3.8"
)
def train_test_splitv2():
    train_test_split
    
@component(
    packages_to_install=['pandas == 2.1.3','numpy == 1.26.2','scikit-learn==1.3.2'],
    base_image="python:3.8"
)
def evaluate_models_level0v2():
   evaluate_models_level0


            
@component(
    packages_to_install=['pandas == 2.1.3','numpy == 1.26.2','scikit-learn==1.3.2'],
    base_image="python:3.8"
)
def train_model_stakingv2():
    train_model_staking
    

@component(
    packages_to_install=['pandas == 2.1.3','numpy == 1.26.2','scikit-learn==1.3.2'],
    base_image="python:3.8"
)
def evaluate_model_stakingv2():
    evaluate_model_staking
    
    

    
# Define the pipeline
@dsl.pipeline(
   name='Insurance Recomendation deploy in kubflow',
   description='ML pipeline  de System recomendation'
)
# Define parameters to be fed into pipeline
def systeme_recomendation_pipeline(data_path: str):
    preparation_task = preparation_data_for_clusturingv2()
    clusturing_task = clusturing_and_save_supervised_datav2().after(preparation_task)
    unbalanced_task = unbalanced_data_procissing_to_balancedv2().after(clusturing_task)
    train_test_split_task = train_test_splitv2().after(unbalanced_task)
    evaluate_models_task = evaluate_models_level0v2().after(train_test_split_task)
    train_staking_task = train_model_stakingv2().after(evaluate_models_task)
    evaluate_staking_task = evaluate_model_stakingv2().after(train_staking_task)
    
    # Set cache staleness for each task
    preparation_task.execution_options.caching_strategy.max_cache_staleness = "P0D"
    clusturing_task.execution_options.caching_strategy.max_cache_staleness = "P0D"
    unbalanced_task.execution_options.caching_strategy.max_cache_staleness = "P0D"
    train_test_split_task.execution_options.caching_strategy.max_cache_staleness = "P0D"
    evaluate_models_task.execution_options.caching_strategy.max_cache_staleness = "P0D"
    train_staking_task.execution_options.caching_strategy.max_cache_staleness = "P0D"
    evaluate_staking_task.execution_options.caching_strategy.max_cache_staleness = "P0D"
    
    
    if __name__ == "__main__":
        kfp.compiler.Compiler().compile(
            pipeline_func=systeme_recomendation_pipeline,
            package_path= input_file_yml)