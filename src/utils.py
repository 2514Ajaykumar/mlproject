import os
import sys
import pandas as pd
import dill
import numpy as np

from sklearn.metrics import r2_score
from src.exception import CustomException   
def save_object(obj, file_path):
    '''
    this function is responsible for saving the object
    '''
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as file:
            dill.dump(obj,file)
    except Exception as e:
        raise CustomException(e, sys)
    

from sklearn.metrics import r2_score

def evaluate_models(X_train, y_train, X_test, y_test, models):
    report = {}
    for model_name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        r2 = r2_score(y_test, y_pred)
        report[model_name] = r2
    return report