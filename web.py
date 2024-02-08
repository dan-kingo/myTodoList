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
        new_todo = ""

# Update the display with the new todos

for i, todo in enumerate(todos):
    checkbox_key = f"checkbox_{i}_{todo.replace(' ', '_')}"
    checkbox = st.checkbox(f'{todo}', key=checkbox_key)
    if checkbox:
        todos.pop(i)
        utils.set_todos(todos)
        del st.session_state[checkbox_key]
        st.experimental_rerun()
