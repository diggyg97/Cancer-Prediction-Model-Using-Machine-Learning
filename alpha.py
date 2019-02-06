import pandas as pd
from sklearn import linear_model
import numpy as np
from flask import Flask
from sklearn.linear_model import LogisticRegression

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

#Function to know lung cancer probability.
def cancer_prob():
    gender = int_check(1,2,"\n\nFirst Parameter:\n\nWhat is your gender?\n1. Female\n2. Male\n\nPlease Enter an integer corresponding to your choice: ")
    age = int_check(18,123,"\nSecond Parameter:\n\nWhat is your age?\n\nPlease input your age (between 18-123, inclusive): ")
    smoking = int_check(1,2, "\nThird Paramenter:\n\nDo you smoke?\n1. No\n2. Yes\n\nPlease enter the integer corresponding to your smoking preference: ")
    fingers = int_check(1,2,"\nFourth Parameter:\n\nDo you have yellow Fingers?\n1. No\n2. Yes\n\nPlease enter the corresponding integer: ")
    anxiety = int_check(1,2,"\nFifth Parameter:\n\nHave you been medically diagnosed with anxiety?\n1. No\n2. Yes\n\nPlease enter the corresponding integer: ")
    peer_pressure = int_check(1,2,"\nSixth Parameter:\n\nAre you regularly peer pressured for smoking?\n1. No\n2. Yes\n\nPlease enter the corresponding integer: ")
    chronic = int_check(1,2,"\nSeventh Parameter:\n\nDo you suffer from any chronic illness?\n1. No\n2. Yes\n\nPlease enter the corresponding integer: ")
    fatigue = int_check(1,2,"\nEighth Parameter:\n\nDo you suffer from fatigue all the time?\n1. No\n2. Yes\n\nPlease enter the corresponding integer: ")
    allergy = int_check(1,2,"\nNinth Parameter:\n\nDo you suffer from any allergies?\n1. No\n2. Yes\n\nPlease enter the corresponding integer: ")
    wheeze = int_check(1,2,"\nTenth Parameter:\n\nDo you wheeze?\n1. No\n2. Yes\n\nPlease enter the corresponding integer: ")
    alcohol = int_check(1,2,"\nEleventh Parameter:\n\nDo you consume alcohol?\n1. No\n2. Yes\n\nPlease enter the corresponding integer: ")
    coughing = int_check(1,2,"\nTwelfth Parameter:\n\nDo you suffer from cough?\n1. No\n2. Yes\n\nPlease enter the corresponding integer: ")
    breath = int_check(1,2,"\nThirteenth Parameter:\n\nDo you suffer from shortness of breath?\n1. No\n2. Yes\n\nPlease enter the corresponding integer: ")
    swallow = int_check(1,2,"\nFourteenth Parameter:\n\nDo you have difficulty in swallowing?\n1. No\n2. Yes\n\nPlease enter the corresponding integer: ")
    chest = int_check(1,2,"\nFifteenth Parameter:\n\nDo you suffer from chest pain?\n1. No\n2. Yes\n\nPlease enter the corresponding integer: ")
    s = pd.read_csv('/Users/digvijayghotane/Desktop/codecell/datasets/lung-cancer-data.csv')
    label = s['LUNG CANCER']
    features = s.drop('LUNG CANCER', axis=1)
    l = linear_model.LinearRegression()
    l.fit(features,label)
    o = l.predict([[gender, age, smoking, fingers, anxiety, peer_pressure, chronic, fatigue, allergy, wheeze, alcohol, coughing, breath, swallow, chest]])
    o = float(o)
    o=(o-1)*100
    if o>100:
        o=100
    return o,age,gender

#Function for insurance tracking.
def insurance_op(z,age,gender):
    e = pd.read_csv(z)
    for i in range(0,8):
        if e.iloc[i,0] <= age < e.iloc[i+1,0] and gender==1:
            print("The premium on every ₹1,000 is ₹",round(e.iloc[i,1],2))
        elif e.iloc[i,0]<= age <e.iloc[i+1,0] and gender==2:
            print("The premium on every ₹1,000 is ₹",round(e.iloc[i,2],2))
        elif age==60 and gender==1:
            print("The premium on every ₹1,000 is ₹",round(e.iloc[8][1],2))
        elif age==60 and gender==2:
            print("The premium on every ₹1,000 is ₹",round(e.iloc[8][2],2))

#Initial choice.
a = int_check(1,4,"\nAre you:\n\n1. A Person checking your likelihood of Cancer?\n2. An Insurance Company?\n3. A Medical Researcher?\n4. A Pharmaceutical Company?\n\nPlease choose the integer corresponding to the dataset you'd like to access: ")

if a==1: #Personal Use
    print("\nThis prediction model will predict the probability of the likelihood of you being affected by lung cancer. We will ask from you, a series of inputs, please input the corresponding values as per your need.")
    b,c,d = cancer_prob()
    print("You have a",round(b,2),"percent chance of getting cancer.")
elif a==2: #Insurance
    b = int_check(1,2,"\nPlease enter the amount of years you want the policy for:\n\n1. 20 years\n2. 30 years.\n\nPlease enter the corresponding integer: ")
    print("\n\nPlease fill in the details to the questions that are going to be asked to receive an appropriate plan for you.")
    c,d,e = cancer_prob()
    if 20<=d<=65:
        print("\nCongratulations, you're eligible for purchasing a policy! According to the information provided by you, these are the premium rates most conducive to you as per the policies offered by us.")
        if 0<=c<=50:
            print("This is a low risk policy.")
            if b==1:
                insurance_op('/Users/digvijayghotane/Desktop/codecell/datasets/20yr-low-risk.csv',d,e)
            elif b==2:
                insurance_op('/Users/digvijayghotane/Desktop/codecell/datasets/30yr-low-risk.csv',d,e)
        elif 50<c<=100:
            print("This is a high risk policy.")
            if b==1:
                insurance_op('/Users/digvijayghotane/Desktop/codecell/datasets/20yr-high-risk.csv',d,e)
            elif b==2:
                insurance_op('/Users/digvijayghotane/Desktop/codecell/datasets/30yr-high-risk.csv',d,e)
    else:
        print("The client does not meet the age requirements for purchasing a policy.")
elif a==3:
    print("Yet to code.")
elif a==4:
    print("Yet to code.")