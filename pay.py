def compute_pay(hours, rate):
    hours = int(input("Enter hours: "))
    rate = float(input("Enter rate: "))
    pay = hours * rate
    if hours <= 40:
        print(f'Pay: {pay}')
    elif hours > 40:
        pay = 40 * rate + (hours - 40) * rate * 1.5
        print(f'Pay: {pay}')
compute_pay(45,10)