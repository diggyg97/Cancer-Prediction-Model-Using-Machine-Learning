import pandas as pd
import sklearn as sk
from sklearn import linear_model

s = pd.read_csv('/Users/digvijayghotane/Desktop/codecell/lung-cancer-data.csv')
label = s['LUNG CANCER']
features = s.drop('LUNG CANCER', axis=1)

l = linear_model.LinearRegression()
l.fit(features,label)
print l.predict([[gender, age, smoking, fingers, anxiety, peer_pressure, chronic, fatigue, allergy, wheeze, alcohol, coughing, breath, swallow, chest]]).tolist()