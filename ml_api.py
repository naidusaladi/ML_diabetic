# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 12:08:47 2022

@author: DELL
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json

app=FastAPI()

origins=["*"]
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

class model_input(BaseModel):
    
    Pregnancies:int
    Glucose:int
    BloodPressure:int
    SkinThickness:int
    Insulin:int
    BMI:float
    DiabetesPedigreeFunction:float
    Age:int

#loding the saved model
diabetes_model=pickle.load(open('diabetes_model (3).sav','rb'))

@app.post('/diabetes_prediction')

def diabetes_pred(input_parameters:model_input):
    input_data=input_parameters.json()
    input_dictionary=json.loads(input_data)
    preg=input_dictionary['Pregnancies']
    glu=input_dictionary['Glucose']
    blp=input_dictionary['BloodPressure']
    skn=input_dictionary['SkinThickness']
    insu=input_dictionary['Insulin']
    bmi=input_dictionary['BMI']
    dipf=input_dictionary['DiabetesPedigreeFunction']
    age=input_dictionary['Age']
    
    input_list=[preg,glu,blp,skn,insu,bmi,dipf,age]
    
    prediction = diabetes_model.predict([input_list])
    return str([preg,glu,blp,skn,insu,bmi,dipf,age])
    if(prediction[0]==1):
        return '0'
    else:
        return 'The person is not Diabetic'
    
    

