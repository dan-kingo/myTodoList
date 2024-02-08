import streamlit as st
import utils

# Retrieve existing todos
todos = utils.get_todos()

# Display existing todos
st.title("TO-DO App")
st.write("Minimalistic todo app")


# Text input for adding new todo
new_todo = '\n' + st.text_input(label="", placeholder="add new todo...", key="new_todo")

# Button to add new todo
if st.button("Add Todo"):
    if new_todo:
        todos.append(new_todo)
        utils.set_todos(todos)


# Update the display with the new todos
for i, todo in enumerate(todos):
    checkbox = st.checkbox(f'{todo}', key=todo)
    if checkbox:
        todos.pop(i)
        utils.set_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
