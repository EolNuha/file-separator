import os
import shutil


def main(folder, extensions):
    # Define the path to the downloads folder
    downloads_path = os.path.expanduser("~/Downloads")

    # Define the path to the new folder to be created
    new_folder_path = os.path.join(downloads_path, folder)

    # Create the new folder if it doesn't already exist
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)

    # Loop through all files in the downloads folder
    for file_name in os.listdir(downloads_path):
        file_path = os.path.join(downloads_path, file_name)

        # Check if the file is an image file
        if file_name.lower().endswith(extensions):
            # Move the file to the new folder if it's not already there
            if not os.path.exists(os.path.join(new_folder_path, file_name)):
                shutil.move(file_path, new_folder_path)
                print(f"Moved {file_name} to {new_folder_path}")


files = [
    {
        "folder": "images",
        "extensions": (".png", ".jpg", ".jpeg", ".bmp", ".gif", ".webp", "ico"),
    },
    {"folder": "videos", "extensions": (".mp4", ".mov", ".flv", ".avi", ".webm")},
    {"folder": "audios", "extensions": (".mp3", ".flac", ".wav")},
    {"folder": "documents", "extensions": (".pdf", ".docx", ".xlsx", ".pptx")},
    {
        "folder": "code",
        "extensions": (".py", ".java", ".html", ".js", ".css", ".sqlite3", ".db"),
    },
]

for item in files:
    main(item["folder"], item["extensions"])
