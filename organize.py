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
    category = get_category(file)
    dest = unique_dest(abspath / category / file.name)
    if not args.dry_run:
        try:
            file.rename(dest)
            print(f"Moved {file.name} -> {category}/{dest.name}")
            return True
        except Exception as e:
            print(f"Failed to move {file.name}: {e}")
            return False
    else:
        print(f"Would Move {file.name} -> {category}/{dest.name}")


def main():
    # Create Folders at Path if not yet exists
    if not args.dry_run:
        for category in list(EXTENSIONS) + ["other"]:
            Path(abspath / category).mkdir(exist_ok=True)
    else:
        print("[Dry Run Enabled] - No Changes Will Be Made")

    sorted_files = 0
    # Main Function
    for file in abspath.iterdir():
        if file.is_file():
            if sort_file(file):
                sorted_files += 1
    if not args.dry_run:
        if sorted_files > 0:
            print(f"Sorted {sorted_files} Files")
        else:
            print("No Files Found")


if __name__ == "__main__":
    main()
