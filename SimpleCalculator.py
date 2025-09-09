n1=float(input('Enter the first number:'))
op=input('Select the operation:\n+ - * / ')
n2=float(input('Enter the second number:'))


if op== '+':
    print('The sum between {} and {} is {:.2f};'.format(n1, n2, n1+n2))
elif op=='-':
    print('The subtraction between {} and {} os {:.2f}'.format(n1, n2, n1-n2))
elif op=='*':
    print('The multiplication between {} and {} is {:.2f}'.format(n1, n2, n1*n2))
elif op=='/':
    if n1==0:
        print('Error! Division by zero is not allowed.')
    if n2==0:
        print('Error! Divison by zero is not allowed.')
    else:
        print('The division between {} and {} is {:.2f}'.format(n1, n2, n1/n2))
else:
    print('Invalid operation! Please select one of the following: + - * /')

repeat=input('Do you want to perform another operation? (y/n):')
if repeat.lower()=='y':
    exec(open('SimpleCalculator.py').read())