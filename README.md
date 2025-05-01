# Google Drive Direct Download
A Python Program that convert Google Drive Link into Direct Download Link

# How does it works?
### Typical Shared Link Format:
```
https://drive.google.com/file/d/YourUniqueFileCode/view?usp=sharing
```
### Convert the Link Format as below to get Direct Download Link Format:
```
https://drive.google.com/uc?export=download&id=YourUniqueFileCode
```

# Sneak Peek:
### Prompt user for link:
![image](https://raw.githubusercontent.com/clementtech/GoogleDriveDirectDownload/refs/heads/main/assets/prompt_link.png)

### Successfully converted the link:
![image](https://raw.githubusercontent.com/clementtech/GoogleDriveDirectDownload/refs/heads/main/assets/success_message.png)
- The link will be automatically copied to the user clipboard thanks to the Pyperclip module

### Error handling:
![image](https://raw.githubusercontent.com/clementtech/GoogleDriveDirectDownload/refs/heads/main/assets/error_handling.png)

# Prerequisites:
- [Python](https://www.python.org/downloads/)

# How to use:
1. Download the project onto your computer.
    - You can download the project by using the [git](https://git-scm.com/downloads) command:
    ```
    git clone https://github.com/clementtech/GoogleDriveDirectDownload.git
    ```

2. Download the required dependencies.
    - The dependencies can be installed using the following command:
    ```
    pip install -r requirements.txt
    ```
3. Done setup!
    - You can run the program by entering the following command:
    ```
    python converter.py
    ```

# Features:
- Convert Google Drive Link into Direct Download Link
- Paste converted link into user clipboard
- Link history