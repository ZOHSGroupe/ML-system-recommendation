def train_test_split():
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import MinMaxScaler
    import numpy as np
    import pandas as pd
    import pickle
    import os
    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_dir, '..', 'data', 'balanced_supervised-lerning-data-insurance.csv')
    input_y_train = os.path.join(script_dir, '..', 'data', 'y_train.npy')
    input_y_test = os.path.join(script_dir, '..', 'data', 'y_test.npy')
    input_X_train = os.path.join(script_dir, '..', 'data', 'X_train.npy')
    input_X_test = os.path.join(script_dir, '..', 'data', 'X_test.npy')
    input_minmaxscaler = os.path.join(script_dir, '..', 'data', 'minmaxscaler.pkl')


    balanced_insurance = pd.read_csv(input_file_path)
    X = balanced_insurance.drop('Cluster', axis=1)  # Exclude the 'Cluster' column
    y = balanced_insurance['Cluster']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    np.save(input_y_train, y_train)
    np.save(input_y_test, y_test)
    np.save(input_X_train, X_train)
    np.save(input_X_test, X_test)
    with open(input_minmaxscaler, 'wb') as scaler_file:
        pickle.dump(scaler, scaler_file)
        
    print("\n---- X_train ----")
    print("\n")
    print(X_train)
    
    print("\n---- X_test ----")
    print("\n")
    print(X_test)
    
    print("\n---- y_train ----")
    print("\n")
    print(y_train)
    
    print("\n---- y_test ----")
    print("\n")
    print(y_test)

if __name__ == "__main__":
    train_test_split()