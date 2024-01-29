import utils
import time

today = time.strftime("%b %d, %Y at %I:%M:%S %p")

print("Today's date is: ", today)
print("Type 'help' to get all of the command!")

while True:
    command = input(">>> ").lower().strip()

    if command.startswith("add"):
        todos = utils.get_todos()

        todo = command[4:] + "\n"
        todos.append(todo)

        utils.set_todos(todos)

    elif command.startswith("show"):
        print("Your Todos: \n")
        todos = utils.get_todos()

        for index, todo in enumerate(todos):
            todo = todo.strip("\n")
            print(f"{index + 1}. {todo}")

    elif command.startswith("edit"):
        number = int(command[5:])
        todos = utils.get_todos()

        todo = input("Enter a new todo: ")
        index = number - 1
        print(f"Todo '{todos[index].strip("\n")}' has been edited.")

        todos[index] = todo + "\n"

        utils.set_todos(todos)

    elif command.startswith("delete"):
        number = int(command[7:])

        todos = utils.get_todos()

        index = number - 1
        todo_to_delete = todos[index].strip("\n")
        todos.pop(index)

        print(f"Todo '{todo_to_delete}' has been deleted.")

        utils.set_todos(todos)

    elif command.startswith("remove"):
        todos = utils.get_todos()

        todos.pop()
        print("The last todo has been removed.")
        utils.set_todos(todos)

    elif command.startswith("help"):

        helps = utils.get_help()

        for get_help in helps:
            get_help = get_help.strip("\n")
            print(get_help)

    elif command.startswith("exit"):
        print("Thanks for using this program!")
        break

    else:
        print("Unknown command!")
