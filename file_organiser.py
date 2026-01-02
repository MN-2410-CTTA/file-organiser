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

folder_path = input("Enter folder path to organise: ")
organise_files(folder_path)
