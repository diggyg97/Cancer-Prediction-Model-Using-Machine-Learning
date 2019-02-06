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
    s = pd.read_csv('/Users/digvijayghotane/Downloads/USCS_1999_2015_ASCII/BYAGE.txt',delimiter='|')
    print(s)
elif a==2:
    print("u noob")
elif a==3:
    print("u noob")
elif a==4:
    print("u noob")