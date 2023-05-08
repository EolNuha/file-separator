# File Separator

This repository contains a simple script for separating files based on their extensions. It is useful for organizing a messy directory or for grouping similar files together.

## How to Use

1. Clone this repository to your local machine.
2. Navigate to the directory containing the `main.py` script.
3. Run the script by entering `python main.py` in your terminal.
4. The script will create four subdirectories in the directory you specified, one for documents, images, videos, and audios. Files with each extension will be moved into their respective subdirectory.

For example, if you run `python main.py`, the script will create subdirectories such as `images`, `documents`, and `videos`, and move all image, document, and video files, respectively, into their corresponding directories.

## Note

- If a file with the same name already exists in the destination directory, it will be overwritten.
- Hidden files (files starting with `.`) will not be moved.
- The script only sorts files in the directory you specify, and does not search subdirectories.

## Executable File

If you want to create an executable file, please install **pyinstaller**, by running the command below:

```python
pip install pyinstaller
```

Then go to the directory of the project and run the following command to create the executable file:

```python
pyinstaller main.py --onefile
```

## Contributing

If you find any issues with this script or have suggestions for improvement, please feel free to submit an issue or pull request.
