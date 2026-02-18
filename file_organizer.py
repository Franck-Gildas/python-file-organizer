import argparse
import os
import shutil
from datetime import datetime

LOG_FILE = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "organizer.log")


def log(message):
    """Append a timestamped message to organizer.log (UTF-8, append mode)."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {message}\n")


parser = argparse.ArgumentParser(
    description="Organize files into category folders.")
parser.add_argument(
    "--dry-run",
    action="store_true",
    help="Preview actions without moving files",
)
args = parser.parse_args()
dry_run = args.dry_run

if dry_run:
    print("DRY RUN MODE — No files will be moved.\n")

log("=== New run started (dry-run mode)" if dry_run else "=== New run started (real mode)")

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

summary = {category: 0 for category in categories}


# Determines the category of a file based on its extension.
def get_category(filename, categories):
    _, ext = os.path.splitext(filename)
    ext = ext.lower()
    for category, extensions in categories.items():
        if category == "Other":
            continue
        if ext in extensions:
            return category
    return "Other"


# Create a subdirectory for each category if it doesn't already exist.
if not dry_run:
    for category in categories:
        dir_path = os.path.join(folder_path, category)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

print(categories)

print("\nFiles moved:")
print("-------------")
# Loop through all files in the folder_path and move them to their corresponding category folders.
for name in os.listdir(folder_path):
    path = os.path.join(folder_path, name)
    if os.path.isfile(path):
        category = get_category(name, categories)
        dest_path = os.path.join(folder_path, category, name)
        dest_name = name
        if os.path.exists(dest_path):
            base, ext = os.path.splitext(name)
            n = 1
            while True:
                dest_name = f"{base} ({n}){ext}"
                dest_path = os.path.join(folder_path, category, dest_name)
                if not os.path.exists(dest_path):
                    break
                n += 1
        if dry_run:
            if dest_name != name:
                print(
                    f"  [DRY RUN] Would move {name} → {category} (renamed to {dest_name})")
                log(f"[DRY RUN] Would move {name} → {category} (renamed to {dest_name}).")
            else:
                print(f"  [DRY RUN] Would move {name} → {category}")
                log(f"[DRY RUN] Would move {name} → {category}.")
        else:
            shutil.move(path, dest_path)
            summary[category] += 1
            if dest_name != name:
                print(f"  - {name:<30} -> {category} (renamed to {dest_name})")
                log(f"Moved {name} → {category} (renamed to {dest_name}).")
            else:
                print(f"  - {name:<30} -> {category}")
                log(f"Moved {name} → {category}.")

print("\nSummary of Files Moved:")
for category, count in summary.items():
    print(f"  {category}: {count}")
log(f"Summary of Files Moved: {summary}")
