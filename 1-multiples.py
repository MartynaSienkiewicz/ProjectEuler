# Solution to Project Euler problem 1 - multiples of 3 or 5

# Problem: If we list all the natural numbers below  10  that are multiples of  3  or  5 , 
# we get  3 , 5 , 6  and  9 . The sum of these multiples is  23 .  
# Find the sum of all the multiples of  3  or  5  below  1000 .
# Below 1000 suggests exclusive 

multiples = []  

for x in range(1000):              # iterating through each number in the range 0 to 999
    if x % 3 == 0 or x % 5 == 0:   # checking if number is a multiple of 3 or 5
        multiples.append(x)
    
ans = sum(multiples)               # calculating the sum
print(ans)
