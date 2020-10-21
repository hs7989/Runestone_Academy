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


