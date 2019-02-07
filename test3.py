
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

s = pd.read_csv('/Users/digvijayghotane/Desktop/codecell/datasets/lung-cancer-data.csv')
label = s['LUNG CANCER']
features = s.drop('LUNG CANCER', axis=1)
features_train, features_test, label_train, label_test = train_test_split(features, label, test_size = 0.3)
l=RandomForestClassifier(n_estimators=100)
l.fit(features_train,label_train)
o = l.predict(features_test)
print("Accuracy:",metrics.accuracy_score(label_test, o))