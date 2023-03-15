'''
Take an input from user, print the input <x> is odd
if the input is odd, otherwise print the input <x> is even.
'''

x = int(input('Enter your Number: '))
x%2 == 1 and print("The Number ", x, " is odd")
x%2 == 0 and print("The Number ", x, " is even")
