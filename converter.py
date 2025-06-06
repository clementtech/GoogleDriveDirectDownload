try:
    import pyperclip
    import re
    import sys

except (ImportError, ModuleNotFoundError):

    sys.exit("Missing required libraries. Please install them by typing the following command: pip install -r requirements.txt")

link_format =  r"^https://drive.google.com/file/d/.+/view\?usp=.+$"

link_input = str(input("Link: "))

if re.match(link_format, link_input):

    with open("history.txt", "a") as link_history:

        link_format_split_a = r"https://drive.google.com/file/d/"

        link_split_a = re.split(link_format_split_a, link_input)[1]

        link_format_split_b = r"/view\?usp="

        link_id = re.split(link_format_split_b, link_split_a)[0]

        converted_link = f"https://drive.google.com/uc?export=download&id={link_id}"

        pyperclip.copy(converted_link)

        pyperclip.paste()

        print(f"Copied link to clipboard: {converted_link}")

        link_history.write(f"{converted_link}\n")

else: 
    sys.exit("Invalid Link.")