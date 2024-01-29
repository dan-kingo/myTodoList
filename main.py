
todos = []

print("Type 'help' to get all of the command!")
while True:
    command = input(">> ").lower().strip()

    if command == "add":
        todo = input("Enter a todo: ")
        todos.append(todo)

    elif command == "show":
        for todo in todos:
            print(todo)

    elif command == "edit":
        number = int(input("Enter a number to edit: "))
        todo = input("Enter a todo: ")
        todos[number - 1] = todo

    elif command == "delete":
        number = int(input("Enter a number to delete: "))
        todos.pop(number - 1)

    elif command == "remove":
        todos.pop()

    elif command == "help":
        print("""
use the commands below:

add - to add a new todo
show - to show the todo 
edit - to edit the todo 
delete - to delete the todo
remove - to remove the todo
help - to show the commands
exit - to exit the program

        """)

    elif command == "exit":
        print("Thanks for using this program!")
        break

    else:
        print("Unknown command!")
