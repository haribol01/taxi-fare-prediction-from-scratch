import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('chicago_taxi_train.csv')

relations = []
features = []

# Correlation between different features and FARE
for i in data.columns:
    if data[i].dtype == 'float64' or data[i].dtype == 'int64':
        correlation = data[i].corr(data['FARE'])
        relations.append(correlation)
        features.append(i)

plt.plot(features, relations)
plt.show()

# We got highest correlation with TRIP_MILES and TRIP_SECONDS