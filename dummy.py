# import re
# import os

# # Set the root of the workspace to the current working directory
# workspace_root = os.getcwd()

# # Set the base directory and the attachment directory
# base_dir = '.'
# attachment_dir = 'z'

# # Recursively search for .md files in all subdirectories
# for root, dirs, files in os.walk(workspace_root):
#     # Calculate the relative depth of the current directory
#     depth = root[len(workspace_root):].count(os.sep)






# import re
# import os

# # Set the root of the workspace to the current working directory
# # workspace_root = os.getcwd()

# workspace_root = os.path.abspath('.')


# # Set the base directory and the attachment directory
# base_dir = '.'
# attachment_dir = 'z'

# # Open the link_blocks.md file
# with open('/Users/aharo/programming/playground/expirimental_aharo24/publi_dev/link_blocks/link_blocks.md', 'r') as f:
#     # Read the file contents
#     contents = f.read()

# # Use a regular expression to find links in the file
# links = re.findall(r'\[(.*?)\]\((.*?)\)', contents)

# # Iterate over the links
# for link in links:
#     # Extract the link text and destination file
#     text, dest = link
#     # Check if the destination file is in the attachment directory
#     if dest.startswith(attachment_dir):
#         # Update the link to point to the correct directory
#         new_link = '[{}](../{})'.format(text, dest)
#         # Use string replacement to update the link in the file contents
#         contents = contents.replace(f'[{text}]({dest})', new_link)

# # Save the updated contents to a new file
# with open('link_blocks_fixed.md', 'w') as f:
#     f.write(contents)




# import re
# import os

# # Set the root of the workspace to the current working directory
# workspace_root = os.getcwd()

# # Set the base directory and the attachment directory
# base_dir = '.'
# attachment_dir = 'z'

# # Open the link_blocks.md file
# with open('/Users/aharo/programming/playground/expirimental_aharo24/publi_dev/link_blocks/link_blocks.md', 'r') as f:
#     # Read the file contents
#     contents = f.read()

# # Use a regular expression to find links in the file
# links = re.findall(r'\[([^\[\]]*)\]\(([^\(\)]*)\)', contents)

# # Iterate over the links
# for link in links:
#     # Extract the link text and destination file
#     text, dest = link
#     # Check if the destination file is in the attachment directory
#     if dest.startswith(attachment_dir):
#         # Update the link to point to the correct directory
#         new_link = '[{}](../{})'.format(text, dest)
#         # Use string replacement to update the link in the file contents
#         contents = contents.replace(f'[{text}]({dest})', new_link)

# # Save the updated contents to a new file
# with open('link_blocks_fixed.md', 'w') as f:
#     f.write(contents)




# import os
# import re

# # Set the root of the workspace to the current working directory
# workspace_root = os.getcwd()

# # Set the base directory and the attachment directory
# base_dir = '.'
# attachment_dir = 'z'

# # Open the link_blocks.md file
# with open('/Users/aharo/programming/playground/expirimental_aharo24/publi_dev/link_blocks/link_blocks.md', 'r') as f:
#     # Read the file contents
#     contents = f.read()

# # Use a regular expression to find links in the file
# links = re.findall(r'\[([^\[\]]*)\]\(([^\(\)]*)\)', contents)

# # Iterate over the links
# for link in links:
#     # Extract the link text and destination file
#     text, dest = link
#     # Construct the full path to the destination file
#     dest_path = os.path.join(base_dir, dest)
#     # Extract the directory name from the full path
#     dest_dir = os.path.dirname(dest_path)
#     # Check if the directory name is equal to the attachment_dir
#     if dest_dir == attachment_dir:
#         # Update the link to point to the correct directory
#         new_link = '[{}](../{})'.format(text, dest)
#         # Use string replacement to update the link in the file contents
#         contents = contents.replace(f'[{text}]({dest})', new_link)

# # Save the updated contents to a new file
# with open('link_blocks_fixed.md', 'w') as f:
#     f.write(contents)








# import re
# import os

# # Set the root of the workspace to the current working directory
# workspace_root = os.getcwd()

# # Recursively search for .md files in all subdirectories
# for root, dirs, files in os.walk(workspace_root):
#     for file_name in files:
#         if file_name.endswith('.md'):
#             # Construct the full path to the file
#             file_path = os.path.join(root, file_name)

#             # Open the input file in read mode
#             with open(file_path, 'r') as file:
#                 # Read the contents of the file into a string
#                 contents = file.read()

#             # Use a regular expression to find all instances of the pattern "[name](path#^id)"
#             pattern = r'\[.+\]\(([\w\d_./]+)\#\^[\w\d]+\)'
#             matches = re.findall(pattern, contents)
#             print(f"Found {len(matches)} matches in {file_name}: {matches}")

#             # Iterate through the matches and replace them with the desired pattern "[name](path#id)"
#             for match in matches:
#                 # Replace the caret (^) symbol with an empty string
#                 new_path = match.replace('^', '')
#                 replacement = f'[name]({new_path})'
#                 contents = contents.replace(match, replacement)

#             # Open the input file in write mode
#             with open(file_path, 'w') as file:
#                 # Write the modified contents back to the input file
#                 file.write(contents)






# import re
# import os

# # Set the root of the workspace to the current working directory
# workspace_root = os.getcwd()

# # Recursively search for .md files in all subdirectories
# for root, dirs, files in os.walk(workspace_root):
#     for file_name in files:
#         if file_name.endswith('.md'):
#             # Construct the full path to the file
#             file_path = os.path.join(root, file_name)

#             # Open the input file in read mode
#             with open(file_path, 'r') as file:
#                 # Read the contents of the file into a string
#                 contents = file.read()

#             # Use a regular expression to find all instances of the pattern "[name](path#^id)"
#             pattern = r'\[.+\]\(([\w\d_./]+)\#\^[\w\d]+\)'
#             matches = re.findall(pattern, contents)
#             print(f"Found {len(matches)} matches in {file_name}: {matches}")

#             # Iterate through the matches and replace them with the desired pattern "[name](path#id)"
#             for match in matches:
#                 # Replace the caret (^) symbol with an empty string
#                 new_path = match.replace('^', '')
#                 replacement = f'[name]({new_path})'
#                 contents = contents.replace(match, replacement)

#             # Open the input file in write mode
#             with open(file_path, 'w') as file:
#                 # Write the modified contents back to the input file
#                 file.write(contents)



import re
import os

# Set the root of the workspace to the current working directory
workspace_root = os.getcwd()

# Recursively search for .md files in all subdirectories
for root, dirs, files in os.walk(workspace_root):
    for file_name in files:
        if file_name.endswith('.md'):
            # Construct the full path to the file
            file_path = os.path.join(root, file_name)

            # Open the input file in read mode
            with open(file_path, 'r') as file:
                # Read the contents of the file into a string
                contents = file.read()

            # Use a regular expression to find all instances of the pattern "[name](path#id)"
            pattern = r'\[.+\]\(([\w\d_./]+)\#[\w\d]+\)'
            matches = re.findall(pattern, contents)
            print(f"Found {len(matches)} matches in {file_name}: {matches}")

            # Replace the links in the file
            contents = re.sub(pattern, r'[name](\1)', contents)

            # Open the file in write mode
            with open(file_path, 'w') as file:
                # Write the updated contents to the file
                file.write(contents)
