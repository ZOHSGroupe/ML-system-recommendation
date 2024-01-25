def clusturing_and_save_supervised_data():
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler
    import pandas as pd
    import os
    k_value =  3
    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_dir, '..', 'data', 'preparation_data_for_clusturing.csv')
    output_file_path = os.path.join(script_dir, '..', 'data', 'unbalanced_supervised-lerning-data-insurance.csv')

    insurance = pd.read_csv(input_file_path)
    datascaler = StandardScaler()
    data_numeric= insurance[['Seniority','Power', 'Cylinder_capacity', 'Value_vehicle', 'N_doors', 'Weight']]
    data_insurance_scaled = datascaler.fit_transform(data_numeric)
    kmeans = KMeans(n_clusters=k_value, init='k-means++', max_iter=300, n_init=10, random_state=0)
    insurance['Cluster'] = kmeans.fit_predict(data_insurance_scaled)
    insurance.to_csv(output_file_path, index=False)

if __name__ == "__main__":
    clusturing_and_save_supervised_data()