""" Use a for statement to print 10 random numbers."""

import random
for i in range(10):
    x = random.random()
    print(x)

"""Repeat the above exercise but this time print 10 
random numbers between 25 and 35."""

import random
for i in range(10):
    x = random.randrange(25,36)
    print(x)

"""In statistical physics, it is common to use Stirling’s approximation for 𝑁!,

𝑁!≈𝑁𝑁𝑒−𝑁2𝜋𝑁‾‾‾‾‾√.
Obtain an integer from the user, assign it to N, and print out, in order, 𝑁!, Stirling’s approximation, and the relative percent error. The relative percent error is calculated as

error=∣∣∣approx−exact/exact∣∣∣100%.
"""

import math
N = int(input("Enter a number"))
factorial = 1

for x in range(1,N+1):
    factorial = factorial*x
print(factorial)

Exact = (N**N)*math.exp(N*(-1))*math.sqrt(2 * math.pi * N)
print(Exact)

error = ((factorial - Exact)/Exact)*100
print(error)


"""For a right triangle we have

tan(𝜃)=opp𝑎𝑑𝑗
Compute and print 𝜃 for

(opp=1,adj=1),(opp=1,adj=−1),(opp=−1,adj=1),and(opp=−1,adj=−1)."""


import math

print(math.atan2(1,1))
print(math.atan2(1,-1))
print(math.atan2(-1,1))
print(math.atan2(-1,-1))

"""Use the double angle formula,

sin(2𝜃)=2sin(𝜃)cos(𝜃),
to compute and print

sin(𝜋/4)"""

import math
x=math.pi/4

print((math.sin(2*(x))/math.cos(x))/2)



"""Write a program to print an n*n times table. n could be any number. For example, the following is a 5*5 times table:

1 x 1 = 1

1 x 2 = 2 2 x 2 = 4

1 x 3 = 3 2 x 3 = 6 3 x 3 = 9

1 x 4 = 4 2 x 4 = 8 3 x 4 = 12 4 x 4 = 16

1 x 5 = 5 2 x 5 = 10 3 x 5 = 15 4 x 5 = 20 5 x 5 = 25"""

First_number = int(input("Insert first number"))
Second_number = int(input("Insert second number"))

for i in range(1,First_number+1):
    for j in range(1, i+1, 1):
        print(str(j)+"x"+str(i)+"="+str(i*j),end=' ')
    print("\n")


"""Write a Python program to print 10 random integers between 1 and 100, 
inclusive. Print one random integer per line. Use a loop. I have started the program for you."""

import random

for i in range(1,11):
    print(random.randint(1,101))


