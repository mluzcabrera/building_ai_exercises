import random

   x = random.random()
   if x < 0.8:
      favourite = "dogs"
   elif x < 0.9:
      favourite = "cats"
   else:
      favourite = "bats"
      
   print("I love " + favourite)
