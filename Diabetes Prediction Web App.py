# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 21:20:28 2021

@author: lenovo
"""

import numpy as np
import pickle
import streamlit as st
from PIL import Image

# LOADING THE SAVE MODEL
loaded_model = pickle.load(open("D:/ML PROJECT/Trained_model.sav", "rb"))

#Creating a Function for Prediction.

def Diabetes_Prediction(input_data):

    # Changing the input_data into numpy array:-

    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the array as we are predicting for one instance:-

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1) # We are not giving 786 example we are giving only one exmple


    Prediction = loaded_model.predict(input_data_reshaped)
    print(Prediction)

    if (Prediction[0] == 0):
        return "The Person Is Not Diabetic"
    else:
        return "The Person Is Diabetic"


def main():
    
    #Giving a Title To Our Web Page.
    st.title("Diabetes Prediction Web App")

    #Getting input data from the user.
    
    pregnant = st.text_input("Number Of Times Pregnancies")
    glocose = st.text_input("Glucose Level")
    bp = st.text_input("Blood Pressure Value")
    skin = st.text_input("Skin Thickness Value")
    insulin = st.text_input("Insulin Level")
    bmi = st.text_input("BMI Value")
    predigree = st.text_input("Diabetes Pedigree Function Value")
    age = st.text_input("Age Of The Person")
    
    
    #Code For Prediction:-
    Diagnosis = " "

    # Creating a Button For Prediction:-
    if st.button("Diabetes Test Result"):
        Diagnosis = Diabetes_Prediction([pregnant, glocose, bp, skin, insulin, bmi, predigree, age])
    
    st.success(Diagnosis)

if __name__ == "__main__":
    main()
        