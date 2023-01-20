
import re
import os

# Set the root of the workspace to the current working directory
workspace_root = os.getcwd()

# Set the base directory and the attachment directory
base_dir = '.'
attachment_dir = 'z'

# Recursively search for .md files in all subdirectories
for root, dirs, files in os.walk(workspace_root):
    # Calculate the relative depth of the current directory
    depth = root[len(workspace_root):].count(os.sep)
    # Construct the relative path to the attachment directory
    attachment_path = os.sep.join(['..'] * depth + [attachment_dir])
    for file_name in files:
        if file_name.endswith('.md'):
            # Construct the full path to the file
            file_path = os.path.join(root, file_name)

            # Open the input file in read mode
            with open(file_path, 'r') as file:
                # Read the contents of the file into a string
                contents = file.read()

            # Use a regular expression to find all instances of the pattern "![](file_name)"
            pattern = r'!\[\]\(([\w\d_\.\-%% ]+)\)'     # Works
            matches = re.findall(pattern, contents)
            print(f"Found {len(matches)} matches in {file_name}: {matches}")

            # Iterate through the matches and replace them with the desired pattern "![](z/file_name)"
            for match in matches:
                # Calculate the new path by adding the relative path to the attachment directory
                # to the front of the file name
                new_path = os.path.join(attachment_path, match)
                replacement = f'![]({new_path})'
                contents = contents.replace(f'![]({match})', replacement)

            # Open the input file in write mode
            with open(file_path, 'w') as file:
                # Write the modified contents back to the input file
                file.write(contents)



