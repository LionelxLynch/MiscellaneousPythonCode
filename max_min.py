largest = None
smallest = None
while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    else:
        if largest is None or largest < num:
            largest = num 
        elif smallest is None or smallest > num:
            smallest = num  

print(f'Max: {largest}\nMin: {smallest}') 