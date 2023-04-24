import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from src.logging import logging



class Data_ingestion:
    def __init__(self):
      self.raw_data_path = os.path.join("Artifacts","Raw.csv")
      self.train_data_path = os.path.join("Artifacts","train.csv")
      self.test_data_path = os.path.join("Artifacts","test.csv")

    def get_Data(self):
        
        logging.info("======================Data collection started======================")
        data= pd.read_csv('Data\data.csv')

        logging.info("Raw Data Collected")

        data['class']=data['class'].map({" <=50K":1," >50K":0})

        data.to_csv(self.raw_data_path,index=False,header=True)
        logging.info("Raw Data stored at Location",self.raw_data_path )
        train_data,test_data= train_test_split(data,test_size=0.30,random_state=34)

        logging.info("Train test split completed")
        train_data.to_csv(self.train_data_path,index=False)

        logging.info(f"train Data stored at Location {self.train_data_path}" )


        test_data.to_csv(self.test_data_path,index=False)
        logging.info(f"Test Data stored at Location {self.test_data_path}" )
        
        logging.info("======================Data collection succesfull======================")
        return train_data,test_data

