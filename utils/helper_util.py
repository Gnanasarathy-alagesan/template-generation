import os
import shutil


def move_file(src: str, dst: str) -> None:
    """
    Moves a file from the source (src) to the destination (dst).

    Args:
        src (str): The path of the source file.
        dst (str): The path of the destination where the file will be moved.

    Returns:
        None
    """
    try:
        shutil.move(src, dst)
        print(f"File moved from {src} to {dst}")
    except FileNotFoundError:
        print(f"File not found: {src}")
    except Exception as e:
        print(f"Error occurred: {e}")


def copy_file(src: str, dst: str) -> None:
    """
    Copies a file from the source (src) to the destination (dst).

    Args:
        src (str): The path of the source file.
        dst (str): The path of the destination where the file will be copied.

    Returns:
        None
    """
    try:
        shutil.copy(src, dst)
        print(f"File copied from {src} to {dst}")
    except FileNotFoundError:
        print(f"File not found: {src}")
    except Exception as e:
        print(f"Error occurred: {e}")


def move_all_files(src_dir: str, dst_dir: str) -> None:
    """
    Moves all files from the source directory to the destination directory.

    Args:
        src_dir (str): The path of the source directory.
        dst_dir (str): The path of the destination directory.

    Returns:
        None
    """
    try:
        # Create destination directory if it doesn't exist
        os.makedirs(dst_dir, exist_ok=True)

        # Iterate through all files in the source directory
        for filename in os.listdir(src_dir):
            src_file = os.path.join(src_dir, filename)
            dst_file = os.path.join(dst_dir, filename)

            # Move the file if it's a file (not a directory)
            if os.path.isfile(src_file):
                shutil.move(src_file, dst_file)
                print(f"Moved: {src_file} -> {dst_file}")

    except FileNotFoundError:
        print(f"Source directory not found: {src_dir}")
    except Exception as e:
        print(f"Error occurred: {e}")


def copy_all_files(src_dir: str, dst_dir: str) -> None:
    """
    Copies all files from the source directory to the destination directory.

    Args:
        src_dir (str): The path of the source directory.
        dst_dir (str): The path of the destination directory.

    Returns:
        None
    """
    try:
        # Create destination directory if it doesn't exist
        os.makedirs(dst_dir, exist_ok=True)

        # Iterate through all files in the source directory
        for filename in os.listdir(src_dir):
            src_file = os.path.join(src_dir, filename)
            dst_file = os.path.join(dst_dir, filename)

            # Copy the file if it's a file (not a directory)
            if os.path.isfile(src_file):
                shutil.copy(src_file, dst_file)
                print(f"Copied: {src_file} -> {dst_file}")

    except FileNotFoundError:
        print(f"Source directory not found: {src_dir}")
    except Exception as e:
        print(f"Error occurred: {e}")


def date_format(date, format: str) -> str:
    """
    Formats a date object into a string according to the specified format.

    Args:
        date (datetime): The date object to format.
        format (str): The format string, e.g., "%Y-%m-%d".

    Returns:
        str: The formatted date string.
    """
    try:
        return date.strftime(format)
    except Exception as e:
        print(f"Error occurred: {e}")


def get_columns(map_dict: dict) -> list:
    """
    Retrieves the 'header' values from a dictionary if the value is a dictionary,
    or retrieves the value itself if it's not a dictionary.

    Args:
        map_dict (dict): The dictionary containing column mappings.

    Returns:
        list: A list of column headers or values.
    """
    values = []
    for value in map_dict.values():
        if isinstance(value, dict):
            # If the value is a dictionary, retrieve the 'header' key
            values.append(value.get("header"))
        else:
            # Otherwise, append the value itself
            values.append(value)
    return values
