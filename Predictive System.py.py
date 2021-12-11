# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
 
# LOADING THE SAVE MODEL
loaded_model = pickle.load(open("D:/ML PROJECT/Trained_model.sav", "rb"))    
 
input_data = (4,110,92,0,0,37.6,0.191,30)

# Changing the input_data into numpy array:-

input_data_as_numpy_array = np.asarray(input_data)

# Reshape the array as we are predicting for one instance:-

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1) # We are not giving 786 example we are giving only one exmple


Prediction = loaded_model.predict(input_data_reshaped)
print(Prediction)

if (Prediction[0] == 0):
    print("The Person Is Not Diabetic")
else:
    print("The Person Is Diabetic")