import os
import shutil

folder_path = r"C:\Users\frank\OneDrive\Desktop\test_downloads"

categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".ico"],
    "Documents": [".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".ppt", ".odt", ".rtf"],
    "PDFs": [".pdf"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".webm", ".m4v"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "Other": [],
}


def get_category(filename, categories):
    _, ext = os.path.splitext(filename)
    ext = ext.lower()
    for category, extensions in categories.items():
        if category == "Other":
            continue
        if ext in extensions:
            return category
    return "Other"


for category in categories:
    dir_path = os.path.join(folder_path, category)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

print(categories)

for name in os.listdir(folder_path):
    path = os.path.join(folder_path, name)
    if os.path.isfile(path):
        category = get_category(name, categories)
        dest_path = os.path.join(folder_path, category, name)
        shutil.move(path, dest_path)
        print(f"Moved {name} to {category}")
