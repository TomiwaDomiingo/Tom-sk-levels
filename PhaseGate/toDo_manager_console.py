def toDo_manager_console():
    toDo_list = []  

    print("\nTODO LIST MANAGER")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark a task as complete")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Pick an option: ")

    while choice != "5":
        if choice == "1":
            print('Add a task')
            new_task = input("Enter the task: ")
            toDo_list.append(new_task)
            print("Task added")

        if choice == "2":
            print(toDo_list)  # Print the list
            print("Current tasks displayed")

        if choice == "3":
            print('Mark a task')
            if toDo_list:  # Check if list is not empty
                print("Current tasks:", toDo_list)
                index = input("Enter task number to mark complete (1-{}): ".format(len(toDo_list)))
                if index.isdigit() and 1 <= int(index) <= len(toDo_list):  # Validate input
                    completed_task = toDo_list.pop(int(index) - 1)  # Remove task
                    print(f"Marked '{completed_task}' as complete")
                else:
                    print("Invalid task number")
            else:
                print("No tasks to mark as complete")

        if choice == "4":
            print('Select a task to delete')
            if toDo_list:
                print("Current tasks:", toDo_list)
                index = input("Enter task number to delete (1-{}): ".format(len(toDo_list)))
                if index.isdigit() and 1 <= int(index) <= len(toDo_list):
                    deleted_task = toDo_list.pop(int(index) - 1)
                    print(f"Deleted '{deleted_task}'")
                else:
                    print("Invalid task number")
            else:
                print("No tasks to delete")

        if choice == "5":
            print("Exiting To-Do List Manager")
            break

        else:
            print("Invalid option, please choose 1-5")

        print("\nTODO LIST MANAGER")  
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark a task as complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Pick an option: ")

toDo_manager_console()