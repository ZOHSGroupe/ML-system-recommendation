def evaluate_models_level0():
    from sklearn.linear_model import LogisticRegression
    from sklearn.naive_bayes import GaussianNB
    from sklearn.svm import SVC
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.tree import ExtraTreeClassifier
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.ensemble import BaggingClassifier
    from sklearn.ensemble import GradientBoostingClassifier
    from sklearn.ensemble import AdaBoostClassifier
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    from sklearn.metrics import confusion_matrix
    import numpy as np
    import os
    script_dir = os.path.dirname(os.path.realpath(__file__))
    output_y_train = os.path.join(script_dir, '..', 'data', 'y_train.npy')
    output_y_test = os.path.join(script_dir, '..', 'data', 'y_test.npy')
    output_X_train = os.path.join(script_dir, '..', 'data', 'X_train.npy')
    output_X_test = os.path.join(script_dir, '..', 'data', 'X_test.npy')

    models = {
        'Logistic Regression': LogisticRegression(),
        'Naive Bayes': GaussianNB(),
        'Support Vector Machine': SVC(),
        'K-Nearest Neighbors': KNeighborsClassifier(),
        'Decision Tree': DecisionTreeClassifier(),
        'Random Forest': RandomForestClassifier(),
        'Bagging': BaggingClassifier(),
        'AdaBoost': AdaBoostClassifier(),
        'Gradient Boosting': GradientBoostingClassifier(),
        'Extra Trees': ExtraTreeClassifier(),
    }

    y_train = np.load(output_y_train, allow_pickle=True)
    y_test = np.load(output_y_test, allow_pickle=True)
    X_train = np.load(output_X_train, allow_pickle=True)
    X_test = np.load(output_X_test, allow_pickle=True)

 
    print(X_train)
    for name, model in models.items():
        try:
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred, average='weighted', zero_division=1)
            recall = recall_score(y_test, y_pred, average='weighted')
            f1 = f1_score(y_test, y_pred, average='weighted')

            confusion_mat = confusion_matrix(y_test, y_pred)

            print(f"{name} - Accuracy: {accuracy:.4f}, Precision: {precision:.4f}, Recall: {recall:.4f}, F1 Score: {f1:.4f}")
            print(f"Confusion Matrix:\n{confusion_mat}\n{'-'*50}")
        except Exception as e:
            print(f"Error occurred for {name}: {e}")

if __name__ == "__main__":
    evaluate_models_level0()
