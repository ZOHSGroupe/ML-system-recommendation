def evaluate_model_staking():
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    from sklearn.metrics import confusion_matrix
    import numpy as np
    import os
    
    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_y_pred = os.path.join(script_dir, '..', 'data', 'y_pred.npy')
    input_y_test = os.path.join(script_dir, '..', 'data', 'y_test.npy')

    y_test = np.load(input_y_test , allow_pickle=True) 
    y_pred = np.load(input_y_pred, allow_pickle=True)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    #matrix confision
    matrix = confusion_matrix(y_test, y_pred)

    print(f"Stacking Classifier - Accuracy: {accuracy:.4f}, Precision: {precision:.4f}, Recall: {recall:.4f}, F1 Score: {f1:.4f}")
    print(matrix)
    
if __name__ == "__main__":
    evaluate_model_staking()