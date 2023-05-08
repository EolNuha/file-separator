import os
import shutil
import re

default_folder_name = "Downloads"
allowed_folder_name_pattern = r"^[A-Za-z0-9_\-]+$"


def get_folder_path(folder_name):
    user_input = input(f"Enter folder name (default '{default_folder_name}'): ")
    folder_name = user_input.strip() or folder_name
    if not re.match(allowed_folder_name_pattern, folder_name):
        raise ValueError("Invalid folder name")
    folder_path = os.path.expanduser(f"~/{folder_name}")
    return folder_path


def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def move_files_to_category(category_name, allowed_extensions, downloads_path):
    category_path = os.path.join(downloads_path, category_name)
    create_folder_if_not_exists(category_path)
    for file_name in [
        f for f in os.listdir(downloads_path) if f.lower().endswith(allowed_extensions)
    ]:
        file_path = os.path.join(downloads_path, file_name)
        new_file_path = os.path.join(category_path, file_name)
        if not os.path.exists(new_file_path):
            shutil.move(file_path, category_path)
            print(f"Moved {file_name} to {category_path}")


categories = [
    {
        "name": "images",
        "extensions": (".png", ".jpg", ".jpeg", ".bmp", ".gif", ".webp", "ico"),
    },
    {"name": "videos", "extensions": (".mp4", ".mov", ".flv", ".avi", ".webm")},
    {"name": "audios", "extensions": (".mp3", ".flac", ".wav")},
    {"name": "documents", "extensions": (".pdf", ".docx", ".xlsx", ".pptx")},
    {
        "name": "code",
        "extensions": (".py", ".java", ".html", ".js", ".css", ".sqlite3", ".db"),
    },
]

downloads_path = get_folder_path(default_folder_name)

for category in categories:
    try:
        move_files_to_category(category["name"], category["extensions"], downloads_path)
    except Exception as e:
        print(f"Error processing category {category['name']}: {e}")
