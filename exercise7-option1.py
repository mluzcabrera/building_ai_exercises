import numpy as np

def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    seq = np.random.choice([0,1], p=[1-p1, p1], size=10000)
    return seq

def count(seq):
    res = 0
    # insert code to return the number of occurrences of 11111 in the sequence
    for i in range(10000-4):
        if seq[i]+seq[i+1]+seq[i+2]+seq[i+3]+seq[i+4] == 5:
            res = res+1
    return res 

def main(p1):
    seq = generate(p1)
    print(seq)
    return count(seq)

print(main(2/3))
