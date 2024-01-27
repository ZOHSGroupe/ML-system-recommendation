import kfp
import kfp.compiler as compiler
import kfp.dsl as dsl
import os
from components.clustering_to_sepervised import clusturing_and_save_supervised_data
from components.evaluate_model_stacking import evaluate_model_staking
from components.evaluate_models_level0 import evaluate_models_level0
from components.preparation_data import preparation_data_for_clusturing
from components.train_model_stacking import train_model_staking
from components.train_test_split import train_test_split
from components.unbalanced_processing import unbalanced_data_procissing_to_balanced

script_dir = os.path.dirname(os.path.realpath(__file__))
input_file_yml = os.path.join(script_dir, '..', 'system_recomendation_insurance_pipelinev1.yaml')

create_step_preparation_data = kfp.components.create_component_from_func(
    func=preparation_data_for_clusturing,
    base_image='python:3.9',
    packages_to_install=['pandas == 2.1.3','numpy == 1.26.2']
)

create_step_clusturing_and_save_supervised_data = kfp.components.create_component_from_func(
    func=clusturing_and_save_supervised_data,
    base_image='python:3.9',
    packages_to_install=['pandas == 2.1.3','numpy == 1.26.2','scikit-learn==1.3.2']
)

create_step_unbalanced_data_procissing_to_balanced = kfp.components.create_component_from_func(
    func=unbalanced_data_procissing_to_balanced,
    base_image='python:3.9',
    packages_to_install=['pandas == 2.1.3','numpy == 1.26.2','scikit-learn==1.3.2']
)

create_step_train_test_split = kfp.components.create_component_from_func(
    func=train_test_split,
    base_image='python:3.9',
    packages_to_install=['pandas == 2.1.3','numpy == 1.26.2','scikit-learn==1.3.2']
)

create_step_evaluate_models_level0 = kfp.components.create_component_from_func(
    func=evaluate_models_level0,
    base_image='python:3.9',
    packages_to_install=['numpy == 1.26.2','scikit-learn==1.3.2']
)
create_step_train_model_staking = kfp.components.create_component_from_func(
    func=train_model_staking,
    base_image='python:3.9',
    packages_to_install=['numpy == 1.26.2','scikit-learn==1.3.2']
)
create_step_evaluate_model_staking = kfp.components.create_component_from_func(
    func=evaluate_model_staking,
    base_image='python:3.9',
    packages_to_install=['numpy == 1.26.2','scikit-learn==1.3.2']
)

# Define the pipeline
@dsl.pipeline(
   name='Insurance Recomendation deploy in kubflow',
   description='ML pipeline  de System recomendation'
)
# Define parameters to be fed into pipeline
def systeme_recomendation_pipeline(data_path: str):
    vop = dsl.VolumeOp(
    name="systme-recomendation_-vol",
    resource_name="systme-recomendation_vol", 
    size="2Gi", 
    modes=dsl.VOLUME_MODE_RWO)
    
    preparation_data_for_clustring = create_step_preparation_data().add_pvolumes({data_path: vop.volume})
    clusturing_and_save_supervised_data = create_step_clusturing_and_save_supervised_data().add_pvolumes({data_path: vop.volume}).after(preparation_data_for_clustring)
    unbalanced_data_procissing_to_balanced = create_step_unbalanced_data_procissing_to_balanced().add_pvolumes({data_path: vop.volume}).after(clusturing_and_save_supervised_data)
    train_test_split = create_step_train_test_split().add_pvolumes({data_path: vop.volume}).after(unbalanced_data_procissing_to_balanced)
    evaluate_models_level0 = create_step_evaluate_models_level0().add_pvolumes({data_path: vop.volume}).after(train_test_split)
    train_model_staking = create_step_train_model_staking().add_pvolumes({data_path: vop.volume}).after(evaluate_models_level0)
    evaluate_model_staking = create_step_evaluate_model_staking().add_pvolumes({data_path: vop.volume}).after(train_model_staking)
    
    preparation_data_for_clustring.execution_options.caching_strategy.max_cache_staleness = "P0D"
    clusturing_and_save_supervised_data.execution_options.caching_strategy.max_cache_staleness = "P0D"
    unbalanced_data_procissing_to_balanced.execution_options.caching_strategy.max_cache_staleness = "P0D"
    train_test_split.execution_options.caching_strategy.max_cache_staleness = "P0D"
    evaluate_models_level0.execution_options.caching_strategy.max_cache_staleness = "P0D"
    train_model_staking.execution_options.caching_strategy.max_cache_staleness = "P0D"
    evaluate_model_staking.execution_options.caching_strategy.max_cache_staleness = "P0D"


    if __name__ == '__main__':

        compiler.Compiler().compile(
            pipeline_func=systeme_recomendation_pipeline,
            package_path= input_file_yml
        )