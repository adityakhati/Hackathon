import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier             # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split        # Import train_test_split function
from sklearn import metrics                                 # Import scikit-learn metrics module for accuracy calculation
from sklearn.metrics import f1_score

features = pd.read_csv('train data.csv')
test = pd.read_csv('test data.csv')

feature_cols = ['shp_type_indicator_fg','transport_group_cd', 
 'carrier_type_cd','creation_dt','shipping_condition_cd','temp_condition_cd','temp_channel_cd']

X = features[feature_cols]

# Features
y = features['hit_or_miss'] 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)  # 70% training and 30% test


# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

# Predict the response for test dataset
y_pred = clf.predict(X_test)


y_test1 = clf.predict(test[feature_cols])

check_df = pd.DataFrame({'shipment number':test['shipment number'],'hit_or_miss': y_test1})
check_df.to_csv('INNOVATE501.csv')

score = f1_score(y_pred, y_test)
print ("Decision Tree F1 score: {:.2f}".format(score))

