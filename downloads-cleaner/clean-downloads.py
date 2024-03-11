#!/usr/local/bin/python3
import platform
import os
import json


def get_download_path() -> str:
    """
    Get the download path for the current system
    :return: The download path
    """
    system_name = platform.system()
    download_path = None
    if system_name == "Windows":
        download_path = os.path.join(os.environ['USERPROFILE'], 'Downloads')
    elif system_name == "Darwin":
        download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    else:
        download_path = os.path.join(os.environ['~'], 'Downloads')

    os.chdir(download_path)
    print(f"Download path: {download_path}")
    return download_path


def create_folders_if_needed(dirs_mapping: dict) -> None:
    """
    Create the folders if they don't exist
    :param dirs_mapping: settings.json
    :return: None
    """
    for folder in dirs_mapping:
        if not os.path.exists(folder):
            os.makedirs(folder)


def clean_folder(download_path: str, dirs_mapping: dict) -> None:
    """
    Move the files to the corresponding folder
    :param download_path:
    :param dirs_mapping:
    :return: None
    """
    for file in os.listdir(download_path):
        full_file_path = os.path.join(download_path, file)
        if os.path.isfile(full_file_path):
            for folder, extensions in dirs_mapping.items():
                target_folder_path = os.path.join(download_path, folder)
                # Ensure the target directory exists
                os.makedirs(target_folder_path, exist_ok=True)

                for ext in extensions:
                    if file.endswith(ext) or file.endswith(ext.upper()):
                        target_file_path = os.path.join(target_folder_path, file)
                        try:
                            os.rename(full_file_path, target_file_path)
                        except Exception as e:
                            print(f"An error occurred while trying move the file: {e}")
                        break


def main():
    """
    Main function
    :return:
    """
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    os.chdir(script_dir)

    try:
        settings = json.loads(open('settings.json').read())
    except FileNotFoundError:
        print("Settings file not found")
        return

    try:
        download_path = get_download_path()
    except Exception as e:
        print(f"An error occurred while trying to get the download path: {e}")
        return

    try:
        create_folders_if_needed(settings['dirs_mapping'])
    except Exception as e:
        print(f"An error occurred while trying to create the folders: {e}")
        return

    try:
        clean_folder(download_path, settings['dirs_mapping'])
    except Exception as e:
        print(f"An error occurred while trying to clean the folder: {e}")

main()
