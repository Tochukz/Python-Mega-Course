import glob

file_paths = glob.glob("files/*.txt")

for file_path in file_paths:
    with open(file_path) as file:
        print(file.read())