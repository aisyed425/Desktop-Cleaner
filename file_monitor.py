#Make sure you replace all placeholders with the required text 
#Credits: 


import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ==========================================
# 🔧 USER CONFIGURATION
# Replace these paths with your own folders
# ==========================================
folder_to_track = 'PATH/TO/FOLDER_TO_WATCH'        # e.g. '/Users/yourname/Desktop'
folder_destination = 'PATH/TO/FOLDER_DESTINATION'  # e.g. '/Users/yourname/Desktop/moved_files'


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        """
        Called when a change is detected in the tracked folder.
        Moves all files from the source folder to the destination folder.
        If a file with the same name exists, it appends a number to make it unique.
        """
        for filename in os.listdir(folder_to_track):
            # Skip the destination folder itself
            if filename == os.path.basename(folder_destination):
                continue

            src = os.path.join(folder_to_track, filename)
            new_name = filename
            name, ext = os.path.splitext(filename)
            i = 1

            # Ensure unique file names in the destination
            while os.path.exists(os.path.join(folder_destination, new_name)):
                new_name = f"{name}_{i}{ext}"
                i += 1

            destination_path = os.path.join(folder_destination, new_name)

            # Move the file
            try:
                os.rename(src, destination_path)
                print(f"Moved: {src} -> {destination_path}")
            except Exception as e:
                print(f"Error moving {filename}: {e}")


if __name__ == "__main__":
    # Ensure the destination folder exists
    if not os.path.exists(folder_destination):
        os.makedirs(folder_destination)
        print(f"Created destination folder: {folder_destination}")

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_to_track, recursive=True)
    observer.start()

    print(f"Monitoring folder: {folder_to_track}")
    print(f"Moving files to: {folder_destination}")
    print("Press CTRL + C to stop.\n")

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
        print("Stopping observer...")

    observer.join()
    print("Observer stopped.")
