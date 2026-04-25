import os
import shutil

# Path to Downloads
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

# File type categories
folders = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".m4a"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"],
    "Archives": [".zip", ".rar", ".7z"]
}

# Create folders
for folder in folders:
    folder_path = os.path.join(downloads_path, folder)
    os.makedirs(folder_path, exist_ok=True)

# Move files
for file in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path, file)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    _, ext = os.path.splitext(file)
    moved = False

    for folder, extensions in folders.items():
        if ext.lower() in extensions:
            shutil.move(file_path, os.path.join(downloads_path, folder, file))
            moved = True
            break

    # If no match
    if not moved:
        others_path = os.path.join(downloads_path, "Others")
        os.makedirs(others_path, exist_ok=True)
        shutil.move(file_path, os.path.join(others_path, file))

print("Downloads cleaned!")
