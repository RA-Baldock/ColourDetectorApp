import pandas as pd
import numpy as np
import colorsys
import cv2

#df = pd.read_csv(r'D:\Colourhex.csv')
df = pd.read_csv('Colourhex.csv')

colour_string = ['blue', 'red', 'green', 'white', 'grey', 'yellow', 'pink', 'orange', 'purple', 'black']

final = []
for i in df['Name']:
    for j in colour_string:
        if j in i.lower():
            final.append(j)
            break
    else:
        final.append('Another colour')
print(final)

df['simple'] = final

other_colours = df.loc[df['simple'].str.contains('Another colour')]
simple_colours = df[df['simple'].isin(['blue', 'red', 'green', 'white',
                                       'grey', 'yellow', 'pink', 'orange', 'purple', 'black'])]



X = simple_colours[["Red (8 bit)", "Green (8 bit)", "Blue (8 bit)"]].values
y = simple_colours['simple']

from imblearn.over_sampling import RandomOverSampler
ros = RandomOverSampler(random_state=0)
X_resampled, y_resampled = ros.fit_resample(X, y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_resampled,y_resampled, test_size=0.2, random_state=0) #create training partition.

from sklearn.linear_model import LogisticRegression
model_log = LogisticRegression(max_iter=1000).fit(X_train, y_train)
y_pred = model_log.predict(X_test)

from sklearn.metrics import ConfusionMatrixDisplay
ConfusionMatrixDisplay.from_predictions(y_test, y_pred)

#Save and export the model----------
import pickle
filename = 'Logistic_model.sav'
pickle.dump(model_log, open(filename, 'wb'))
