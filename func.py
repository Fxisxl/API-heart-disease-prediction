import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

import pickle
with open('heart_disease.pkl', 'rb') as file:
    loaded_model = pickle.load(file)


# predictions = loaded_model.predict()
# input  = (62,0,0,140,268,0,0,160,0,3.6,0,2,2)
# input = (56,1,1,120,236,0,1,178,0,0.8,2,0,2)

def predict (input_data):
    #converting the input inyo np array
    input_data_as_numpy_array= np.asarray(input_data)

    #reshaping the np array data
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    # print(prediction)

    if (prediction[0]== 0):
        prediction = 'The Person does not have a Heart Disease'
    else:
        prediction ='The Person has Heart Disease'

    return {
        'prediction':prediction
    }


# predict(input)