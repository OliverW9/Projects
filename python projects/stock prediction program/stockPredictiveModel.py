import csv # get it explained line by line!!!!!!!!!!!!!!!!
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

dates = []
price = []

def get_data(filename):

    rows = []

    with open(filename, 'r') as csvfile:
        csvfileReader = csv.reader(csvfile)
        next(csvfileReader)

        for row in csvfileReader:
            rows.append(row)

            #reverses the rows so oldest date is now first
        rows.reverse()

        for row in rows:
            dates.append(len(dates) + 1)
            price.append(float(row[1]))

def predict_prices(dates, prices, x):
    dates = np.reshape(dates,(len(dates), 1))

    svr_lin = SVR(kernel= 'linear', C=1e3)
    svr_poly = SVR(kernel= 'poly', C=1e3, degree = 2)
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
    svr_lin.fit(dates, prices)
    svr_poly.fit(dates, prices)
    svr_rbf.fit(dates, prices)

    plt.scatter(dates, prices, color='black', label='data')
    plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')
    plt.plot(dates, svr_lin.predict(dates), color='green', label='Linear model')
    plt.plot(dates, svr_poly.predict(dates), color='blue', label='Polynomial model')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Support Vector Regression')
    plt.legend()
    plt.show()

    x = np.array([[x]])

    return (svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0])

def pick_stock():

    while True:

        stock_choice = input("what stock would you like to predict Apple(a) or Meta(m):")

        if stock_choice == "m":
            get_data('meta.csv')
            break

        elif stock_choice == "a":
            get_data('appl.csv')
            break

        else:
            print("ERROR invalid stock choice")

pick_stock()

predictedPrice = predict_prices(dates, price, len(dates)+1)

print(f"RBF Prediction: ${predictedPrice[0]:.2f}")
print(f"Linear Prediction: ${predictedPrice[1]:.2f}")
print(f"Polynomial Prediction: ${predictedPrice[2]:.2f}")