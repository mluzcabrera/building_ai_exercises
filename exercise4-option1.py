import random

def main():
    
    #Write a program that prints "I love" followed by one word: 
    #the additional word should be 'dogs' with 80% probability, 
    #'cats' with 10% probability, and 'bats' with 10% probability.
    val = random.random()
    if val < 0.1:
        favourite = "bats"  # change this
    elif val < 0.2:
        favourite = "cats"    
    else:
        favourite = "dogs"
        
    print("I love " + favourite) 
    
main()
