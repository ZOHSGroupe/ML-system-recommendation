def train_model_staking():
    from sklearn.linear_model import LogisticRegression
    from sklearn.naive_bayes import GaussianNB
    from sklearn.svm import SVC
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.ensemble import AdaBoostClassifier
    import numpy as np
    import pickle
    from sklearn.ensemble import StackingClassifier
    import os

    script_dir = os.path.dirname(os.path.realpath(__file__))
    output_y_train = os.path.join(script_dir, '..', 'data', 'y_train.npy')
    output_X_train = os.path.join(script_dir, '..', 'data', 'X_train.npy')
    output_X_test = os.path.join(script_dir, '..', 'data', 'X_test.npy')
    input_file_model = os.path.join(script_dir, '..', 'data', 'model.pkl')
    input_y_pred = os.path.join(script_dir, '..','data', 'y_pred.npy')

    y_train = np.load(output_y_train,allow_pickle=True)
    X_train = np.load(output_X_train, allow_pickle=True)
    X_test = np.load(output_X_test, allow_pickle=True)


    level0 = [
    ('AdaBoost', AdaBoostClassifier()),
    ('Naive Bayes', GaussianNB()),
    ('Support Vector Machine', SVC()),
    ('K-Nearest Neighbors', KNeighborsClassifier()),
    ('Random Forest', RandomForestClassifier())
    ]
    
    # Define level1 classifier
    level1 = LogisticRegression(max_iter=1000)
    
    # Create StackingClassifier
    model = StackingClassifier(estimators=level0, final_estimator=level1, cv=5)
    
    # Fit the model
    model.fit(X_train, y_train)
    

    with open(input_file_model, 'wb') as model_file:
        pickle.dump(model, model_file)
        
    # Predictions
    y_pred = model.predict(X_test)
    np.save(input_y_pred, y_pred) 
    print(y_pred)

if __name__ == "__main__":
    train_model_staking()
    