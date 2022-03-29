# Lionel Lynch

longer_list = ['item1','item2','item3','item4','item5','item6']
print(longer_list)

# The Range function when combined with the List function prints out the
# the numbers given in the range function [inclusive,exclusive]
my_range = list(range(1,10))
print(range)

# You can also turn the list into the range
range_list = list(my_range)
print(range_list)

# We can also loop over ranges using FOR loops
for i in range(1,10):
    print(i)

# We can also loop over a captured, previosly defined ranged
for i in range_list:
    print(i)

# We can also loop over a list, and that example is pretty much that
for i in longer_list:
    print(i)

# The way the FOR loop works is it ask
# for <item> in <list/object>:
#       do something

# ACTIVITY 1
# This function will loop through the list and return the sum the items in the list
def sum_of_list(list):
    sum = 0 # When ever you want to calculate the sum you must intialize the variable
    for i in list:
        sum = sum + i
    return sum

# Now what if we want to loop through the index of the itemes in the list?

for index in range(0, len(longer_list), 1):
    item = longer_list[index]
    print('The item at index',index, 'is',item)