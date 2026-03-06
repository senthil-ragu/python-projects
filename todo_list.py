def print_menu():
    # Display the main menu options
    print('\nTodo List Menu:')
    print('1. View Tasks')
    print('2. Add a Task')
    print('3. Remove a Task')
    print('4. Exit')


def get_choice():
    """Prompt the user to enter a valid menu choice."""
    valid_choices = ('1', '2', '3', '4')

    while True:
        choice = input('Enter your choice: ')
        if choice in valid_choices:
            return choice
        print('Invalid choice. Please try again.')


def display_tasks(tasks):
    """Display all tasks in the todo list."""
    if not tasks:
        print('No tasks in the list.')
        return

    for index, task in enumerate(tasks, start=1):
        print(f'{index}. {task}')


def add_task(tasks):
    """Add a new task to the list."""
    while True:
        task = input('Enter a new task: ').strip()
        if task:
            tasks.append(task)
            print('Task added successfully.')
            break
        print('Invalid task. Please enter a valid task.')


def remove_task(tasks):
    """Remove a task from the list based on its number."""
    if not tasks:
        print('No tasks to remove.')
        return

    display_tasks(tasks)

    while True:
        try:
            task_number = int(input('Enter the task number to remove: '))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f'Task "{removed_task}" removed successfully.')
                break
            else:
                raise ValueError
        except ValueError:
            print('Invalid task number. Please try again.')


def main():
    """Main function to run the todo list application."""
    tasks = []

    while True:
        print_menu()
        choice = get_choice()

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print('Exiting Todo List. Goodbye!')
            break


if __name__ == '__main__':
    main()
