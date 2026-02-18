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
parser.add_argument(
    "--path",
    type=str,
    default=None,
    help="Folder path to organize (default: current working directory)",
)
parser.add_argument(
    "--verbose",
    action="store_true",
    help="Enable extra detailed output",
)
parser.add_argument(
    "--quiet",
    action="store_true",
    help="Suppress almost all output except errors",
)
args = parser.parse_args()
dry_run = args.dry_run

if args.quiet:
    output_mode = "quiet"
elif args.verbose:
    output_mode = "verbose"
else:
    output_mode = "normal"


def print_msg(message, level="normal"):
    """Print message only if it matches the current output mode."""
    if output_mode == "quiet":
        if level == "error":
            print(message)
    elif output_mode == "normal":
        if level in ("normal", "error"):
            print(message)
    else:  # verbose
        print(message)


if dry_run:
    print_msg("DRY RUN MODE — No files will be moved.\n", level="normal")

log("=== New run started (dry-run mode)" if dry_run else "=== New run started (real mode)")

folder_path = args.path if args.path else os.getcwd()
if args.path:
    print_msg(f"Organizing folder: {folder_path}", level="normal")
else:
    print_msg(f"No --path provided. Using current working directory: {folder_path}", level="normal")

if not os.path.exists(folder_path):
    print_msg(f"Error: Path does not exist: {folder_path}", level="error")
    exit(1)
if not os.path.isdir(folder_path):
    print_msg(f"Error: Path is not a directory: {folder_path}", level="error")
    exit(1)

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

print_msg(str(categories), level="verbose")

print_msg("\nFiles moved:", level="normal")
print_msg("-------------", level="normal")
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
                print_msg(
                    f"  [DRY RUN] Would move {name} → {category} (renamed to {dest_name})", level="normal")
                log(f"[DRY RUN] Would move {name} → {category} (renamed to {dest_name}).")
            else:
                print_msg(f"  [DRY RUN] Would move {name} → {category}", level="normal")
                log(f"[DRY RUN] Would move {name} → {category}.")
        else:
            shutil.move(path, dest_path)
            summary[category] += 1
            if dest_name != name:
                print_msg(f"  - {name:<30} -> {category} (renamed to {dest_name})", level="normal")
                log(f"Moved {name} → {category} (renamed to {dest_name}).")
            else:
                print_msg(f"  - {name:<30} -> {category}", level="normal")
                log(f"Moved {name} → {category}.")

print_msg("\nSummary of Files Moved:", level="normal")
for category, count in summary.items():
    print_msg(f"  {category}: {count}", level="normal")
log(f"Summary of Files Moved: {summary}")
