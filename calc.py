operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
number1 = int(input("Please Put your first number. "))
number2 = int(input("Please put your second number. "))

if operation == '+':
    print('{} + {} = '.format(number1, number2))
    print(number1 + number2)

elif operation == '-':
    print('{} - {} = '.format(number1, number2))
    print(number1 - number2)

elif operation == '*':
    print('{} * {} = '.format(number1, number2))
    print(number1 * number2)

elif operation == '/':
    print('{} / {} = '.format(number1, number2))
    print(number1 / number2)

else:
    print('You have not typed a valid operator, please run the program again.')
