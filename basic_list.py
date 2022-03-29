# Lionel Lynch
# basiclist.py
# Notes on the lecture about list/arrays

# list can be seen as a contaner of sorts.They can hold multiple items, such as variables. Python has the capablity to store the different types of data in one 
# list, but it's best practice to store the same type of data in a list/array.

# Here's a example of a list/array.

from matplotlib.cbook import index_of


my_list = ['item1', 'item2', 'item3']

print(my_list)

# Now as a stated eariler you can technically make a list consiting of different types of variables, but this isn't reccomened. 

# Here's a example of a list that isn't in line with Python best practice.

strange_list =['item1', 1, 3.01, False]
print('Strange list example', strange_list)

# List a ordered colletions of data. Meaning that each item has a Index or place indicated by a number.
# To be more specfic the name would be a Zero-index because instead of starting from 1 like in convential counting,
# the ordered collection starts from 0. So the first item in a list/array would be the 0th item not the 1st.

# Here's an example of the ordering of list in a index in python.

print(my_list[0]) # This corresponds to the first item in the list. 
print(my_list[1]) # This corresponds to the second item in the list. 
print(my_list[2]) # This corresponds to the third item in the list. 

# Note: You can call for items in a list in any order you like.

print(my_list[2])
print(my_list[0])
print(my_list[1])

# You can also use negative indices to walk itterate through a list backwards.

# Lets make a longer list first
longer_list = ['item1','item2','item3','item4','item5','item6']

# By using the negative number we start from the back of the list, meaning the number outputed would be 'item5'
print('Negative indexing: ', longer_list[-2])

# You can also print certain numbers from one range to another range
# Example below

# This line of code assigns a range within the list to the var shorter_list
shorter_list = longer_list[1:4] # [inclusive:exclusive]

# Now it's important to know how the range notation works in python.
# The left side (that being the first number) is inclusive and the right side is exculsie, 
# meaning that when in this example the short_list will include all values from the secnond item through to the third item.
# The out put would look like ['item2','item3','item4']

# So,using range notation yuo make shorter list out of larger list
print('Range example: ', shorter_list) 

# So, how do we add to a list? Theres a few ways, and the easiest way is to add a item to the end of a list.
# Which would be called "appending" a item to a list. When the order doesnt matter you should APPEND.

print('Appeding item4: ')
print(my_list)
my_list.append('item4') # This line of code adds 'item 4 to the list
print('item4 appended: ', my_list)

# Lets talk about inserting items, which shouldnt be confused with appending items
# When inserting a item into a lost you want to use dot notation and then the word 'insert'
# then as funstion args you want to first pass the location in the list for example '2',
# then you want to pass the value you wish insert. It's important to know that the first arg
# places the item BEFORE the vaule you give. So if you pass a number 2 then you would be placing the
# item BEFORE the item at the 2nd index. Lets go through a example.

longer_list.insert(0,'item0')
print('After insertion: ', longer_list)

# Removing items follows the pattern. Using dot notaion you can remove items.
# In this example we remove a item from a list using the Vaule of said item
longer_list.remove('item0')
print('After deletion: ', longer_list)

# But we can also delete or POP items using the index or position of the item
longer_list.pop(5)
print('After deletion/pop: ', longer_list)

# Now what if we wanted to find the index of a item in a list? Is there a function that we could use to
# help find the index of any given item in a list? That function would be the '.index' function.
# This fuction is whats known as a slow funtion. Meaning that it has to go through the entirety of the list
# to determine if the item you're looking for exit or not. 
print('searching list....')
index_of_item4 = longer_list.index('item4')
print('the index of item4 is: ', index_of_item4)

# Now what you used the index funtion to look for a vaule that wasnt in the list for example 'item42'

#---index_of_item42 = longer_list('item42')--- # This code would result in a ERROR

# What you want to do is write your code in a way that would block or acccount for any potential search
# that could fail.
# Here's a examlpe below. In structuring the code this way we are to account for the scenario where the user 
# makes a search for a item that doesn't exist
if 'item42' in longer_list: # the in te
    index_of_item42 = longer_list('item42')
    print(index_of_item42)
else:
    print('Item not found.')

# Theres also empty list. These are pretty self explanatory, it's a list with no items. Shocker
# Heres an example below.
print('Empty list')
empty_list = []
print('A Empty list: ', empty_list)

# So when would we need to use a empty list? Good question.Theres a multitude of situations where you would want to
# Intialize a list before inputing items into it. A obviuos case would be when using a loop to genrate items in a list
# via itteration.Think back to the assingment when we had to find the sum, where we started from 0 and repeatedly
# added to it. Empty list are similar.


# Lecture Activity 1
def list(a,b):
    list = [a,b]
    list.remove(a)
    list.append(b)
    return list

# Call list
print(list('water', 'fire'))

# List to test function 
hay_stack = ['h1','h2', 'h3','h4','h5','h6']


# Lecture activity 2
def Vaule_searcher(list,value):
    if value in list:
        index_of_vaule = list.index(value)
        print("The value was found: ",value)
        print("Here's the index:  ",index_of_vaule)
    else:
        print('This vaule wasnt found.')

# Call function
Vaule_searcher(hay_stack, 'needle')