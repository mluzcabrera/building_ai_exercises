# input values for three mökkis: size, size of sauna, distance to water, number of indoor bathrooms, 
# proximity of neighbors
X = [[66, 5, 15, 2, 500], 
     [21, 3, 50, 1, 100], 
     [120, 15, 5, 2, 1200]]
c = [3000, 200, -50, 5000, 100]    # coefficient values

def predict(X, c):
    prices = []            
    for i in range(len(X)):
        price = 0
        for j in range(len(X[i])):
            price = price + X[i][j]*c[j]
        print(price)
        #prices.append(price)
    #print(prices)

predict(X, c)
