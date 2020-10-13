"""Challenge: Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
Write a Python program to solve the general version of the above problem.
Ask the user for the time now (in hours), and then ask for the number of hours to wait for the alarm.
Your program should output what the time will be on the clock when the alarm goes off."""

Present_time = int(input("what is present time:"))
Hours_to_add = int(input("hours from now to get notification: "))
Total_time = Present_time + Hours_to_add
time = Total_time % 24
print(time)

"""It is possible to name the days 0 thru 6 where day 0 is Sunday and day 6 is Saturday. 
If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home 
after 10 nights you would return home on a Saturday (day 6). Write a general version of the 
program which asks for the starting day number, and the length of your stay, and it will tell 
you the number of day of the week you will return on."""

Start_day = int(input("Enter the start date"))
Returning_after = int(input("Enter days after you will return"))

Day_of_return = (Start_day + Returning_after) % 7

print(Day_of_return)

"""Challenge: Take the sentence: All work and no play makes Jack a dull boy. 
Store each word in a separate variable, then print out the sentence on one line using print."""

W1 = "All"
W2 = "work"
W3 = "and"
W4 = "no"
W5 = "play"
W6 = "makes"
W7 = "Jack"
W8 = "a"
W9 = "dull"
W10 = "boy."

print(W1 + " " + W2 + " " + W3 + " " + W4 + " " + W5 + " " + W6 + " " + W7 + " " + W8 + " " + W9 + " " + W10)

"""Add parentheses to the expression 6 * 1 - 2 to change its value from 4 to -6."""
print(6 * (1 - 2))

"""Write a Python program that assigns the principal amount of 10000 to variable P, 
assign to n the value 12, and assign to r the interest rate of 8% (0.08). Then have 
the program prompt the user for the number of years, t, that the money will be compounded 
for. Calculate and print the final amount after t years."""

P = 10000
n = 12
r = 0.08

t = int(input("Enter number of year: "))

times_years_power = n*t

Amount = P * ((1+(r/n))** (n * t))

print(Amount)

"""Write a program that will compute the area of a circle. Prompt the user to 
enter the radius and save it to avariable called radius. Print a nice message 
back to the user with the answer."""

pi = 3.14

radius = int(input("Enter radius"))

Area_of_circle = pi * (radius ** 2)

print(Area_of_circle)

"""Write a program that will compute the area of a rectangle. 
Prompt the user to enter the width and height of the rectangle and 
store the values in variables called width and height. 
Print a nice message with the answer.."""

width  = int(input("Width: "))
height = int(input("Height: "))

Area_of_rectangle = width * height

"""Challenge: Write a program that will convert degrees celsius to degrees fahrenheit."""

Degree_C = int(input("Enter Temperature in celsius:"))

Degee_F = Degree_C * (9 / 5) + 32

print(Degee_F)

print(Area_of_rectangle)


"""
Write a program that will compute MPG for a car. Prompt the user to enter 
the number of miles driven and store it in a variable called miles and the 
number of gallons used stored in a variable gallons. Print a nice message 
with the answer.
"""


miles = int(input("Insert miles driven"))
gallons = int(input("Insert gallons stored"))

MPG = miles / gallons

print(MPG)



