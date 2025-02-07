# MP3-Title-Updater
Update titles of all MP3 files in the current directory

#  Info

This Python script updates the title tag of all MP3 files in a specified directory to match their filenames (without the file extension). It uses the `mutagen` library to manipulate ID3 tags in MP3 files.

## Features

- Automatically updates the title of each MP3 file to its corresponding filename.
- Handles both existing title tags and creates new ones if they do not exist.
- Processes all MP3 files in the specified directory.

## Requirements

- Python 3.x
- `mutagen` library

You can install the `mutagen` library using pip:

```bash
pip install mutagen
```

### Usage
- Clone or download this repository to your local machine.
- Navigate to the directory containing the script.
- Run the script. It will update the titles of all MP3 files in the current directory. bash

```bash
python main.py
```
