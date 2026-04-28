def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mult(x, y):
    return x * y
def div(x, y):
    if y == 0:
        print('Cannot div by zero')
    return x / y

def calculator():
    while True:
        print('What function would you like to perform: +, -, *, or /?')
        print('Or if you would like to end the application enter "quit"')
        
        user_input = input(': ')
        
        if user_input == 'quit':
            break
        
        if user_input in ['+', '-', '*', '/']:
            num1 = float(input('Enter the first number: '))
            num2 = float(input('Enter the second number: '))
            
        if user_input == '+':
            result = add(num1, num2)
            print(result)
        elif user_input == '-':
            result = sub(num1, num2)
            print(result)
        elif user_input == '*':
            result = mult(num1, num2)
            print(result)
        elif user_input == '/':
            result = div(num1, num2)
            print(result)
        
calculator()