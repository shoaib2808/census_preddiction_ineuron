from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
from src.utils import save_obj
import os
from src.logging import logging


class model_trainer_class:
    def __init__(self):
        self.Model_path = os.path.join("Artifacts","Model.pkl")


    def Train_model(self,x_train,x_test,y_train,y_test):
        logging.info("=====================Model Training Started=====================")
        regressor=LogisticRegression(max_iter=1000)
        regressor.fit(x_train,y_train)
        y_pred=regressor.predict(x_test)
       
        accuracy=accuracy_score(y_test,y_pred)
        matrix=confusion_matrix(y_test,y_pred)
        print(accuracy)
        print(matrix)
        logging.info(f"Accuracy of the model is {accuracy*100} percent ")
        logging.info("Confusion matrix is==>")
        logging.info(matrix)

        logging.info("Model object saved")
        save_obj(self.Model_path,regressor)
        logging.info("=====================Model trining completed==================== ")
        
