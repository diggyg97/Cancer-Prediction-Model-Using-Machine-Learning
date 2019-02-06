import pandas as pd
#low risk 20 yr
def insurance_op(z,age,gender)
e = pd.read_csv(z)
for i in range(0,8):
    if e.iloc[i,0] <= age < e.iloc[i+1,0] and gender==1:
       print(e.iloc[i,1])
    elif e.iloc[i,0]<= age <e.iloc[i+1,0] and gender==2:
        print(e.iloc[i,2])
    elif age==60 and gender==1:
        print(e.iloc[8][1])
    elif age==60 and gender==2:
        print(e.iloc[8][2])