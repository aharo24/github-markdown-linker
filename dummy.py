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

#             # Use a regular expression to find all instances of the pattern "[name](path#id)"
#             pattern = r'\[.+\]\(([\w\d_./]+)\#[\w\d]+\)'
#             matches = re.findall(pattern, contents)
#             print(f"Found {len(matches)} matches in {file_name}: {matches}")

#             # Replace the links in the file
#             contents = re.sub(pattern, r'[name](\1)', contents)

#             # Open the file in write mode
#             with open(file_path, 'w') as file:
#                 # Write the updated contents to the file
#                 file.write(contents)







# import re
# import os

#     # Set the root of the workspace
#     # workspace_root = '/Users/aharo/z/aharo24'


# # Set the root of the workspace to the current working directory
# workspace_root = os.getcwd()

# # Set the base directory and the attachment directory
# base_dir = '.'
# attachment_dir = 'z'

# # Recursively search for .md files in all subdirectories
# for root, dirs, files in os.walk(workspace_root):
#     # Calculate the relative depth of the current directory
#     depth = root[len(workspace_root):].count(os.sep)
#     # Construct the relative path to the attachment directory
#     attachment_path = os.sep.join(['..'] * depth + [attachment_dir])
#     for file_name in files:
#         if file_name.endswith('.md'):
#             # Construct the full path to the file
#             file_path = os.path.join(root, file_name)

#             # Open the input file in read mode
#             with open(file_path, 'r') as file:
#                 # Read the contents of the file into a string
#                 contents = file.read()

#             # Use a regular expression to find all instances of the pattern "![](file_name)"
#             pattern = r'!\[\]\(([\w\d_.]+)\)'
#             matches = re.findall(pattern, contents)
#             print(f"Found {len(matches)} matches in {file_name}: {matches}")

#             # Iterate through the matches and replace them with the desired pattern "![](z/file_name)"
#             for match in matches:
#                 # Calculate the new path by adding the relative path to the attachment directory
#                 # to the front of the file name
#                 new_path = os.path.join(attachment_path, match)
#                 replacement = f'![]({new_path})'
#                 contents = contents.replace(f'![]({match})', replacement)

#             # Open the input file in write mode
#             with open(file_path, 'w') as file:
#                 # Write the modified contents back to the input file
#                 file.write(contents)













# import re

# def percent_encode_carets(markdown_string):
#   # Find all links that contain a caret (^) symbol in their link target
#   caret_links = re.findall(r'\[.+\]\(.+\^.+\)', markdown_string)
  
#   # Replace the caret (^) symbol with its percent-encoded equivalent (%5E)
#   for link in caret_links:
#     markdown_string = markdown_string.replace(link, link.replace('^', '%5E'))
  
#   return markdown_string

# # Example usage
# markdown_string = "[how does this look?](cars.md#^8f98eb)"
# print(percent_encode_carets(markdown_string))  # Output: "[how does this look?](cars.md#%5E8f98eb)"



# import re

# def fix_relative_paths(markdown_string, source_dir, target_dir):
#   # Find all links that contain a relative path
#   relative_links = re.findall(r'\[.+\]\(.+\.md\)', markdown_string)
  
#   # Replace the relative path with the correct path
#   for link in relative_links:
#     fixed_link = link.replace(source_dir, target_dir)
#     markdown_string = markdown_string.replace(link, fixed_link)
  
#   return markdown_string

# # Example usage
# markdown_string = "[link_header](link_blocks/link_header.md)"
# source_dir = "link_blocks"
# target_dir = "../link_header"
# print(fix_relative_paths(markdown_string, source_dir, target_dir))  # Output: "[link_header](../link_header/link_header.md)"



# import re

# def fix_relative_paths(markdown_string, source_dir, target_dir):
#   # Find all links that contain a relative path
#   relative_links = re.findall(r'\[.+\]\(.+\)', markdown_string)
  
#   # Replace the relative path with the correct path
#   for link in relative_links:
#     fixed_link = link.replace(source_dir, target_dir)
#     markdown_string = markdown_string.replace(link, fixed_link)
  
#   return markdown_string

# # Example usage
# markdown_string = "[link_header](link_blocks/link_header.md)"
# source_dir = "link_blocks"
# target_dir = "../link_header"
# print(fix_relative_paths(markdown_string, source_dir, target_dir))  # Output: "[link_header](../link_header/link_header.md)"



# import re

# def fix_relative_links(markdown_string, source_path, target_path):
#   # Find all relative links in the markdown string
#   relative_links = re.findall(r'\[.+\]\(\.\/.+\)', markdown_string)
  
#   # Replace the relative links with links that use the target path
#   for link in relative_links:
#     fixed_link = link.replace('./', target_path)
#     markdown_string = markdown_string.replace(link, fixed_link)
  
#   return markdown_string

# # Example usage
# markdown_string = "[link_header](../link_header/link_header.md#nospace)"
# source_path = "publi_dev/link_blocks/link_blocks.md"
# target_path = "publi_dev/link_header/link_header.md"
# print(fix_relative_links(markdown_string, source_path, target_path))  # Output: "[link_header](publi_dev/link_header/link_header.md#nospace)"


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
            pattern = r'!\[\]\(([\w\d_./]+)\)'
            matches = re.findall(pattern, contents)
            print(f"Found {len(matches)} matches in {file_name}: {matches}")

            # Iterate through the matches and replace them with the desired pattern "![](z/file_name)"
            for match in matches:
                # Check if the file path is already correct
                if not match.startswith('../z/'):
                    # Calculate the new path by adding the relative path to the attachment directory
                    # to the front of the file name
                    attachment_path = os.path.join(base_dir, attachment_dir)
                    attachment_path = os.path.relpath(attachment_path, os.path.dirname(file_path))
                    new_path = os.path.join(attachment_path, match)
                    replacement = f'![]({new_path})'
                    contents = contents.replace(f'![]({match})', replacement)

            # Open the input file in write mode
            with open(file_path, 'w') as file:
                # Write the modified contents back to the input file
                file.write(contents)
