
import sys

def main():


 
    import pyperclip

    pyperclip.copy(convert(str(input("Enter the Shared Link: "))))

    # Use pyperclip function to paste the item into the clipboard
    pyperclip.paste()

    # Display Success Message to the User
    print("Copied to Clipboard!")

        # # Except pyperclip.PyperclipException will appear if the dependencies is not installed correctly
        # # Usually this error will occurs for Linux Users
        # except pyperclip.PyperclipException:

        #     # Display Error Message
        #     # Good Luck Fixing, that's what all I could say :D
        #     print("Please visit: https://pypi.org/project/pyperclip/")
        #     print("Seems like Pyperclip needs some dependencies to be installed")
        #     print("Most likely you are using Linux :) Good Luck Installing and Fixing Useless Dependencies")

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