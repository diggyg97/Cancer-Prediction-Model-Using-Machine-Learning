import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
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
    gender = gender - 1
    age = int_check(18,123,"\nSecond Parameter:\n\nWhat is your age?\n\nPlease input your age (between 18-123, inclusive): ")
    age = age - 1
    smoking = int_check(1,2, "\nThird Paramenter:\n\nDo you smoke?\n1. No\n2. Yes\n\nPlease enter the integer corresponding to your smoking preference: ")
    smoking = smoking - 1
    fingers = int_check(1,2,"\nFourth Parameter:\n\nDo you have yellow Fingers?\n1. No\n2. Yes\n\nPlease enter the corresponding integer: ")
    fingers = fingers - 1
    anxiety = int_check(1,2,"\nFifth Parameter:\n\nHave you been medically diagnosed with anxiety?\n1. No\n2. Yes\n\nPlease enter the corresponding integer: ")
    anxiety = anxiety - 1
    peer_pressure = int_check(1,2,"\nSixth Parameter:\n\nAre you regularly peer pressured for smoking?\n1. No\n2. Yes\n\nPlease enter the corresponding integer: ")
    peer_pressure = peer_pressure - 1
    chronic = int_check(1,2,"\nSeventh Parameter:\n\nDo you suffer from any chronic illness?\n1. No\n2. Yes\n\nPlease enter the corresponding integer: ")
    chronic = chronic -1
    fatigue = int_check(1,2,"\nEighth Parameter:\n\nDo you suffer from fatigue all the time?\n1. No\n2. Yes\n\nPlease enter the corresponding integer: ")
    fatigue = fatigue - 1
    allergy = int_check(1,2,"\nNinth Parameter:\n\nDo you suffer from any allergies?\n1. No\n2. Yes\n\nPlease enter the corresponding integer: ")
    allergy = allergy - 1
    wheeze = int_check(1,2,"\nTenth Parameter:\n\nDo you wheeze?\n1. No\n2. Yes\n\nPlease enter the corresponding integer: ")
    wheeze = wheeze - 1
    alcohol = int_check(1,2,"\nEleventh Parameter:\n\nDo you consume alcohol?\n1. No\n2. Yes\n\nPlease enter the corresponding integer: ")
    alcohol = alcohol-1
    coughing = int_check(1,2,"\nTwelfth Parameter:\n\nDo you suffer from cough?\n1. No\n2. Yes\n\nPlease enter the corresponding integer: ")
    coughing=coughing-1
    breath = int_check(1,2,"\nThirteenth Parameter:\n\nDo you suffer from shortness of breath?\n1. No\n2. Yes\n\nPlease enter the corresponding integer: ")
    breath=breath-1
    swallow = int_check(1,2,"\nFourteenth Parameter:\n\nDo you have difficulty in swallowing?\n1. No\n2. Yes\n\nPlease enter the corresponding integer: ")
    swallow=swallow-1
    chest = int_check(1,2,"\nFifteenth Parameter:\n\nDo you suffer from chest pain?\n1. No\n2. Yes\n\nPlease enter the corresponding integer: ")
    chest=chest-1
    s = pd.read_csv('datasets/lung-cancer-data.csv')
    label = s['LUNG CANCER'].values
    features = s.drop('LUNG CANCER', axis=1).values
    features_train, features_test, label_train, label_test = train_test_split(features, label, test_size = 0.3)
    l = RandomForestClassifier(n_estimators=100)
    label_train = label_train.reshape(-1,1)
    label_test = label_test.reshape(-1,1)
    l.fit(features_train,label_train)
    o = l.predict_proba([[gender, age, smoking, fingers, anxiety, peer_pressure, chronic, fatigue, allergy, wheeze, alcohol, coughing, breath, swallow, chest]])
    return o,age,gender

#Function for insurance tracking.
def insurance_op(z,age,gender):
    e = pd.read_csv(z)
    for i in range(0,8):
        if e.iloc[i,0] <= age < e.iloc[i+1,0] and gender==1:
            print("\nThe premium on every ₹1,000 is ₹",round(e.iloc[i,1],2))
        elif e.iloc[i,0]<= age <e.iloc[i+1,0] and gender==2:
            print("\nThe premium on every ₹1,000 is ₹",round(e.iloc[i,2],2))
        elif age==60 and gender==1:
            print("\nThe premium on every ₹1,000 is ₹",round(e.iloc[8][1],2))
        elif age==60 and gender==2:
            print("\nThe premium on every ₹1,000 is ₹",round(e.iloc[8][2],2))

#Function for choice of procedure to cure cancer.
def cure_procedure():
    chemocat = int_check(1,2,"\nWhich procedure would you want to access?\n1. Chemotherapy\n2. Infusion\n\nPlease enter the corresponding integer: ")
    chemocat = chemocat - 1
    chemo_type = int_check(1,5,"\nWhich Treatment Type would you like to choose?\n\n1. Anthracycline\n2. Herceptin\n3. Immunotherapy\n4. Other\n5. Hormone\n\nPlease choose the corresponding integer: ")
    chemo_type = chemo_type - 1
    treatment = int_check(1,6,"\nWhich Treatment Type would you like to choose?\n\n1. Biology\n2. Chemotherapy\n3. Hormone\n4. Immunologic\n5. Other\n6. Radioactive\n\nPlease choose the corresponding integer: ")
    treatment = treatment - 1
    chemo_therapy = int_check(1,2,"\nDo you want chemotherapy?\n\n1. No\n2. Yes\n\nPlease choose the corresponding integer: ")
    chemo_therapy = chemo_therapy - 1
    s = pd.read_csv('datasets/procedure.csv')
    label = s['CURE']
    features = s.drop('CURE',axis=1)
    features_train, features_test, label_train, label_test = train_test_split(features, label, test_size = 0.3)
    l = RandomForestClassifier(n_estimators=100)
    l.fit(features_train,label_train)
    o = l.predict_proba([[chemocat,chemo_type,treatment,chemo_therapy]])
    return o

#Initial choice.
a = int_check(1,3,"\nAre you:\n\n1. A Person checking your likelihood of Cancer?\n2. An Insurance Company?\n3. A Medical Researcher?\n\nPlease choose the integer corresponding to the dataset you'd like to access: ")
if a==1: #Personal Use
    print("\nThis prediction model will predict the probability of the likelihood of you being affected by lung cancer. We will ask from you, a series of inputs, please input the corresponding values as per your need.")
    b,c,d = cancer_prob()
    print("You have a",round(float(b[:,1]),2)*100,"percent chance of getting cancer.")
elif a==2: #Insurance
    b = int_check(1,2,"\nPlease enter the amount of years you want the policy for:\n\n1. 20 years\n2. 30 years.\n\nPlease enter the corresponding integer: ")
    print("\n\nPlease fill in the details to the questions that are going to be asked to receive an appropriate plan for you.")
    c,d,e = cancer_prob()
    c=c[:,1]
    if 20<=d<=65:
        print("\nCongratulations, you're eligible for purchasing a policy! According to the information provided by you, these are the premium rates most conducive to you as per the policies offered by us.")
        if 0<=c<=50:
            print("\n\nThis is a low risk policy.")
            if b==1:
                insurance_op('datasets/20yr-low-risk.csv',d,e)
            elif b==2:
                insurance_op('datasets/30yr-low-risk.csv',d,e)
        elif 50<=c<=100:
            print("\n\nThis is a high risk policy.")
            if b==1:
                insurance_op('datasets/20yr-high-risk.csv',d,e)
            elif b==2:
                insurance_op('datasets/30yr-high-risk.csv',d,e)
    else:
        print("The client does not meet the age requirements for purchasing a policy.")
elif a==3: #Medical Researcher
    b = cure_procedure()
    print("You have a",round(float(b[:,1]),2)*100,"percent chance of curing cancer.")