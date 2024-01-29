

print("Type 'help' to get all of the command!")
while True:
    command = input(">> ").lower().strip()

    if command.startswith("add"):
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()
        todo = command[4:] + "\n"
        todos.append(todo)

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    elif command.startswith("show"):
        print("Your Todos: ")
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()
        for index, todo in enumerate(todos):
            todo = todo.strip("\n")
            print(f"{index + 1}. {todo}")

    elif command.startswith("edit"):
        number = int(command[5:])
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        todo = input("Enter a todo: ")
        index = number - 1
        print(f"Todo '{todos[index].strip("\n")}' has been edited.")

        todos[index] = todo + "\n"

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    elif command.startswith("delete"):
        number = int(command[7:])
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()
            index = number - 1
            todo_to_delete = todos[index].strip("\n")
        todos.pop(index)
        print(f"Todo '{todo_to_delete}' has been deleted.")
        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    elif command.startswith("remove"):
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        todos.pop()
        print("The last todo has been removed.")
        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    elif command.startswith("help"):
        with open("files/help.txt", "r") as get_file:
            helps = get_file.readlines()
        for get_help in helps:
            get_help = get_help.strip("\n")
            print(get_help)

    elif command.startswith("exit"):
        print("Thanks for using this program!")
        break

    else:
        print("Unknown command!")
