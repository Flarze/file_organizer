# A file organizer that sorts the downloads folder into different categories based on the files extension.
# Images (.png .svg .jpg .jpeg .gif .AVIF and .WebP)
# Docs (.docx .pdf .txt .odt .rtf .md .csv .json)
# Videos (.mp4 .mov .mkv .avi .wmv .webm)
# Music (.mp3 .wav .flac .aac .m4a)
# Programs (.exe .jar .bin .msi .sh .py .js .bat)
# Other (anything not listed before)
# Duplicate files are appended with (amount + 1)
# Creates destination folder if it doesn't exist yet.
# When does prints an exit message such as "successfully sorted folder" or "failed to sort folder"

import argparse
from pathlib import Path

EXTENSIONS = {
    "images": (".png", ".svg", ".jpg", ".jpeg", ".gif", ".avif", ".webp"),
    "docs": (".txt", ".docx", ".pdf", ".odt", ".rtf", ".md", ".csv", ".json"),
    "videos": (".mp4", ".mov", ".mkv", ".avi", ".wmv", ".webm"),
    "music": (".mp3", ".wav", ".flac", ".aac", ".m4a"),
    "programs": (".exe", ".jar", ".bin", ".msi", ".sh", ".py", ".js", ".bat"),
}

# Parse CLI for folder Path
parser = argparse.ArgumentParser()
parser.add_argument("folder", type=Path)
parser.add_argument("--dry-run", action="store_true")
args = parser.parse_args()
abspath = args.folder


# Get category of items at Path
def get_category(file: Path):
    for category, ext in EXTENSIONS.items():
        if file.suffix.lower() in ext:
            return category
    return "other"


# Check if file name already exists to handle duplicates
def unique_dest(dest: Path):
    if not dest.exists():
        return dest
    counter = 1
    while True:
        uniquedest = dest.with_name(f"{dest.stem} ({counter}){dest.suffix}")
        if not uniquedest.exists():
            return uniquedest
        counter += 1


def sort_file(file: Path):
    if not args.dry_run:
        category = get_category(file)
        dest = unique_dest(abspath / category / file.name)
        file.rename(dest)
        print(f"Moved {file.name} -> {category}/{dest.name}")
    else:
        category = get_category(file)
        dest = unique_dest(abspath / category / file.name)
        print(f"Would Have Moved {file.name} -> {category}/{dest.name}")


def main():
    # Create Folders at Path if not yet exists
    if args.dry_run:
        print("[Dry Run] Enabled. No Changes Will Be Made")
    for category in EXTENSIONS:
        Path(abspath / category).mkdir(exist_ok=True)

    # Main Function
    for file in abspath.iterdir():
        if file.is_file():
            sort_file(file)

    print("Files Successfully Sorted")


if __name__ == "__main__":
    main()
