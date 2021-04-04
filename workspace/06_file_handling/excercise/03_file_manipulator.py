import os


def print_error_message():
    print("An error occurred")


def create_file(file_path):
    with open(file_path, "w") as file:
        file.write("")


def add_content_to_file(file_path, content):
    with open(file_path, "a") as file:
        file.write(content + "\n")


def replace_content_in_file(file_path, content, replacement):
    try:
        with open(file_path, "r+") as file:
            text = "".join(file.readlines())
            replaced_content = text.replace(content, replacement)
            file.seek(0)
            file.write(replaced_content)
    except FileNotFoundError:
        print_error_message()


def delete_file(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print_error_message()


def manage_files():
    cmd = input().split("-")
    while cmd[0] != "End":
        command_args = cmd[1:]
        manage_file_tools[cmd[0]](*command_args)
        cmd = input().split("-")


manage_file_tools = {
    "Create": create_file,
    "Add": add_content_to_file,
    "Replace": replace_content_in_file,
    "Delete": delete_file,
}

manage_files()
