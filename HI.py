#some comment here
import functions
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print('it is', now)

while True:
    user_action = input('type add, complete, show, edit, or exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos, 'todos.txt')

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f'{index + 1} - {item}')
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input('enter new todo')
            todos[number] = new_todo + '\n'

            functions.write_todos(todos, 'todos.txt')
        except ValueError:
            print('Your command is not valid')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos, 'todos.txt')

            message = (f'Todo {todo_to_remove} was removed from the list')
            print(message)
        except IndexError:
            print('There is no item with that number')
            continue

    elif 'exit' in user_action:
        break
    else:
        print('command is not valid')


