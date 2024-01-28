def unbalanced_data_procissing_to_balanced():
    import pandas as pd
    from sklearn.utils import resample
    import os

    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_dir, '..', 'data', 'unbalanced_supervised-lerning-data-insurance.csv')
    output_file_path = os.path.join(script_dir, '..', 'data', 'balanced_supervised-lerning-data-insurance.csv')
    insurance = pd.read_csv(input_file_path)
    print(insurance['Cluster'].value_counts())
    min_observation_count = insurance['Cluster'].value_counts().min()
    
    balanced_dfs = []

    for cluster_label, group in insurance.groupby('Cluster'):
        
        balanced_cluster = resample(group, replace=False, n_samples=min_observation_count, random_state=42)
    
        balanced_dfs.append(balanced_cluster)

    balanced_insurance = pd.concat(balanced_dfs, ignore_index=True)

    print(balanced_insurance['Cluster'].value_counts())
    print(balanced_insurance.shape)
    print(balanced_insurance.info())
    balanced_insurance.to_csv(output_file_path, index=False)

if __name__ == "__main__":
    unbalanced_data_procissing_to_balanced()