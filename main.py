import argparse
import shutil
from pathlib import Path

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Installers": [".exe", ".msi", ".dmg"],
}


def get_category(file: Path) -> str:
    """Return the category folder name for a file, based on its extension."""
    extension = file.suffix.lower()
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    return "Other"


def get_free_destination(destination: Path) -> Path:
    """If the file already exists, add _1, _2, etc. to the name."""
    if not destination.exists():
        return destination
    counter = 1
    while True:
        new_path = destination.with_name(
            f"{destination.stem}_{counter}{destination.suffix}"
        )
        if not new_path.exists():
            return new_path
        counter += 1


def organize(folder: Path, dry_run: bool = False):
    """Move every file in the folder into a subfolder by file type."""
    for file in folder.iterdir():
        if file.is_dir():
            continue  # skip subfolders

        category = get_category(file)
        destination = folder / category

        if not dry_run:
            destination.mkdir(exist_ok=True)
            shutil.move(str(file), str(get_free_destination(destination / file.name)))

        prefix = "[DRY RUN] " if dry_run else ""
        print(f"{prefix}{file.name} -> {category}/")


def main():
    parser = argparse.ArgumentParser(
        description="Organize a folder by moving files into subfolders by type."
    )
    parser.add_argument(
        "folder",
        nargs="?",
        default=str(Path.home() / "Downloads"),
        help="Folder to organize (default: Downloads)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would happen without moving any files",
    )
    args = parser.parse_args()

    folder = Path(args.folder)
    if not folder.is_dir():
        print(f"Error: '{folder}' is not a valid folder.")
        return

    organize(folder, args.dry_run)


if __name__ == "__main__":
    main()