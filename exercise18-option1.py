# DATA BLOCK

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

import math
import numpy as np

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

def main(text):
    
    # tasks your code should perform:

    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal 
    # despite casing) can be done with 
    # docs = [line.lower().split() for line in text.split('\n')]

    # 2. go over each unique word and calculate its term frequency, and its document frequency

    # 3. after you have your term frequencies and document frequencies, go over each line in the text and 
    # calculate its TF-IDF representation, which will be a vector

    # split the text first into lines and then into lists of words
    docs = [line.split() for line in text.splitlines()]

    N = len(docs)

    # create the vocabulary: the list of words that appear at least once
    vocabulary = list(set(text.split()))

    df = {}
    tf = {}
    for word in vocabulary:
        # tf: number of occurrences of word w in document divided by document length
        # note: tf[word] will be a list containing the tf of each word for each document
        # for example tf['he'][0] contains the term frequence of the word 'he' in the first
        # document
        tf[word] = [doc.count(word)/len(doc) for doc in docs]

        # df: number of documents containing word w
        df[word] = sum([word in doc for doc in docs])/N

    tfidfs = []
    # loop through documents to calculate the tf-idf values
    for doc_index, doc in enumerate(docs):
        tfidf = []
        for word in vocabulary:
            # ADD THE CORRECT FORMULA HERE. Remember to use the base 10 logarithm: math.log(x, 10)
            if df[word] > 0:
                tfidf_value = tf[word][doc_index] * math.log(N / (df[word] * N), 10)
            else:
                tfidf_value = 0
            tfidf.append(tfidf_value) 

        #print(tfidf)
        tfidfs.append(tfidf)
    #print(tfidfs)    
    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.
    find_nearest_pair(tfidfs)

main(text)
