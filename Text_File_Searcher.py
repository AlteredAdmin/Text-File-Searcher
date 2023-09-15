import os


def search_in_text_files(string, directory):
    # Create an empty list to store the filenames that contain the search string
    found_in_files = []

    # Convert the search string to lowercase
    string = string.lower()

    # Iterate through all the files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a text file
        if filename.endswith('.txt'):
            # Open the file and search for the string
            with open(os.path.join(directory, filename), 'r') as f:
                # Read the contents of the file and convert them to lowercase
                contents = f.read().lower()
                if string in contents:
                    # If the string is found, add the filename to the list
                    found_in_files.append(filename)

    return found_in_files


# Test the function
found_in_files = search_in_text_files('Searchstring', '/home/administrator/txtfiles')
print(found_in_files)
for each in found_in_files:
    print(each)
