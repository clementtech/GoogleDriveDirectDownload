# Usage:
# python converter.py
# Enter the Shared Link: https://drive.google.com/file/d/YourUniqueFileCode/view?usp=sharing
# Direct Download Link:
# https://drive.google.com/uc?export=download&id=YourUniqueFileCode

# Note:
# The Shared Link should be Publicly Shared
# The Shared Link should be in the above format

# You can run the program by downloading the file and run the following command using terminal:
# python converter.py

# Importing the required modules
# sys module is used to exit the program if the Shared Link is not in the correct format
# sys module is used to exit the program if the file is not Publicly Shared
# sys module is used to exit the program if the Shared Link is not in the correct format
import sys

# Main function
def main():
    
    # Printing the Direct Download Link
    # Ask the user to enter the Shared Link
    # Call the convert function and pass the Shared Link as an argument
    print(convert(str(input("Enter the Shared Link: "))))

# Convert function
# This function is used to convert the Shared Link to Direct Download Link
def convert(link):

    # Check if the Shared Link is in the correct format

    # Check if the link is Google Drive Link
    # If the link is not in the correct format, exit the program
    if "drive.google.com" not in link:

        # Exit the program if the Shared Link is not in the correct format
        sys.exit("Invalid Link Format")

    # Check if the file is Publicly Shared
    # If the file is not Publicly Shared, exit the program
    elif "usp=sharing" not in link:

        # Exit the program if the file is not Publicly Shared
        sys.exit("File is not Publicly Shared")
    
    # Get the Unique Code from the Shared Link by calling the code function
    unique_code = code(link)

    # Return the Direct Download Link
    return f"Direct Download Link:\nhttps://drive.google.com/uc?export=download&id={unique_code}"

# Code function
# This function is used to get the Unique Code from the Shared Link
def code(code):

    # Split the Shared Link using '/' and get the 6th element which is the Unique Code
    # Try and Except block is used to handle the IndexError
    # If the IndexError occurs, exit the program, which means the Shared Link is not in the correct format
    try:

        # Return the Unique Code
        return code.strip().split('/')[5]

    # If the IndexError occurs, exit the program
    except IndexError:

        # Exit the program if the Shared Link is not in the correct format
        sys.exit("Invalid Link Format")

# Main Guard
# Main guard is to prevent the program from running when the module is imported
# The program will run only when the module is run directly
if __name__ == '__main__':

    # Call the main function
    main()