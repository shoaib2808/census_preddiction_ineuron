import os
import sys

from src.components.Data_ingestion import Data_ingestion
from src.components.Data_transformation import Data_transformation_class
from src.components.model_traniner import model_trainer_class

if __name__=='__main__':
        obj=Data_ingestion()
        train_data,test_data=obj.get_Data()
        obj2=Data_transformation_class()
        x_train,x_test,y_train,y_test=obj2.initiate_data_transformation(train_data,test_data)
        obj3=model_trainer_class()
        obj3.Train_model(x_train,x_test,y_train,y_test)