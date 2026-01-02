import os

def organise_files(path):
    files = os.listdir(path)
    print("Found files: ")
    for file in files:
        print("-", file)

    categories = {
    "Text Files": [".txt"],
    "Images": [".jpg", ".png", ".jpeg"],
    "PDFs": [".pdf"]
    }

    for category in categories:
        folder = os.path.join(path, category)
        if not os.path.exists(folder):
            os.mkdir(folder)
            print(f"Created folder: {category}")

    import shutil

    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        # Skip directories
        if os.path.isdir(file_path):
            continue
        for category, extensions in categories.items():
            if file.lower().endswith(tuple(extensions)):
                dest = os.path.join(path, category, file)
                shutil.move(file_path, dest)
                print(f"Moved {file} → {category}")

folder_path = input("Enter folder path to organise: ")
organise_files(folder_path)
