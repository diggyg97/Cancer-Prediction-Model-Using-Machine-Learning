import pandas as pd
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

def csv_display(directory,index,z):
    s = pd.read_csv(directory)
    print(s)
    o = int_check(1,2,"\nWould you like to predict future values?\n\n1. Yes\n2. No\n\nChoose a corresponding number: ")
    if o==1:
        n = int_check(0,36,'\nWhich one of the following places would you like to predict the future values for?\n\n{}\n\nPlease choose the corresponding integer: '.format(s.iloc[:,0].to_string()))
        i=0
    return s

a = int_check(1,4,"\nAre you:\n\n1. A Person looking for likelihood of Cancer?\n2. An Insurance Company?\n3. A Medical Researcher?\n4. A Pharmaceutical Company?\n\nPlease choose the integer corresponding to the dataset you'd like to access: ")
if a==1:
    gender = int_check(1,3,"\nThis prediction model will predict the probability of the likelihood of you being affected by lung cancer. We will ask from you, a series of inputs, please input the corresponding values as per your need.\n\nFirst Parameter:\nWhat is your gender?\n1. Female\n2. Male\n3. Other\n\nPlease Enter an integer corresponding to your choice: ")
    age = int_check(1,10,"\nSecond Parameter:\nWhat age group do you belong to?:\n1. 18-40\n2. 40-45\n3. 45-50\n4. 50-55\n5. 55-60\n6. 60-65\n7. 65-70\n8. 70-75\n9. 75-80\n10. 80+\nPlease enter the integer corresponding to your age group: ")
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
elif a==2:
    print("u noob")
elif a==3:
    print("u noob")
elif a==4:
    print("u noob")