# Text File Searcher

This Python script searches for a specific string within all text files inside a given directory. If the string is found within a file, the script will print the filename.

## Features
- Case insensitive search: Regardless of the case of your search string or the content of the text files, the script will find matches.
- Efficient: Only scans `.txt` files within the specified directory.

## Usage

1. Clone this repository to your machine.
2. Modify the script to search for your desired string and directory.
3. Run the script.

Example:

```
found_in_files = search_in_text_files('Searchstring', '/path/to/your/directory')
print(found_in_files)
for each in found_in_files:
    print(each)
```

## Functionality

### `search_in_text_files(string, directory)`

- `string`: The substring you're searching for.
- `directory`: The path to the directory containing `.txt` files to search within.

Returns a list of filenames that contain the given string.

## Requirements

This script requires Python 3.x and no additional libraries.
