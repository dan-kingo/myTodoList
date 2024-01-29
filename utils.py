def get_todos(path="files/todos.txt"):
    with open(path, "r") as file:
        todos = file.readlines()
    return todos


def get_help(path="files/help.txt"):
    with open(path, "r") as get_file:
        helps = get_file.readlines()
        return helps


def set_todos(my_todos, path="files/todos.txt"):
    with open(path, "w") as file:
        file.writelines(my_todos)


if __name__ == "__main__":
    print("The logic is here!")
