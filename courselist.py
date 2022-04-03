# Lionel Lynch

# courselist.py

# This assignment requires you to let the user enter a list of courses, 
# but stop them if they enter a sixth and insist that they delete one.  
# The result will be an interactive program - it will keep running until the user commands it to stop.

# Empty list
course_list = []

# Get the list of course from the user
def get_list(list):
    while True:
        # Prompt user to enter courses, then add the courses to the list
        courses = input("""Enter a course you would like to enroll in or type "EXIT" if you would like to stop: """)
        list.append(courses) # add to list

        # Break if the user enters 'EXIT'
        if courses == "EXIT":
            list.remove('EXIT') # Remove 'EXIT' from the list
            break

        elif len(list) >= 6:
            remove_course(list)
            
# print items in the list
def get_item(list):
    print('--YOUR COURSES--') # HEADER
    for index in range(0, len(list), 1): 
        item = list[index]
        print (f'{item}')

# print a numbered list of the items
def get_item_numbered(list):
    print('--YOUR COURSES--')
    for index in range(0, len(list), 1): 
            item = list[index]
            print (f'{index+1}. {item}')

# Cap the user at 6 courses
def remove_course(list):
        print(f'You have one too many courses. Which course would you like to remove.')

        # loop through the index of the course list, and print the items in it.
        get_item_numbered(list)

        # Get user input on which course to drop
        drop_course = int(input('You have too many coursea. Enter the number of the course you would like to remove. Ex: Entering "1" would remove the first course: '))
        list.pop(drop_course-1)

        # loop through the index of the course list, and print the items in it.
        get_item_numbered(list)

# Main function
def main():
    get_list(course_list)
    get_item(course_list)
    get_list(course_list) 

# Main entrance 
if __name__ == '__main__':
    main()