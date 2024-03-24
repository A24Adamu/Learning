#==================PRACTICAL TASK 3==================
#==================   Pseudo code  ==================
# 1. Request user to enter integers three times - number1, number2, number3.
# 2. Calculate the sum of the three integers.
# 3. Calculate the difference between first and second integer.
# 4. Multiply the third integer by the first integer.
# 5. Divide the sum of the three integer by the third integer.
# 6. Print out 1 - 5 commands.

#==================   Python code  ==================
number1 = int(input("Enter first integer: ")) 
number2 = int(input("Enter second integer: "))
number3 = int(input("Enter third integer: "))

# Sum of the three integers.
sum = number1 + number2 + number3

# Difference between 1st and 2nd integer
minus = number1 - number2

# Product of 3rd and 1st integers.
multiply = number3 * number1

# Divide the sum of the three integers with 3rd integer.
division = sum/number3

print("First integer = {}\nSecond integer = {}\nThird integer = {}\nSum of the three integers = {}\nFirst integer - second integer = {}\nThe third integer x the first integer = {}\nSum of first three integers/the third integer = {}".format(number1, number2, number3, sum, minus, multiply, division))
