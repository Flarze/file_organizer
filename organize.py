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

import os
import sys
from pathlib import Path

print(os.listdir("./downloads"))

DIRS = (
    "./downloads/images",
    "./downloads/docs",
    "./downloads/videos",
    "./downloads/music",
    "./downloads/programs",
    "./downloads/other",
)

IMAGES = (".png", ".svg", ".jpg", ".jpeg", ".gif", ".avif", ".webp")
DOCS = (".txt", ".docx", ".pdf", ".odt", ".rtf", ".md", ".csv", ".json")
VIDEOS = (".mp4", ".mov", ".mkv", ".avi", ".wmv", ".webm")
MUSIC = (".mp3", ".wav", ".flac", ".aac", ".m4a")
PROGRAMS = (".exe", ".jar", ".bin", ".msi", ".sh", ".py", ".js", ".bat")

if os.getcwd().endswith("/file_organizer"):
    print("Running Organizer")
    for dir in DIRS:
        try:
            os.mkdir(dir)
        except FileExistsError:
            pass
else:
    print("Run In Downloads Folder")
    sys.exit()


for file in os.listdir("./downloads"):
    path = Path(f"./downloads/{file}")
    target = Path(f"./downloads/images/{file}")

    if not path.is_file():
        continue

    # Images
    if file.endswith(IMAGES):
        if not Path(f"./downloads/images/{file}").is_file():
            path.rename(f"./downloads/images/{file}")
            print("Sorted")
        else:
            counter = 1
            while os.path.exists(
                f"./downloads/images/{path.stem} ({counter}){path.suffix}"
            ):
                counter += 1
            path.rename(f"./downloads/images/{path.stem} ({counter}){path.suffix}")

    # Docs
    elif file.endswith(DOCS):
        if not Path(f"./downloads/docs/{file}").is_file():
            path.rename(f"./downloads/docs/{file}")
            print("Sorted")
        else:
            counter = 1
            while os.path.exists(
                f"./downloads/docs/{path.stem} ({counter}){path.suffix}"
            ):
                counter += 1
            path.rename(f"./downloads/docs/{path.stem} ({counter}){path.suffix}")

    # Videos
    elif file.endswith(VIDEOS):
        if not Path(f"./downloads/videos/{file}").is_file():
            path.rename(f"./downloads/videos/{file}")
            print("Sorted")
        else:
            counter = 1
            while os.path.exists(
                f"./downloads/videos/{path.stem} ({counter}){path.suffix}"
            ):
                counter += 1
            path.rename(f"./downloads/videos/{path.stem} ({counter}){path.suffix}")

    # Music
    elif file.endswith(MUSIC):
        if not Path(f"./downloads/music/{file}").is_file():
            path.rename(f"./downloads/music/{file}")
            print("Sorted")
        else:
            counter = 1
            while os.path.exists(
                f"./downloads/music/{path.stem} ({counter}){path.suffix}"
            ):
                counter += 1
            path.rename(f"./downloads/music/{path.stem} ({counter}){path.suffix}")

    # Programs
    elif file.endswith(PROGRAMS):
        if not Path(f"./downloads/programs/{file}").is_file():
            path.rename(f"./downloads/programs/{file}")
            print("Sorted")
        else:
            counter = 1
            while os.path.exists(
                f"./downloads/programs/{path.stem} ({counter}){path.suffix}"
            ):
                counter += 1
            path.rename(f"./downloads/programs/{path.stem} ({counter}){path.suffix}")

    # Other
    else:
        if not Path(f"./downloads/other/{file}").is_file():
            path.rename(f"./downloads/other/{file}")
            print("Sorted")
        else:
            counter = 1
            while os.path.exists(
                f"./downloads/other/{path.stem} ({counter}){path.suffix}"
            ):
                counter += 1
            path.rename(f"./downloads/other/{path.stem} ({counter}){path.suffix}")

print("Files Successfully Sorted")
