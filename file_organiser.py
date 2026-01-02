import os
import shutil

def create_folders(path, categories):
    for category in categories:
        folder = os.path.join(path, category)
        if not os.path.exists(folder):
            os.mkdir(folder)
            print(f"Created folder: {category}")

def move_files(path, categories):
    moved_count = {category: 0 for category in categories}

    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            continue
        for category, extensions in categories.items():
            if file.lower().endswith(tuple(extensions)):
                try:
                    dest = os.path.join(path, category, file)
                    shutil.move(file_path, dest)
                    moved_count[category] += 1
                except Exception as e:
                    print(f"Error moving {file}: {e}")

    print("\nOrganization complete!")
    for category, count in moved_count.items():
        print(f"{category}: {count} file(s) moved")


def organise_files(path):
    categories = {
        "Text Files": [".txt"],
        "Images": [".jpg", ".png", ".jpeg"],
        "PDFs": [".pdf"]
    }
    create_folders(path, categories)
    move_files(path, categories)

folder_path = input("Enter folder path to organise: ")
organise_files(folder_path)
