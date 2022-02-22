#Lionel Lynch
#oddeven.py
#randomly choose a number, accept input from the user, and print whether or not the user is correct.

#import random module
import random 

#accept input from the user 
guess = input(('Im thinking of a number. Is it odd or even? ')) 

#retrieve pseudo random number
num = random.randrange(1,256) 

#Determine whether user guessed the number correctly
if (guess == 'even' and num % 2 == 0):
    print(f'My number was {num}. You guessed the even number, Well done!')
elif (guess == 'odd' and num % 2 != 0):
    print(f'The number was {num}. You guessed the odd number, Well done!')
elif(guess == 'even' and num % 2 != 0 or guess == 'odd' and num % 2 == 0):
    print(f'The number was {num}. Sorry!')
else:
   print(f"""You didn't enter "odd" or "even". You forfeit! (My number was {num} if you're wondering.)""")