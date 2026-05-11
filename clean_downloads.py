import os
import shutil
from datetime import datetime

# Path to Downloads
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

# LOG SETUP
log = []

# Create logs folder inside Downloads
logs_folder = os.path.join(downloads_path, "cleaner_logs")
os.makedirs(logs_folder, exist_ok=True)

# Create log file with timestamp
log_filename = datetime.now().strftime("log_%Y-%m-%d_%H-%M-%S.txt")
log_file_path = os.path.join(logs_folder, log_filename)

# File type categories
folders = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".m4a"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"],
    "Archives": [".zip", ".rar", ".7z"]
}

# Create category folders
for folder in folders:
    os.makedirs(os.path.join(downloads_path, folder), exist_ok=True)

# Move files
for file in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path, file)

    if os.path.isdir(file_path):
        continue

    _, ext = os.path.splitext(file)
    moved = False

    for folder, extensions in folders.items():
        if ext.lower() in extensions:
            new_path = os.path.join(downloads_path, folder, file)
            shutil.move(file_path, new_path)

            log.append(f"Moved: {file} → {folder}")
            moved = True
            break

    if not moved:
        others_path = os.path.join(downloads_path, "Others")
        os.makedirs(others_path, exist_ok=True)

        new_path = os.path.join(others_path, file)
        shutil.move(file_path, new_path)

        log.append(f"Moved: {file} → Others")

# Write log file
with open(log_file_path, "w") as f:
    f.write("Downloads Cleanup Log\n")
    f.write("======================\n\n")
    for entry in log:
        f.write(entry + "\n")

# Print results
print("Downloads cleaned!\n")

print("===== LOG SUMMARY =====")
for entry in log:
    print(entry)
print(f"\nLog saved to: {log_file_path}")
