import PySimpleGUI as pyGUI
import time
import utils

input_label = pyGUI.Text("Write in a todo: ")
input_box = pyGUI.InputText(tooltip="Type a todo",key="todo")

time_label = pyGUI.Text('', key="clock")

list_box = pyGUI.Listbox(values=utils.get_todos(),
                         key='todos',
                         size=(56, 10),
                         enable_events=True)

edit_button = pyGUI.Button("Edit", size=10)
delete_button = pyGUI.Button("Delete", size=10)
exit_button = pyGUI.Button("Exit", size=10)
add_button = pyGUI.Button("Add", size=10)

app = pyGUI.Window("My Todo App",
                   layout=[[time_label], [input_label],
                           [input_box, add_button],
                           [list_box],
                           [edit_button, delete_button, exit_button]],
                   font=("Montserrat", 18))
while True:
    event, values = app.read(timeout=200)
    app['clock'].update(time.strftime("%b %d, %Y at %I:%M:%S %p"))
    match event:
        case "Add":
            todos = utils.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            utils.set_todos(todos)
            app['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = utils.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                utils.set_todos(todos)
                app['todos'].update(values=todos)
            except IndexError:
                pyGUI.popup("Please select an item first!",
                            font=("Montserrat", 18),
                            title="Information")
        case "Delete":
            try:
                todo_to_delete = values['todos'][0]
                todos = utils.get_todos()
                todos.remove(todo_to_delete)
                utils.set_todos(todos)

                app['todos'].update(values=todos)
                app['todo'].update(value='')

            except IndexError:
                pyGUI.popup("Please select an item first!",
                            font=("Montserrat", 18),
                            title="Information")

        case "Exit":
            break
        case "todos":
            app['todo'].update(value=values['todos'][0])
        case pyGUI.WIN_CLOSED:
            break

app.close()
