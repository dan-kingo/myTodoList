import utils
import time

"""
sample CLI based TODO list that provide different functionalities,

developed by @dan-kingo
visit my github page: https://github.com/dan-kingo/myTodoList
"""

today = time.strftime("%b %d, %Y at %I:%M:%S %p")

print("\nToday's date is: ", today)
print("Type 'help' to get all of the command!")

while True:
    command = input(">>> ").lower().strip()

    if command.startswith("add"):
        todos = utils.get_todos()
        if len(command) > 3:
            todo = command[4:] + "\n"

            todos.append(todo)
        else:
            print("Please add a note it is empty!")

        utils.set_todos(todos)

    elif command.startswith("show"):

        todos = utils.get_todos()
        if todos.__len__() > 0:
            print("Your Todos: \n")
            for index, todo in enumerate(todos):
                todo = todo.strip("\n")
                print(f"{index + 1}. {todo}")
        else:
            print("Your todo list is empty!")

    elif command.startswith("edit"):
        try:
            number = int(command[5:])
            todos = utils.get_todos()

            todo = input("Enter a new todo: ")

            index = number - 1
            todo_to_edit = todos[index].strip("\n")
            print(f"Todo '{todo_to_edit}' has been edited.")

            todos[index] = todo + "\n"

            utils.set_todos(todos)
        except ValueError:
            print("Please enter a valid command!")
            continue
    elif command.startswith("delete"):
        try:
            try:
                number = int(command[7:])

                todos = utils.get_todos()

                index = number - 1
                todo_to_delete = todos[index].strip("\n")
                todos.pop(index)

                print(f"Todo '{todo_to_delete}' has been deleted.")

                utils.set_todos(todos)
            except IndexError:
                print("here is no such todo to be deleted.")
        except ValueError:
            print("Please enter a valid command!")
            continue
    elif command.startswith("remove"):
        try:
            todos = utils.get_todos()

            todos.pop()
            print("The last todo has been removed.")
            utils.set_todos(todos)
        except IndexError:
            print("here is no such todo to be removed.")
            continue
    elif command.startswith("clear"):
        try:
            todos = utils.get_todos()
            todos.clear()

            print("The todo list has been cleared.")
            utils.set_todos(todos)

        except IndexError:
            print("Please enter a valid command!")

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
