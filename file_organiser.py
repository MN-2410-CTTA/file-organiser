import os

def organise_files(path):
    files = os.listdir(path)
    print("Found files: ")
    for file in files:
        print("-", file)

folder_path = input("Enter folder path to organise: ")
organise_files(folder_path)
