import PySimpleGUI as pyGUI

input_label = pyGUI.Text("Write in a todo: ")
input_box = pyGUI.InputText(tooltip="Type a todo")
add_button = pyGUI.Button("add")

app = pyGUI.Window("My Todo App", layout=[[input_label], [input_box, add_button]])
app.read()
app.close()
