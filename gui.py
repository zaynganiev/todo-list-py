import FreeSimpleGUI.window
import functions
import FreeSimpleGUI

label = FreeSimpleGUI.Text("Type in a to-do")
input_box = FreeSimpleGUI.InputText(tooltip="Enter todo", key="todo")
add_button = FreeSimpleGUI.Button("Add")
list_box = FreeSimpleGUI.Listbox(values=functions.get_todos(), key='todos', 
                                 enable_events=True, size=[45, 10])
edit_button = FreeSimpleGUI.Button("Edit")
complete_button = FreeSimpleGUI.Button("Complete")
exit_button = FreeSimpleGUI.Button("Exit")

window = FreeSimpleGUI.Window('My To-Do App',
                               layout=[[label],
                                        [input_box, add_button],
                                        [list_box, edit_button, complete_button],
                                        [exit_button]], 
                               font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case "Exit":
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])
            
        case FreeSimpleGUI.WIN_CLOSED:
            break

window.close()
