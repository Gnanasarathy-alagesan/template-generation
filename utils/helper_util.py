import shutil
import os

def move_file(src, dst):
    try:
        shutil.move(src, dst)
        print(f"File moved from {src} to {dst}")
    except FileNotFoundError:
        print(f"File not found: {src}")
    except Exception as e:
        print(f"Error occurred: {e}")


def copy_file(src, dst):
    try:
        shutil.copy(src, dst)
        print(f"File copied from {src} to {dst}")
    except FileNotFoundError:
        print(f"File not found: {src}")
    except Exception as e:
        print(f"Error occurred: {e}")


def move_all_files(src_dir, dst_dir):
    try:
        # Create destination directory if it doesn't exist
        os.makedirs(dst_dir, exist_ok=True)
        
        # Iterate through all files in the source directory
        for filename in os.listdir(src_dir):
            src_file = os.path.join(src_dir, filename)
            dst_file = os.path.join(dst_dir, filename)
            
            # Move file
            if os.path.isfile(src_file):  # Ensure it's a file
                shutil.move(src_file, dst_file)
                print(f"Moved: {src_file} -> {dst_file}")
                
    except FileNotFoundError:
        print(f"Source directory not found: {src_dir}")
    except Exception as e:
        print(f"Error occurred: {e}")


def copy_all_files(src_dir, dst_dir):
    try:
        # Create destination directory if it doesn't exist
        os.makedirs(dst_dir, exist_ok=True)
        
        # Iterate through all files in the source directory
        for filename in os.listdir(src_dir):
            src_file = os.path.join(src_dir, filename)
            dst_file = os.path.join(dst_dir, filename)
            
            # Copy file
            if os.path.isfile(src_file):  # Ensure it's a file
                shutil.copy(src_file, dst_file)
                print(f"Copied: {src_file} -> {dst_file}")
                
    except FileNotFoundError:
        print(f"Source directory not found: {src_dir}")
    except Exception as e:
        print(f"Error occurred: {e}")
