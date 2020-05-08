# -Create staff.txt file (2 Staff members)
# Username
# Password
# Email
# Fullname

# -Create customer.txt file (Empty)

# -Run
# options
# 1. Staff Login
# 2. Close App

# -Staff Login
# Username
# Password
# Error -> Error message -> try again
# Success -> New file(user_session) -> store the user session

# -Login Success
# -1. Create New Bank Account
# Provide the following infomation saved to customer.txt
# Account Name
# Opening Balance
# Account Type
# Account Email
# generate 10 Digit account number
# Success -> display account number -> show options

# -2. Check Bank Account Details
# request for acccount number
# display account details
# back option leading to options

# -3. Logout
# delete session and return to first option

from login import login
from operations import operations
from utils import error_msg


def cli_bank():
    running = True
    options = "*Menu*\n1. Staff Login\n2. Close App\n"

    print("Welcome to HNG CLI Bank\n")
    while running:
        print(options)
        try:
            user_input = int(input("Enter the number for choice option >_ "))
            if user_input > 0 and user_input <= 2:
                if user_input == 1:
                  # invoke operations function
                    operations()
                else:
                    print("Bye!")
                    # set running to false to break loop
                    running = False
            else:
                # print error message if the user inputs a number less than 1 or greater than 2
                error_msg("Invalid Option, option must be a number 1 or 2")
        except ValueError:
            # print error message if user input value not a number
            error_msg("Option must be a number 1 or 2")


if __name__ == "__main__":
    # Invoke App
    cli_bank()
