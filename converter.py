# Import library into the program
# Pyperclip is used to copy/paste URL to clipboard
import pyperclip
# Regular Expression (re) is used to check if the link is valid and extract id
import re
# sys is used to exit the program when invalid link is provided
import sys

# Regex, link format that the re should cross check with the input to ensure the link is valid
link_format =  r"^https://drive.google.com/file/d/.+/view\?usp=.+$"

# Request link input from user and convert it to string
link_input = str(input("Link: "))

# re.search(template, input)
# If the input matches with the format
# Proceed with the program
if re.search(link_format, link_input):

    with open("history.txt", "a") as link_history:

        # Split out the front part of the link
        link_format_split_a = r"https://drive.google.com/file/d/"

        # Left the back nonsense of the link
        link_split_a = re.split(link_format_split_a, link_input)[1]

        # Split the last part of the link
        link_format_split_b = r"/view\?usp="

        # The link should just remain the id which is what we want
        link_id = re.split(link_format_split_b, link_split_a)[0]

        # Build the export link with the link id
        converted_link = f"https://drive.google.com/uc?export=download&id={link_id}"

        # Copy the converted_link into user clipboard
        pyperclip.copy(converted_link)

        # Paste the link into the user clipboard
        pyperclip.paste()

        # Show success message to the user and display the converted link
        print(f"Copied link to clipboard: {converted_link}")

        link_history.write(f"{converted_link}\n")

# If link does not matches
else: 

    # Exit the program with the message "Invalid Link."
    sys.exit("Invalid Link.")