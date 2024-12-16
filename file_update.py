def edit_file(file_path, new_content):
    """
    Edits the file at the specified path with the new content.
    If the file doesn't exist, it will create it.

    :param file_path: Path to the file to edit.
    :param new_content: The content to write into the file.
    """
    try:
        # Open the file in write mode ('w') to overwrite its content
        with open(file_path, 'w') as file:
            file.write(new_content)
        print(f"File '{file_path}' has been updated.")
    except Exception as e:
        print(f"An error occurred: {e}")


def append_to_file(file_path, content_to_append):
    """
    Appends the given content to the file at the specified path.
    If the file doesn't exist, it will create it.

    :param file_path: Path to the file.
    :param content_to_append: Content to append to the file.
    """
    try:
        # Open the file in append mode ('a') to add content without overwriting
        with open(file_path, 'a') as file:
            file.write(content_to_append)
        print(f"Content has been appended to '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
file_path = "E:/Python/sample.txt"  # Replace with your file path

# To overwrite the content with new content
new_content = "This is the new content of the file."
edit_file(file_path, new_content)

# To append new content to the file
content_to_append = "\nThis is some additional content."
append_to_file(file_path, content_to_append)
