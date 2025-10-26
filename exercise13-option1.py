import numpy as np
from io import StringIO

input_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
 
def fit_model(input_file):
    # Please write your code inside this function
    data = np.genfromtxt(input_file)
    
    # Features are all columns except the last; target is the last column
    X = data[:, :-1]
    y = data[:, -1]
    
    # Least-squares fit: minimizes sum of squared errors
    c, *_ = np.linalg.lstsq(X, y, rcond=None)
    
    # Fitted (predicted) prices for the training data
    y_hat = X @ c

    print(c)      # coefficients (intercept first, then one per feature)
    print(y_hat)  # fitted prices

    #'[2989.6 800.6 -44.8 3890.8 99.8]\n[127[47 chars]9.9]'

# simulate reading a file
input_file = StringIO(input_string)
fit_model(input_file)
