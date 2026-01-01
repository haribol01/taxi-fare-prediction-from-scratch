import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('chicago_taxi_train.csv')

x = (data['TRIP_MILES'] - data['TRIP_MILES'].mean()) / data['TRIP_MILES'].std()
x2 = (data['TRIP_SECONDS'] - data['TRIP_SECONDS'].mean()) / data['TRIP_SECONDS'].std()
y = data['FARE']

# Parameters for linear regression
m = 0.0
m2 = 0.0
c = 0.0
L = 0.01  # Learning Rate

# Number of iterations for gradient descent
epochs = 1000
n = float(len(data))

for epoch in range(epochs):
    Y_pred = m * x + m2 * x2 + c
    m += L * (-1/n) * ((Y_pred - y)*x).sum()
    m2 += L * (-1/n) * ((Y_pred - y)*x2).sum()
    c += L * (-1/n) * (Y_pred - y).sum()

def plot_regression_line(x_t, x2_t, y_t):
    plt.scatter(x_t, y_t, alpha=0.3)
    normalised_x = (x_t - data['TRIP_MILES'].mean()) / data['TRIP_MILES'].std()
    normalised_x2 = (x2_t - data['TRIP_SECONDS'].mean()) / data['TRIP_SECONDS'].std()
    plt.plot(x_t, m*normalised_x + m2*normalised_x2 + c, color='red')
    plt.xlabel("Trip Miles")
    plt.ylabel("Fare")
    plt.show()

def test_regression():
    test_data = pd.read_csv('test_data.csv')
    plot_regression_line(test_data['TRIP_MILES'], test_data['TRIP_SECONDS'], test_data['FARE'])

test_regression()

isRunning = True

while isRunning:
    trip_miles = float(input("Enter trip miles: "))
    trip_seconds = float(input("Enter trip seconds: "))
    fare_prediction = m * ((trip_miles - data['TRIP_MILES'].mean()) / data['TRIP_MILES'].std()) + m2 * ((trip_seconds - data['TRIP_SECONDS'].mean()) / data['TRIP_SECONDS'].std()) + c
    print(f"Predicted Fare: ${fare_prediction:.2f}")
    cont = input("Do you want to predict another fare? (yes/no): ").strip().lower()
    if cont != 'yes':
        isRunning = False