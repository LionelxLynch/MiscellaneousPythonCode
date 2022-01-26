total = 0
avg = 0
count = 0
while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    else: 
        try:
            total += int(num)
            count += 1
            avg = total/count
        except:
            print("Invalid input")
print(f'Total: {total}\nCount: {count}\nAverage: {avg}')
