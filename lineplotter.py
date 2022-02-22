#Lionel Lynch
#lineplotter.py
#accept slope and intercept as input,
#then output the X values

slope = float(input('Enter the slope: '))
intercept = float(input('Enter the intercept: '))
print(f'Line {slope} * x + {intercept}')
x = 0

while x <= 9:
    y = (slope * x) + intercept
    print(f'AT x = {x} , y = {y}')
    x = x + 1

x = 10

while x <= 100000:
    y = (slope * x) + intercept
    print(f'AT x = {x} , y = {y}')
    x = x * 10