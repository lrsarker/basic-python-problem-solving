#Let's Build a Calculator.
'''
a+b
a-b
a*b
a/b
a%b
'''
f_number = float(input("Enter 1st Number : "))
operator = input("Enter Operator (+,-,*,/,%) : ")
l_number = float(input("Enter 2nd Number : "))

if operator == "+":
    print(f_number + l_number)
elif operator == "-":
    print(f_number - l_number)
elif operator == "*":
    print(f_number * l_number)
elif operator == "/":
    print(f_number / l_number)
elif operator == "%":
    print(f_number % l_number)
else:
    print("Invalid Operation")

#Code End.
