# Metadata Cleaner

Metadata Cleaner is a Python program designed to remove metadata from files. It ensures your files are free from any metadata that may contain sensitive or unwanted information.

## Features

- Remove metadata from files.
- Supports multiple file formats.

## Requirements

- Python 3.6+
- Required Python packages are listed in the requirements.txt file.
- `MediaInfo` library for extracting video metadata (if needed).
- `ffmpeg` library for extracting video metadata (if needed).

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/Metadata-Cleaner.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd Metadata-Cleaner
   ```   

3. **Install the required dependencies** (creating a virtual environment is strongly recommended):
   ```bash
   pip install -r requirements.txt
   ```

4. **Add a file**: Add as many files as you want in the clean folder.

5. **Run the application**:
   ```bash
   python3 main.py
   ```
6. **Check the files**: The files are in the results folder

## Installing MediaInfo for Video Metadata Extraction

#### Ubuntu/Debian

```bash
sudo apt-get update
sudo apt-get install mediainfo
```

#### Red Hat-based systems (Fedora, CentOS, etc.)

```bash
sudo dnf install mediainfo
```

#### macOS

```bash
brew install media-info
```

#### Windows

Download and install MediaInfo from the official [MediaInfo website](https://mediaarea.net/en/MediaInfo/Download/Windows).

## Installing ffmpeg for Video Metadata Extraction

##### Ubuntu/Debian
```sh
sudo apt-get update
sudo apt-get install ffmpeg
```

##### On Red Hat-based systems (Fedora, CentOS, etc.)
```sh
sudo dnf install ffmpeg
```

##### On macOS:
```sh
brew install ffmpeg
```

##### On Windows:
Download and install the FFmpeg release package from the [official FFmpeg website](https://ffmpeg.org/download.html).

## License
This project is licensed under the GNU General Public License - see the [LICENSE](LICENSE) file for details.

## Notes
Feel free to contribute or report issues! This README provides a clear structure, concise information, and instructions for setting up and running the Food Table Reader. Adjust the content as needed for your project.