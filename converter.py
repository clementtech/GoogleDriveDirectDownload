# Convert Format:
# Typical Shared Link Format:
# https://drive.google.com/file/d/YourUniqueFileCode/view?usp=sharing
# Convert the Link Format as below to get Direct Download Link Format
# https://drive.google.com/uc?export=download&id=YourUniqueFileCode


def main():
    
    link_input = str(input("Enter the Shared Link: "))

    unique_code = link_input.strip().split('/')[5]

    direct_link = f"https://drive.google.com/uc?export=download&id={unique_code}"

    print(f"Direct Download Link: {direct_link}")

if __name__ == '__main__':
    main()