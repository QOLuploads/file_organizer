# File Organizer

A small Python command-line tool that cleans up a messy folder (like your Downloads) by moving each file into a subfolder based on its type.

```
Before                      After
Downloads/                  Downloads/
├── vacation.jpg            ├── Images/
├── resume.pdf              │   └── vacation.jpg
├── setup.exe               ├── Documents/
├── song.mp3                │   └── resume.pdf
└── notes.txt               ├── Installers/
                            │   └── setup.exe
                            ├── Audio/
                            │   └── song.mp3
                            └── ...
```

## Features

- Sorts files into folders by extension (Images, Documents, Videos, Audio, Archives, Installers, Other)
- **Dry-run mode** to preview changes before moving anything
- **Safe with duplicates**: if a file with the same name already exists, the new one is renamed (`photo_1.jpg`) instead of being overwritten
- Works on any folder, defaults to your Downloads folder
- No external dependencies, just the Python standard library

## Requirements

- Python 3.8 or newer

## Installation

```bash
git clone https://github.com/QOLuploads/file-organizer.git
cd file-organizer
```

## Usage

Organize your Downloads folder (the default):

```bash
python main.py
```

Organize a specific folder:

```bash
python main.py "C:\Users\You\Desktop"
```

Preview what would happen without moving any files:

```bash
python main.py --dry-run
```

Show all options:

```bash
python main.py --help
```

### Example output

```
$ python main.py --dry-run
[DRY RUN] vacation.jpg -> Images/
[DRY RUN] resume.pdf -> Documents/
[DRY RUN] setup.exe -> Installers/
[DRY RUN] mystery.xyz -> Other/
```

## Default categories

| Folder       | Extensions                                |
|--------------|-------------------------------------------|
| Images       | .jpg, .jpeg, .png, .gif, .webp            |
| Documents    | .pdf, .docx, .txt, .xlsx, .pptx           |
| Videos       | .mp4, .mov, .avi, .mkv                    |
| Audio        | .mp3, .wav, .flac                         |
| Archives     | .zip, .rar, .7z                           |
| Installers   | .exe, .msi, .dmg                          |
| Other        | Anything not listed above                 |

## Customizing

To add or change categories, edit the `CATEGORIES` dictionary at the top of `main.py`:

```python
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Code": [".py", ".js", ".html", ".css"],  # add your own
}
```

## Important notes

- Moving files cannot be undone automatically. Try `--dry-run` first, especially on important folders.
- Only files directly inside the chosen folder are organized. Existing subfolders are left untouched.

## Contributing

Suggestions and pull requests are welcome. Ideas for future improvements:

- Undo the last organization
- Configurable categories through a settings file
- Standalone `.exe` for users without Python

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
