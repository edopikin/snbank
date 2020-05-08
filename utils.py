import os

FOLDER = os.path.dirname(os.path.abspath(__file__))

# reusable function for printing error messages in profram
def error_msg(message):
    print(f'**ERROR:**\n{message}\n')


# function to read file, receives parameter of file name eg. customer.txt
def read_file(file):
    my_file = os.path.join(FOLDER, file)

    # open file passing the file name.extension for reading
    f = open(my_file, 'r')
    # create dictionary for quick look up
    data = {}
    try:
        # loop through read data
        for line in f.readlines():
            # strip read line removing special characters
            stripped_data = line.strip()
            # split the line in to an array by ","
            split_data = stripped_data.split(",")
            # make data a tuple, to keep data unchangeable in code
            data_tuple = tuple(split_data)
            # use the first item of the tuple as key in the dict
            data[data_tuple[0]] = data_tuple
    except:
        # print an error message if somthing went wrong
        error_msg(f"Something went wrong in {file}")
    # close file
    f.close()
    # return the dict
    return data


# function to write to a file
# receives parameter of file name eg. customer.txt and the data you want to write
def write_data(file, data):
    my_file = os.path.join(FOLDER, file)

    # open file passing the file name.extension for appending
    f = open(my_file, 'a+')
    # writes data to file and adds a newline at the end of line
    f.write(data + '\n')
    # close file
    f.close()
