tasks = []

while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
         if len(tasks) == 0:
            print("No tasks found!")
         else:
           for i, task in enumerate(tasks,1):
               print(i,task)

    elif choice == "3":
        task_number = int(input("Enter task number to remove: "))

        if task_number >=1 and task_number <=len(tasks):
            tasks.pop(task_number - 1)
            print("task remove!")
        else:
            print("Invalid task number!")

    elif choice == "4":
        print("Todo list closed!")
        break