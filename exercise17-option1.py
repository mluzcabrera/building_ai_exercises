import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]
        
def calc_dist(v1,v2):
    res = 0
    for i in range(len(v1)):
        res = res + abs(v1[i]-v2[i])
    
    return res
        
#Your task is to write a program that calculates the distances (or differences) 
#between every pair of lines in the This Little Piggy rhyme and finds the most similar pair. 
#Use the Manhattan distance (also called Taxicab distance) as your distance metric.

def find_nearest_pair(data):
    N = len(data)
    
    #You can start by building a numpy array to store all the distances. 
    #Notice that the diagonal elements in the array (elements at positions [i, j] with i=j) 
    #will be equal to zero. 
    dist = np.empty((N, N), dtype=float)
    
    for i in range(N):
        for j in range(N):
            if i == j:
                dist[i,j] = np.inf
            else:
                dist[i,j] = calc_dist(data[i],data[j])    
    
    #A quick way to get the index of the element with the lowest value in a 2D array 
    #(or in fact, any dimension) is by the function
    print(np.unravel_index(np.argmin(dist), dist.shape))

find_nearest_pair(data)
