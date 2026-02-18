# File Organizer Automation

A simple and effective Python script that automatically organizes files into category folders based on their extensions. It supports:

- Automatic category detection
- Folder creation
- Safe file moving
- Duplicate filename handling (`file (1).ext`, `file (2).ext`, etc.)
- A summary of how many files were moved per category

This project is part of my automation learning journey and serves as a clean, portfolio‑ready example of practical scripting.

---

## Features

### ✔ Categorizes files into:

- Images
- Documents
- PDFs
- Videos
- Audio
- Archives
- Other

### ✔ Handles duplicate filenames

Automatically renames files using `(1)`, `(2)`, etc.

### ✔ Prints a summary

Shows how many files were moved into each category.

---

## How to Use

1. Clone the repository
2. Edit the `folder_path` variable in `file_organizer.py` to point to the folder you want to organize
3. Run:

```bash
python file_organizer.py

```
