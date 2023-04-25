from flask import Flask,request,render_template,jsonify
from src.Pipeline.prediction_pipeline import custom_data,predict
import os 

TEMPLATE_DIR = os.path.abspath('../templates')
STATIC_DIR = os.path.abspath('../static')
app= Flask(__name__)

Application = app

@app.route("/",methods=['GET','POST'])
def Home_screen():
    if(request.method=='GET'):
      return render_template("form.html")

    else:
      custom_data_obj= custom_data(
        age = int(request.form.get('Age')),
        workclass=(request.form.get('workclass')),
        fnlwgt=int(request.form.get('fnlwgt')),
        education_num=int(request.form.get('Education Num')),
        marital_status=(request.form.get('Marital status')),
        occupation=(request.form.get('Occupation')),
        relationship=(request.form.get('relationship')),
        race=(request.form.get('Race')),
        sex=(request.form.get('Sex')),
        capital_gain=int(request.form.get('capital-gain')),
        capital_loss=int(request.form.get('capital-loss')),
        hours_per_week=int(request.form.get('hours-per-week')),
       )
      
      transformed_data=custom_data_obj.get_data_in_df()
      print("==========")
      print(transformed_data)
      print("==========")
      predict_obj =predict()
      result= predict_obj.predict(transformed_data)
      if (result==[0]):
         result='<=50k'
      else:
         result='>50k'
      return render_template('result.html',final_result=result)


if __name__=="__main__":
   app.run(host="0.0.0.0",port=5000)