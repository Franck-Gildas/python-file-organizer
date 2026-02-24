---

📄 README.md

# File Organizer CLI

A lightweight, fast, and user friendly command line tool that automatically organizes files into category based folders.  
Built with clarity, safety, and real world workflows in mind — featuring dry run previews, verbose logging, quiet mode, and clean summaries.

---

## 🚀 Features

- **Automatic file categorization**  
  Sorts files into folders like `Images`, `Documents`, `PDFs`, `Videos`, `Audio`, `Archives`, and `Other`.

- **Dry run mode**  
  Preview all actions without moving any files.

- **Verbose mode**  
  See detailed logs of every decision and action.

- **Quiet mode**  
  Suppress all output except errors.

- **Default path behavior**  
  If no `--path` is provided, the tool organizes the current working directory.

- **Logging**  
  All operations are recorded in `organizer.log` with timestamps.

- **Idempotent**  
  Safe to run multiple times — already organized files are not moved again.

---

## 📦 Installation

### Optional: Create a virtual environment

This is recommended to keep your Python tools isolated:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
________________________________________
Standard installation (most users)
python -m pip install .
This installs the tool normally into your Python environment.
________________________________________
Editable installation (useful when working on the code)
If you want your local changes to take effect immediately without reinstalling each time:
python -m pip install -e .
Editable mode links the installed command to your project folder, making it easier to test and iterate while modifying the code.
________________________________________
🧠 Usage
Organize the current directory
file-organizer
Organize a specific folder
file-organizer --path "C:\Downloads"
________________________________________
🔍 Dry Run Mode (Safe Preview)
Preview all actions without moving files:
file-organizer --dry-run --path "C:\Downloads"
________________________________________
📢 Verbose Mode
Show detailed logs of every action:
file-organizer --verbose --path "C:\Downloads"
________________________________________
🤫 Quiet Mode
Suppress all output except errors:
file-organizer --quiet --path "C:\Downloads"
________________________________________
🗂 Categories
Files are automatically sorted into:
Category	Extensions (examples)
Images	.jpg, .jpeg, .png, .gif, .bmp
Documents	.txt, .docx, .xlsx, .csv
PDFs	.pdf
Videos	.mp4, .mov, .avi
Audio	.mp3, .wav
Archives	.zip, .rar, .7z
Other	Everything else
________________________________________
🧪 Full Test Suite
Use this checklist to verify all features:
1. Help command
file-organizer --help
2. Dry run mode
file-organizer --dry-run --path "C:\test-organizer"
3. Real run
file-organizer --path "C:\test-organizer"
4. Default path behavior
cd C:\test-organizer
file-organizer
5. Verbose mode
file-organizer --verbose --path "C:\test-organizer"
6. Quiet mode
file-organizer --quiet --path "C:\test-organizer"
7. Logging
Check:
organizer.log
8. Unknown extensions
Ensure .xyz files go to Other.
9. Nested folders
Tool should NOT recurse into subfolders.
10. Repeated runs
Running twice should move 0 files the second time.
11. Invalid path
file-organizer --path "C:\does-not-exist"
________________________________________
🧰 Tech Stack
•	Python 3.13
•	Standard library only:
o	os
o	shutil
o	argparse
o	logging
o	pathlib
No external dependencies.
________________________________________
🎯 Why This Project Exists
I built this tool to solve a real world problem:
keeping messy folders (especially Downloads) clean and organized automatically.
It also serves as a demonstration of:
•	clean CLI design
•	robust error handling
•	user friendly options
•	logging and idempotent behavior
•	packaging a Python project into an installable command line tool
This project is part of my growing portfolio of automation tools.
________________________________________
🛠 Development
If you're working on the codebase, editable mode makes it easy to test changes:
python -m pip install -e .
Use the test suite above to validate behavior.
________________________________________
📌 Roadmap
•	Recursive mode (optional)
•	Custom category configuration file
•	JSON output mode
•	Progress bar
•	Duplicate file handling
•	PyPI release
________________________________________
📄 License
MIT License
________________________________________
👤 Author
Franck Gildas Kamga
Bathurst, NB, Canada
GitHub: https://github.com/Franck-Gildas
LinkedIn: https://www.linkedin.com/in/frankygildas/
```
