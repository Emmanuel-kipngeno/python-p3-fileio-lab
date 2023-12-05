def write_file(file_name, file_content):
    """
    Write content to a .txt file.

    :param file_name: The name of the file without extension.
    :type file_name: str
    :param file_content: The content to be written to the file.
    :type file_content: str
    """
    file_name_with_extension = f"{file_name}.txt"
    with open(file_name_with_extension, 'w') as file:
        file.write(file_content)


def append_file(file_name, append_content):
    """
    Append content to a .txt file.

    :param file_name: The name of the file without extension.
    :type file_name: str
    :param append_content: The content to be appended to the file.
    :type append_content: str
    """
    file_name_with_extension = f"{file_name}.txt"
    with open(file_name_with_extension, 'a') as file:
        file.write(append_content)


def read_file(file_name):
    """
    Read content from a .txt file.

    :param file_name: The name of the file without extension.
    :type file_name: str
    :return: The content of the file.
    :rtype: str
    """
    file_name_with_extension = f"{file_name}.txt"
    with open(file_name_with_extension, 'r') as file:
        return file.read()
