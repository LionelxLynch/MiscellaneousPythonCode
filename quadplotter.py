#Lionel Lynch
#quadplotter.py
#accept a, b, and c as coefficients as input,
#then output the X values and y values.

#get a, b, and c from user via input
a = float(input('Enter coefficient a: '))
b = float(input('Enter coefficient b: '))
c = float(input('Enter coeffient c: '))

#show the quadratic equation
print(f'Parabola y = {a} x^2 + {b} x + {c}')

#loop for 0 through 9
x = 0
while x <= 9:
    y = a * (pow(x,2)) + b*x + c    #quadratic formula 
    print(f'AT x = {x} , y = {y}')
    x = x + 1

#loop for 10^2 up to 10,000,000
x = 10
while x <= 10000000:
    y = a * (pow(x,2)) + b*x + c    #quadratic formula 
    print(f'AT x = {x} , y = {y}')
    x = x * 10