import PySimpleGUI as pyGUI

import utils

input_label = pyGUI.Text("Write in a todo: ")
input_box = pyGUI.InputText(tooltip="Type a todo",
                            key="todo")
list_box = pyGUI.Listbox(values=utils.get_todos(),
                         key='todos',
                         size=(50, 10),
                         enable_events=True)

add_button = pyGUI.Button("Add")

app = pyGUI.Window("My Todo App",
                   layout=[[input_label], [input_box, add_button], [list_box]],
                   font=("Montserrat", 18))
while True:
    event, values = app.read()

    match event:
        case "Add":
            todos = utils.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            utils.set_todos(todos)

        case pyGUI.WIN_CLOSED:
            break

app.close()
