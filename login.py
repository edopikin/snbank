from utils import error_msg, read_file, write_data
from datetime import datetime

import os

FOLDER = os.path.dirname(os.path.abspath(__file__))

# save the user session, receives username as parameter
def save_user_session(username):
    my_file = os.path.join(FOLDER, "user_session.txt")

    # get the current timestamp
    now = datetime.now()
    # concatnate the username and timestamp
    session = f"{username} {now}"
    # write the session string to "user_session.txt" file
    write_data(my_file, session)


# remove the user session, receives user_to_remove as parameter
def remove_user_session(user_to_remove):
    my_file = os.path.join(FOLDER, "user_session.txt")

    # open file for read
    fr = open(my_file, "r")
    # read lines in file
    lines = fr.readlines()
    # close file
    fr.close()
    # open file for write
    fw = open(my_file, "w")
    # loop through read lines
    for line in lines:
        # strip line, spilt by space
        # select the first item in the array (username)
        # if the username is not equal to the passed in user_to_remove
        if line.strip().split(" ")[0] != user_to_remove:
            # write the line to the file
            fw.write(line)
    # close read write
    fw.close()


# handles user login
def login():
    print("*Staff Login*")
    # read staff in staff.txt file, returns a dict {username: (username, password)
    staff = read_file('staff.txt')
    isLoggingIn = True

    while isLoggingIn:
        # read user input for username and password
        uname_input = input("Enter Username >_ ")
        pwd_input = input("Enter Password >_ ")

        try:
            # get user input from the staff dict
            staff_details = staff[uname_input]
            # if user in staff dict
            if staff:
                # get the username and password from returned tuple (username, password)
                username, password = staff_details
                # if the username and password match userinput
                if username == uname_input and password == pwd_input:
                    # end loop
                    isLoggingIn = False
                    # call the save_user_session function pass username
                    save_user_session(username)
                    # return username and end function
                    return username
                else:
                    # if user input is incorrect, throw an error
                    raise KeyError()
        # if username not in dict, handle error
        except KeyError:
            # print error message
            error_msg("Wrong User detail, Try again")
            # get next action from user
            response = input("Enter any key to try again or Q to cancel >_ ")
            # if user quits
            if response.upper() == 'Q':
                # end loop
                isLoggingIn = False
    # return false if function doesn't end before here
    return False
