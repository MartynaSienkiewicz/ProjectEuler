# Solution to Project Euler problem 1 - multiples of 3 or 5

# Problem: If we list all the natural numbers below  10  that are multiples of  3  or  5 , 
# we get  3 , 5 , 6  and  9 . The sum of these multiples is  23 .  
# Find the sum of all the multiples of  3  or  5  below  1000 .
# Below 1000 suggests exclusive 

import numpy as np

natnum_list = np.arange(1,1000,1) # produce list of natural numbers below 1000

multiples = [] # empty list for storing multiples later

for num in natnum_list:
    if num % 3 == 0 or num % 5 == 0:
        multiples.append(num)

ans = sum(multiples)
print(ans)
