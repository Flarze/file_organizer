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

print(os.listdir())

DIRS = (
    "./downloads/images",
    "./downloads/docs",
    "./downloads/videos",
    "./downloads/videos",
    "./downloads/music",
    "./downloads/programs",
    "./downloads/other",
)

IMAGES = (".png", ".svg", ".jpg", ".jpeg", ".gif", ".AVIF", ".WebP")
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


for file in os.listdir():
    if file.endswith(IMAGES):
        print("counted")
