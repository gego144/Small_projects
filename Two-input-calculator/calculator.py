import math

#telling the user the operations they can use
print("The operations you can use are + , - , * , / , ** , sqrt, and log")

#user selecting their operation
first_op = input("Put in the operation you would like to use: ")

#user inputs their first number and returns their input back if its not a number
print("Enter your first number")
first_num = input()
while first_num.isdigit() == False:
    first_num = input("Please enter a number: ")

#converting the input to a float once its been checked that a number has been inputted
first_num = float(first_num)

#user inputs their second number and returns their input back if its not a number
print("Enter your second number")
second_num = input()
while second_num.isdigit() == False:
    second_num == input("Please enter a number: ")

#converting the input to a float once its been checked that a number has been inputed
second_num = float(second_num)

#doing the math based on the operation inputted and the first and second number
if first_op == "+":
    print(first_num + second_num)
elif first_op == "-":
    print(first_num- second_num)
elif first_op == "*":
    print(first_num * second_num)
elif first_op == "/":
    print(first_num/second_num)
elif first_op == "**":
    print(first_num**second_num)
elif first_op == "sqrt":
    print(math.sqrt(first_num))
elif first_op == "log":
    print(math.log(first_num, second_num))
