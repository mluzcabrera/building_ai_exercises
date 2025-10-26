import numpy as np
from io import StringIO

train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''

def main():
    np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
    
    # Please write your code inside this function
    training_file = StringIO(train_string)
    training_data = np.genfromtxt(training_file)
    
    test_file = StringIO(test_string)
    test_data = np.genfromtxt(test_file)
    
    # Features are all columns except the last; target is the last column
    X = training_data[:, :-1]
    y = training_data[:, -1]
    
    X2 = test_data[:, :-1]
    y2 = test_data[:, -1]
    
    # Least-squares fit: minimizes sum of squared errors
    c, *_ = np.linalg.lstsq(X, y, rcond=None)
    
    # Predicted prices for the test data
    y_hat = X2 @ c

    print(c)      # coefficients (intercept first, then one per feature)
    print(y_hat)  # fitted prices

main()
    

    

    

    

    

