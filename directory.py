# Import OS module
import os, os.path

# Ask user if they want to create a new directory.
directory = input("\nWould you like to create a new directory? ")

# Name the new directory
if 'yes' or 'y':
    new_directory = input("\nWhat would you like your new directory to be called? ")
    os.makedirs(new_directory)
else:
    print("\nNo new directory was created.")

# Next ask the user what the name of te file will be.
name_of_file = input("\nPlease input the name that you would like to give to the file: ")

# Complete name of file.
complete_file_name = name_of_file + ".txt"

# Where to save new file.
with open(os.path.join(new_directory, complete_file_name), 'a') as file_object:

# Ask the user for their name, address, and phone number.
    name = input("\nPlease input your name: ")
    file_object.write(f"\n{name.title()}")

    address = input("Please input your address: ")
    file_object.write(f"\n{address.title()}")

    phone_number = input("Please input your phone number: ")
    file_object.write(f"\n{phone_number}\n")

# Check if directory exists.
path_directory = f"/Users/Onyxus/OneDrive - Bellevue University/CIS245/Week 10/{new_directory}/"
isDir = os.path.isdir(path_directory)

# Read file and display contents to the user.
print("\nYour file currently contains: ")
with open(path_directory + complete_file_name, 'r') as file_object:
    for line in file_object:
        print(line.strip())

# Check if file exists.
path_file = f"{path_directory}/{complete_file_name}"
isFile = os.path.isfile(path_file)
print(f"\n{isFile}")

# Show user where their file is located.
print(f"\nYour file is located in {path_directory}.")
