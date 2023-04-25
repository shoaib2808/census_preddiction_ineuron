import pandas as pd
import numpy as np
import os
from src.utils import load_obj

class custom_data:
    def __init__(self,age,workclass,fnlwgt,education_num,marital_status,occupation,relationship,race,sex,capital_gain,capital_loss,hours_per_week):
        self.age=age
        self.workclass=workclass
        self.fnlwgt=fnlwgt
        self.education_num=education_num
        self.marital_status=marital_status
        self.occupation=occupation
        self.relationship=relationship
        self.race=race
        self.sex=sex
        self.capital_gain=capital_gain
        self.capital_loss=capital_loss
        self.hours_per_week=hours_per_week


    def get_data_in_df(self):
        dictinary = {'age':[self.age],
                    'workclass':[self.workclass],
                    'fnlwgt':[self.fnlwgt],
                    'education-num':[self.education_num],
                    'marital-status':[self.marital_status],
                    'occupation':[self.occupation],
                    'relationship':[self.relationship],
                    'race':[self.race],
                    'sex':[self.sex],
                    'capital-gain':[self.capital_gain],
                    'capital-loss':[self.capital_loss],
                    'hours-per-week':[self.hours_per_week]

                      }
        print(dictinary)
        df=pd.DataFrame(dictinary)
        return df 




class predict:

    def predict(self,df):
            preprocessor_path=os.path.join('Artifacts','processor.pkl')
            model_path=os.path.join('Artifacts','Model.pkl')

            proceesor=load_obj(preprocessor_path)
            model=load_obj(model_path)
            print("==========")
            print(df)
            print("==========")
            # transformed_data=proceesor.fit([df])
            # proceesor.fit(df)
            transformed_data=proceesor.transform(df)

            print("==========")
            print(transformed_data)
            print("==========")
            result=model.predict(transformed_data)

            return result

