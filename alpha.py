import pandas as pd
from sklearn import linear_model
import numpy as np

#Function to check for valid input.
def int_check(l,h,message):
    while True:
        s = input(message)
        if s.isdigit():
            s=int(s)
            if l<=s<=h:
                return s
            else:
                print("\nError in input, please try again.")
        else:
            print("\nError in input, please try again.")

#Initial choice.
a = int_check(1,4,"\nAre you:\n\n1. A Person looking for likelihood of Cancer?\n2. An Insurance Company?\n3. A Medical Researcher?\n4. A Pharmaceutical Company?\n\nPlease choose the integer corresponding to the dataset you'd like to access: ")

if a==1:
    gender = int_check(1,2,"\nThis prediction model will predict the probability of the likelihood of you being affected by lung cancer. We will ask from you, a series of inputs, please input the corresponding values as per your need.\n\nFirst Parameter:\nWhat is your gender?\n1. Female\n2. Male \n\nPlease Enter an integer corresponding to your choice: ")
    age = int_check(18,123,"\nSecond Parameter:\nWhat is your age?\nPlease input your age (between 18-123, inclusive): ")
    smoking = int_check(1,2, "\nThird Paramenter:\nDo you smoke?\n1. No\n2. Yes\nPlease enter the integer corresponding to your smoking preference: ")
    fingers = int_check(1,2,"\nFourth Parameter:\nDo you have yellow Fingers?\n1. No\n2. Yes\nPlease enter the corresponding integer: ")
    anxiety = int_check(1,2,"\nFifth Parameter:\nHave you been medically diagnosed with anxiety?\n1. No\n2. Yes\nPlease enter the corresponding integer: ")
    peer_pressure = int_check(1,2,"\nSeventh Parameter:\nAre you regularly peer pressured for smoking?\n1. No\n2. Yes\nPlease enter the corresponding integer: ")
    chronic = int_check(1,2,"\nEighth Parameter:\nDo you suffer from any chronic illness?\n1. No\n2. Yes\nPlease enter the corresponding integer: ")
    fatigue = int_check(1,2,"\nNinth Parameter:\nDo you suffer from fatigue all the time?\n1. No\n2. Yes\nPlease enter the corresponding integer: ")
    allergy = int_check(1,2,"\nTenth Parameter:\nDo you suffer from any allergies?\n1. No\n2. Yes\nPlease enter the corresponding integer: ")
    wheeze = int_check(1,2,"\nEleventh Parameter:\nDo you wheeze?\n1. No\n2. Yes\nPlease enter the corresponding integer: ")
    alcohol = int_check(1,2,"\nTwelfth Parameter:\nDo you consume alcohol?\n1. No\n2. Yes\nPlease enter the corresponding integer: ")
    coughing = int_check(1,2,"\nThirteenth Parameter:\nDo you suffer from cough?\n1. No\n2. Yes\nPlease enter the corresponding integer: ")
    breath = int_check(1,2,"\nFourteenth Parameter:\nDo you suffer from shortness of breath?\n1. No\n2. Yes\nPlease enter the corresponding integer: ")
    swallow = int_check(1,2,"\nFifteenth Parameter:\nDo you have difficulty in swallowing?\n1. No\n2. Yes\nPlease enter the corresponding integer: ")
    chest = int_check(1,2,"\nSixteenth Parameter:\nDo you suffer from chest pain?\n1. No\n2. Yes\nPlease enter the corresponding integer: ")
    s = pd.read_csv('/Users/digvijayghotane/Desktop/codecell/lung-cancer-data.csv')
    label = s['LUNG CANCER']
    features = s.drop('LUNG CANCER', axis=1)
    l = linear_model.LinearRegression()
    l.fit(features,label)
    o = l.predict([[gender, age, smoking, fingers, anxiety, peer_pressure, chronic, fatigue, allergy, wheeze, alcohol, coughing, breath, swallow, chest]])
    o=float(o)
    o=(o-1)*100
    print("You have a",o,"percent chance of getting cancer.")
    
elif a==2:
    print("Yet to code.")
elif a==3:
    print("Yet to code.")
elif a==4:
    print("Yet to code.")