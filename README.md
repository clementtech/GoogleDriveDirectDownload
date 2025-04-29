# Google Drive Direct Download
A Python Program that convert Google Drive Link into Direct Download Link

# How it works?
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