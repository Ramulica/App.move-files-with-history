import shutil
import os


def get_file_location() -> str:
    """
    This function gets a correct file path as input
    :return: file path
    """


def get_future_file_location() -> str:
    """
    This function gets a correct folder path as input
    :return: file path
    """


def get_file_type(path):
    """
    This function gets the file type from fis path
    :return:
    """


def move_file_to_future_position(file_path: str, future_file_path: str):
    """
    Function moves the selected file to a selected location
    :return:
    """


def read_moved_file():
    """
    reads and returns what is written in the log file as a list
    (don't forget to remove the enters from every item)
    :return:
    """


def available_file_type(content: list) -> list:
    """
    creates a list with all file types added in moved_files.txt
    :param content:
    :return:
    """


def modify_log_file(old_content: list, file_extension):
    """
    Function overwrites the existent content in moved_files.txt with the updated information
    ex: if you move a text file, you need to add 1 to the corresponding dile type and 1 at the total
    :return:
    """


def add_file_type_in_moved_files(file_extension: str):
    """
    if there is no row in modified_files.txt for the file type you want to move, The function adds it
    :return:
    """


file_path = get_file_location()
file_future_path = get_future_file_location()

if get_file_type(file_path) not in available_file_type(read_moved_file()):
    add_file_type_in_moved_files(get_file_type(file_path))

modify_log_file(read_moved_file(), get_file_type(file_path))

move_file_to_future_position(file_path, file_future_path)

