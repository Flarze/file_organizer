# File Sorter

A simple Python script that sorts file into categories based on file extension.

## Categories

| Category | Extensions |
|----------|------------|
| `images` | `.png`, `.svg`, `.jpg`, `.jpeg`, `.gif`, `.avif`, `.webp` |
| `docs` | `.txt`, `.docx`, `.pdf`, `.odt`, `.rtf`, `.md`, `.csv`, `.json` |
| `videos` | `.mp4`, `.mov`, `.mkv`, `.avi`, `.wmv`, `.webm` |
| `music` | `.mp3`, `.wav`, `.flac`, `.aac`, `.m4a` |
| `programs` | `.exe`, `.jar`, `.bin`, `.msi`, `.sh`, `.py`, `.js`, `.bat` |
| `other` | Anything not matching the above |

## Requirements

- Python 3.6+
- No external dependencies

## Usage

```bash
python3 organize.py <folder>
```

### Dry run

Preview what would be moved without making any changes

```bash
python organize.py <folder> --dry-run
```

| Argument | Description |
|----------|-------------|
| `folder` | Path to the directory to sort (required) |
| `--dry-run` | Print planned moves without modifying the filesystem |

## Behavior

- Only files in the top level of the target folder are sorted. Subdirectories are ignored.
- Category folders are created inside the target folder if they don't exist.
- Duplicate filenames are appended with a counter: `file.txt`, `file (1).txt`, `file (2).txt`.

## Example

```bash
python organize.py ~/Downloads
```

Before:
```
Downloads/
├── photo.jpg
├── song.mp3
├── notes.txt
└── installer.exe
```

After:
```
Downloads/
├── images/
│   └── photo.jpg
├── music/
│   └── song.mp3
├── docs/
│   └── notes.txt
└── programs/
    └── installer.exe
```
