# Convert Format:
# Typical Shared Link Format:
# https://drive.google.com/file/d/YourUniqueFileCode/view?usp=sharing
# Convert the Link Format as below to get Direct Download Link Format
# https://drive.google.com/uc?export=download&id=YourUniqueFileCode

import sys

def main():
    
    print(convert(str(input("Enter the Shared Link: "))))

def convert(link):

    if "drive.google.com" not in link:
        sys.exit("Invalid Link Format")

    elif "usp=sharing" not in link:
        sys.exit("File is not Publicly Shared")
    
    unique_code = code(link)

    return f"Direct Download Link:\nhttps://drive.google.com/uc?export=download&id={unique_code}"


def code(code):

    try:
        return code.strip().split('/')[5]

    except IndexError:
        sys.exit("Invalid Link Format")


if __name__ == '__main__':
    main()