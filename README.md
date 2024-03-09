# Downloads Folder Cleaner

This is a simple python script that will clean your downloads folder by moving all the files to their respective folders.
You can make additional mapping such as adding new folders and file types using `settings.json` file.

## Prerequisites
- Python version - 3.10 or higher
- System:
  - Windows - 8 or higher
  - Linux - Ubuntu 18.04 or higher (Have not tested on other distributions)
  - MacOS - Catalina or higher

## How to use

### Windows
1. Clone the repository to `C:\Program Files\`
2. Open `cmd` as administrator
3. Run `cd C:\Program Files\downloads-folder-cleaner`
4. Run `setx PATH "%PATH%;C:\Program Files\downloads-folder-cleaner\downloads-cleaner\clean-downloads.py"`
5. Now you can run `clean-downloads.py` from anywhere in the command line
> Note: If you are not able to just run `clean-downloads.py` then you can also try running `python clean-downloads.py`

### MacOS and Linux
1. Clone the repository to `~/Downloads/`
2. Open terminal
3. Run `nano ~/.bash_profile`
4. export PATH="~/Downloads/downloads-folder-cleaner/downloads-cleaner/clean-downloads.py:$PATH"
5. Save and close the file. 
6. To apply the changes, you can either restart your terminal or source the profile script with the command source ~/.bash_profile (or the relevant file for your shell).
7. Now you can run `clean-downloads.py` from anywhere in the command line
8. If you are not able to just run `clean-downloads.py` then you can also try running `python clean-downloads.py`
> Note: You are able to place this repo anywhere on your system but make sure to provide the correct path in the `~/.bash_profile` file.
