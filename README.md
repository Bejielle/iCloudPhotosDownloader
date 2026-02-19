# iCloud Photo Downloader

## Description

A simple and efficient Python script to automatically download and organize all your photos and videos from your iCloud account directly to your local machine.

## Features

- **Complete Authentication:** Supports Two-Factor Authentication (2FA) and Two-Step Verification (2SA) directly from the terminal.
- **Smart Organization:** Automatically sorts downloaded photos into subfolders based on their creation year.
- **Download Resume:** Checks if files already exist (and are not empty) to prevent duplicate downloads, which is ideal if the script gets interrupted.
- **Safe Filenames:** Automatically sanitizes special characters in filenames to ensure compatibility across all operating systems (Windows, macOS, Linux).

## Requirements

- [`Python`](https://www.python.org/)
- `pip` (Python package manager)

## Quick Start

Get the downloader up and running locally.

```bash
git clone https://github.com/Bejielle/iCloudPhotoDownloader
cd iCloudPhotoDownloader
pip install pyicloud
```
## Configuration

⚠️ **Security Warning**: The current script requires you to enter your Apple ID and password directly into the code. **Never** share or commit this file publicly if it contains your real credentials.

Open the script (`icloud.py`) in your code editor and modify the following variables at the beginning of the file:
```py
APPLE_ID = 'email@domain.com'
PASSWORD = 'password'
```
## CLI Commands

| Command                                 | Description                                  |
| --------------------------------------- | -------------------------------------------- |
| `pip install pyicloud`                             | Install the required dependency for the script.            |
| `python icloud.py`                              | Start the authentication and download process. |

## Generated Folder Structure

Once you run the script, it will create a main directory and sort your media automatically:

```
/YourProjectFolder
 ├── icloud.py
 └── /iCloudPhotos
     ├── /2021
     ├── /2022
     ├── /2023
     └── /Unknown (For photos without date metadata)
```

## License

This project is open-source and available under the [MIT License](https://github.com/Bejielle/iCloudPhotoDownloader/blob/master/LICENSE).
