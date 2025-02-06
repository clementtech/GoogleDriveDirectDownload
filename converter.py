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
    
    
    print("This program converts Google Drive Shared Link to Direct Download Link")
    print("This program uses Pyperclip module to get the Shared Link from the Clipboard")
    print("You can install the Pyperclip module using the following command:")
    print("pip install pyperclip")

    print("This program will respect your choice and provide you the option to not use the Pyperclip module")

    clipboard_consent = str(input("Do you want to use Pyperclip? (Y/N): ")).upper()

    if clipboard_consent == "Y":
        

        try:

            import pyperclip

            print(pyperclip.copy(convert(str(input("Enter the Shared Link: ")))))

            pyperclip.paste()

            print("Copied to Clipboard!")

        
        except ModuleNotFoundError:
            print("Pyperclip module is not installed")
            print("Please install the Pyperclip module using the following command:")
            print("pip install pyperclip")

        except pyperclip.PyperclipException:
            print("Please visit: https://pypi.org/project/pyperclip/")
            print("Seems like Pyperclip needs some dependencies to be installed")
            print("Most likely you are using Linux :) Good Luck Installing and Fixing Useless Dependencies")

    elif clipboard_consent == "N":

        # Printing the Direct Download Link
        # Ask the user to enter the Shared Link
        # Call the convert function and pass the Shared Link as an argument
        print("Direct Download Link:")
        print(convert(str(input("Enter the Shared Link: "))))

    else:
        print("Invalid Input")
        sys.exit("Please enter Y or N")

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
    return f"https://drive.google.com/uc?export=download&id={unique_code}"

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