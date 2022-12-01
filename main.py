import shutil
import os


def get_file_location() -> str:
    """
    input file path
    :return: file path
    """
    file_path = input("What is the file path of the file you want to move?")
    while not os.path.isfile(file_path):
        file_path = input("file path of the location was wrong. Try again")
    return file_path


def get_future_file_location() -> str:
    """
    input future file path
    :return: file path
    """
    file_path = input("What is the path of the future location?")
    while not os.path.isdir(file_path):
        file_path = input("the path was wrong. Try again")
    return file_path


def get_file_type(path):
    """
    function returns file type from path
    :return:
    """
    return os.path.basename(path)[os.path.basename(path).rfind(".") + 1::]


def move_file_to_future_position(file_path: str, future_file_path: str):
    """
    Function moves the selected file to a selected location
    :return:
    """
    shutil.move(file_path, future_file_path)


def read_moved_file():
    """
    reads and returns what is written in the log file
    :return:
    """
    with open("moved_files.txt", "r") as fr:
        content = fr.readlines()

    return [item.strip() for item in content]


def available_file_type(content: list) -> list:
    """
    creates a list with all file types added in moved_files.txt
    :param content:
    :return:
    """
    return [item[0:item.find(" ")] for item in content][1::]


def modify_log_file(old_content: list, file_extension):
    """
    Function overwrites the existent content in moved_files.txt with the updated information
    :return:
    """
    with open("moved_files.txt", "w") as fw:
        for item in old_content:
            if item[0:item.find(" ")] == "Total":
                updated_total_number = int(item[item.rfind(":") + 1::]) + 1
                fw.write(item[0:item.rfind(":") + 2] + str(updated_total_number) + "\n")
            elif file_extension == item[0:item.find(" ")]:
                updated_number = int(item[item.rfind(":") + 1::]) + 1
                fw.write(item[0:item.rfind(":") + 2] + str(updated_number) + "\n")
            else:
                fw.write(item + "\n")


def add_file_type_in_moved_files(file_extension: str):
    """
    if there is no row in modified_files.txt for the file type you want to move, The function adds it
    :return:
    """
    with open("moved_files.txt", "a") as fa:
        fa.write(f"{file_extension} files moved: 0")

# move_file_to_future_position(get_file_location(), get_future_file_location())

# print(available_file_type(read_moved_file()))


file_path = get_file_location()
file_future_path = get_future_file_location()

if get_file_type(file_path) not in available_file_type(read_moved_file()):
    add_file_type_in_moved_files(get_file_type(file_path))

modify_log_file(read_moved_file(), get_file_type(file_path))

move_file_to_future_position(file_path, file_future_path)

