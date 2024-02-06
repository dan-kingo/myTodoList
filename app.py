import PySimpleGUI as pyGUI

import utils

input_label = pyGUI.Text("Write in a todo: ")
input_box = pyGUI.InputText(tooltip="Type a todo",
                            key="todo")
list_box = pyGUI.Listbox(values=utils.get_todos(),
                         key='todos',
                         size=(50, 10),
                         enable_events=True)

edit_button = pyGUI.Button("Edit")
delete_button = pyGUI.Button("Delete")
exit_button = pyGUI.Button("Exit")
add_button = pyGUI.Button("Add")

app = pyGUI.Window("My Todo App",
                   layout=[[input_label],
                           [input_box, add_button],
                           [list_box],
                           [edit_button, delete_button, exit_button]],
                   font=("Montserrat", 18))
while True:
    event, values = app.read()

    match event:
        case "Add":
            todos = utils.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            utils.set_todos(todos)
            app['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = utils.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            utils.set_todos(todos)
            app['todos'].update(values=todos)

        case "Delete":
            todo_to_delete = values['todos'][0]
            todos = utils.get_todos()
            todos.remove(todo_to_delete)
            utils.set_todos(todos)

            app['todos'].update(values=todos)
            app['todo'].update(value='')

        case "Exit":
            break
        case "todos":
            app['todo'].update(value=values['todos'][0])
        case pyGUI.WIN_CLOSED:
            break

app.close()
