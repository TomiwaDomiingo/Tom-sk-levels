def toDo_list_func(choice):
    toDo_list = ['write a code', 'water the plants', 'get some groceries', 'Get a bike', 'sleep']
    
    if choice == "2":
        return toDo_list
    
    if choice == "3":
        marked_task = toDo_list.pop()
        return marked_task
    
    if choice == "4":
        deleted_task = toDo_list.pop()
        return deleted_task
    
    if choice == "1":
        toDo_list.append('get that bag')
        return toDo_list
    
    else:
        return "invalid"