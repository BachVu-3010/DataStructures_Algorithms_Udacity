import os

# Code to demonstrate the use of some of the OS modules in python

# Let us print all the files in the directory in which you are running this script

path = os.getcwd() + "\\testdir"


def find_files(suffix, path):

    directories = os.listdir(path)
    files = []

    for dir in directories:

        dir_path = os.path.join(path, dir)

        if os.path.isdir(dir_path):
            files += find_files(suffix, dir_path)
            # Here we don't use append to avoid add empty string into our list
        elif os.path.isfile(dir_path) and dir_path.endswith(suffix):
            files.append(dir_path)

    return files

    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """


list = find_files(suffix=".c", path=path)
print(list)
