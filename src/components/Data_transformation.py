import pandas as pd
import numpy as np
import os
import pickle
from sklearn. pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer
from sklearn.base import BaseEstimator,TransformerMixin
from src.utils import save_obj
from src.logging import logging


class custum_transformer(BaseEstimator,TransformerMixin):
    def __init__(self,col):
        self.col=col
        

    def fit(self, X, y=None):
        X=pd.DataFrame(X)
        print(X.columns)
        self.top3 = X[self.col].value_counts().head(3).index
        return self
        
    
    def transform(self, X, y=None):
        print(self.top3)
        for j in self.top3 :
            X['workclass'+"_"+j]=np.where(X['workclass']==j,1,0)
            print("Func call complete")
            return X

class Data_transformation_class:
    
    def __init__(self):
        self.Transformed_data_path=os.path.join("Artifacts","processor.pkl")
    
    def drop_columns(self,df,col):
        col_list=list(col)
        for i in col_list:
          logging.info("Column dropped ",i)
          df.drop(i,axis=1,inplace=True)

   
    def get_Transform_data_obj(self,train_data,test_data):
        
        categorical_col= train_data.columns[train_data.dtypes=='object']
        numerical_col= train_data.columns[train_data.dtypes!='object']
        pipeline_col =['marital-status','relationship','race','sex']
        pipeline2_col = ['workclass','occupation']
       
        num_pipeline = Pipeline([
            ('imputer',SimpleImputer(strategy='median')),
            ('scalar',MinMaxScaler())
        ])
        
        cat_pipeline = Pipeline([
            ('imputer',SimpleImputer(strategy='most_frequent')),
            ('encoder',OneHotEncoder())
        ])

        cat_pipeline2= Pipeline(
            [
            ('transformer',custum_transformer('workclass'))
            ]
        )
        cat_pipeline2.fit(train_data)
        cat_pipeline2.transform(train_data)
        processor = ColumnTransformer([
            ('num_pipeline',num_pipeline,numerical_col),
            ('cat_pipeline',cat_pipeline,pipeline_col),
        ])
        
        save_obj(self.Transformed_data_path,processor)
        logging.info("Data Transformation pipeline object saved")
        return processor
    
    def initiate_data_transformation(self,train_data,test_data):
         
         categorical_col= train_data.columns[train_data.dtypes=='object']
         pipeline2_col = ['workclass','occupation']
         self.drop_columns(train_data,['Unnamed: 0','education','native-country'])
         self.drop_columns(test_data,['Unnamed: 0','education','native-country'])

       

         x_train = train_data.drop('class',axis=1)
         x_test = test_data.drop('class',axis=1)
         y_train = train_data['class']
         y_test = test_data['class']

        
         processor_obj = self.get_Transform_data_obj(x_train,test_data)
        
         logging.info("================Data Transformation Started==================")
         x_train=processor_obj.fit_transform(x_train)
         x_test=processor_obj.transform(x_test)


         logging.info("Transformed Train data sample==>")
         logging.info(pd.DataFrame(x_train).head(3))
         logging.info("Transformed Test data sample==>")
         logging.info(pd.DataFrame(x_test).head(3))
        
        #  self.drop_columns(x_train,categorical_col)

         logging.info("================Data Transformation succesful==================")
         return x_train,x_test,y_train,y_test




