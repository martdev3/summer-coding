def main():
    startingList = []
    startingID = 1
    mainMenu(startingList, startingID)

def mainMenu(taskList, id):
    while True:
        printMenu()
        choice = input(">  ").strip()
        if choice == "1":
            id = addTasks(taskList, id)
        elif choice == "2":
            listTasks(taskList)
        elif choice == "3":
            completeTask(taskList)
        elif choice == "4":
            deleteTask(taskList)
        elif choice == "5":
            print('goodbye')
            break
        else:
            print('Not an option')

def printMenu():
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark task done")
    print("4. Delete task")
    print("5. Quit")

def addTasks(tasks, next_id):
    text = input("Task description: ").strip()
    if not text:
        print("Task can't be empty")
        return next_id
    tasks.append({"id": next_id, "text": text, "done": False})
    print(f"Added task #{next_id}")
    return next_id + 1

def listTasks(taskList):
    if len(taskList) == 0:
        print("No tasks yet.")
        return
    for task in taskList:
        status = "[X]" if task["done"] == True else "[ ]"
        print(f"{status} {task["id"]}: {task["text"]}")

def completeTask(taskList):
    taskNum = input("Enter task number: ")
    try:
        int(taskNum)
    except ValueError:
        print("That is not a number")
        return
    for i in range(len(taskList)):
        idNumber = taskList[i]["id"]
        if idNumber == taskNum:
            taskList[i]["done"] = True
            return
    print("No such task exists")


def deleteTask(taskList):
    taskNum = input("Enter task number: ")
    try:
        int(taskNum)
    except ValueError:
        print("That is not a number")
        return
    for i in range(len(taskList)):
        idNumber = taskList[i]["id"]
        if idNumber == int(taskNum):
            taskList.pop(i)
            return
    print("No such task exists")



if __name__ == "__main__":
    main()