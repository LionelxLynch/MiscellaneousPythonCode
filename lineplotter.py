#Lionel Lynch
#lineplotter.py
#accept slope and intercept as input,
#then output the X values and y values.


#get slope and intercept from user via input
slope = float(input('Enter the slope: '))
intercept = float(input('Enter the intercept: '))

#show the line equation
print(f'Line {slope} * x + {intercept}')

#loop for 0 through 9
x = 0
while x <= 9:
    y = (slope * x) + intercept
    print(f'AT x = {x} , y = {y}')
    x = x + 1

#loop for 10^2 up to 100,000
x = 10
while x <= 100000:
    y = (slope * x) + intercept
    print(f'AT x = {x} , y = {y}')
    x = x * 10