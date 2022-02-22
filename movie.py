#Lionel Lynch
#movie.py
#calculate the price of admission for a movie based on user input 

#get input from user
moviegoers = int(input('Enter the number of moviegoers: '))

#determine price based on group size
if (moviegoers > 25):
    print(f'The toal ticket price is $ {moviegoers*7.25}')

else:
    print(f'The total ticket price is $ {moviegoers*12 - 12 + 9.50}')
