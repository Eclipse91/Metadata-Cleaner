# Metadata Cleaner

Metadata Cleaner is a Python program designed to remove metadata from files. It ensures your files are free from any metadata that may contain sensitive or unwanted information.

## Features

- Remove metadata from files.
- Supports multiple file formats.
- Option to overwrite the original file or save a new file without metadata.

## Requirements

- Python 3.6+
- `mutagen` library for handling audio metadata.
- `pymediainfo` and the `MediaInfo` library for extracting video metadata (if needed).

## Installing MediaInfo Library

#### Ubuntu/Debian

```bash
sudo apt-get update
sudo apt-get install libmediainfo0v5
sudo apt-get install libmediainfo-dev
```

#### Fedora

```bash
sudo dnf install libmediainfo
sudo dnf install libmediainfo-devel
```

#### macOS (using Homebrew)

```bash
brew install media-info
```

#### Windows

Download and install MediaInfo from the official [MediaInfo website](https://mediaarea.net/en/MediaInfo/Download/Windows).

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

4. **Add a file**: Add a file in the root.

5. **Run the application**:
   ```bash
   python3 main.py
   ```
6. **Check the files**: The files are in the results folder


## License
This project is licensed under the GNU General Public License - see the [LICENSE](LICENSE) file for details.

## Notes
Feel free to contribute or report issues! This README provides a clear structure, concise information, and instructions for setting up and running the Food Table Reader. Adjust the content as needed for your project.