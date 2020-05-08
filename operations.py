from random import randint
from utils import error_msg, write_data, read_file
from login import login, remove_user_session


# function to handle bank operations
def operations():
    # invoke login function to log user in and get username if user
    staff = login()
    running = True
    # if the login is successful
    if staff:
        options = "\n*Menu*\n1. Create New Bank Account\n2. Check Bank Account Details\n3. Logout\n"
        while running:
            print(options)
            try:
                # get user action
                user_input = int(input("Select option >_ "))
                # if input is within range and correct
                if user_input in range(1, 4):
                    # first option
                    if user_input == 1:
                        try:
                            # get details from staff
                            acc_name = input("Enter Account Name >_ ")
                            open_bal = float(
                                input("Enter Opening Balance >_ ") or 0)  # if no input, default to 0
                            acc_type = input("Enter Account Type >_ ")
                            acc_email = input("Enter Email Address >_ ")
                            # check if fields are not empty
                            if (len(acc_name) and len(acc_type) and len(acc_email)):
                                # generate random number for accout number
                                acc_no = randint(0000000000, 9999999999)
                                # concatnate values to a comma separeated string
                                info = f"{acc_no},{acc_name},{acc_type},{acc_email},{open_bal}"
                                # write the string to the customer.txt file
                                write_data("customer.txt", info)
                                # print the user's account number
                                print(f"\n**New Account Number: {acc_no}***")
                            # if a required field is not entered
                            else:
                                # print and error message
                                error_msg("All fields are required")
                        # handle conversion error for float(open balance)
                        except ValueError as e:
                            # print the error message
                            error_msg(e)
                    # second option
                    if user_input == 2:
                        try:
                            # get account number from user
                            acc_no = input("Enter Account Number >_ ")
                            # read the customers file, returns a dict {'account_number': (acc_no, acc_name, acc_type, acc_email, open_bal)}
                            customers = read_file("customer.txt")
                            # unpack tuple for the customer if customer in dict
                            acc_no, acc_name, acc_type, acc_email, open_bal = customers[acc_no]
                            # print information
                            print("\n**Account Details**")
                            print(f"Account Number: {acc_no}")
                            print(f"Account Name: {acc_name}")
                            print(f"Account Type: {acc_type}")
                            print(f"Account Email: {acc_email}")
                            print(f"Opening Balance: N {open_bal}")
                        # handle error, if account number not in dict
                        except KeyError:
                            # print error message
                            error_msg("Invalid/Incorrect Account Number")
                    # option 3
                    if user_input == 3:
                        # clear the current staff session
                        remove_user_session(staff)
                        # end loop
                        running = False
                else:
                    # print error message if the user inputs a number less than 1 or greater than 3
                    error_msg(
                        "Invalid Option, option must be a number 1 or 3")
            except ValueError:
                # print error message if the user input is not a number
                error_msg("Option must be a number")
