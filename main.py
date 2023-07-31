from task import Task
from tasklist import TaskList

import os, sys

toDOList = TaskList()


def printList():
  print("\nTODO List:\n")
  if(len(toDOList.list) == 0):
    print("EMPTY LIST")
    return
  for index, task in enumerate(toDOList.list):
    print(f"{index}. {task}")


def createTask():
  title = input("Write the title: ")
  description = input("Write the description: ")
  person = input("Write the name of who is reponsible: ")
  newTask = Task(title, description, False, person)
  toDOList.addTask(newTask)
  print("\nTask added successfully\n")


def removeTask():
  printList()
  index = int(input("\nWrite the index of the task: "))
  toDOList.removeTask(toDOList.list[index])
  print("\nTask removed successfully\n")


def markTask():
  printList()
  index = int(input("\nWrite the index of the task: "))
  toDOList.list[index].complete()


def seeTaskDetails():
  printList()
  index = int(input("\nWrite the index of the task: "))
  print(toDOList.list[index].details())


def printMenu():
  print("\nTO-DO List Manager\n")
  print("1. Add New Task")
  print("2. List All Tasks")
  print("3. Clear Task List")
  print("4. Remove Task")
  print("5. Mark Task as completed")
  print("6. See Task details")
  print("7. Exit")


def processOption(option):
  if (option == 7):
    sys.exit()
  elif (option == 1):
    createTask()
  elif (option == 2):
    printList()
  elif (option == 3):
    toDOList.clear()
    print("\nTO-DO List Cleared Successfully\n")
  elif (option == 4):
    removeTask()
  elif (option == 5):
    markTask()
  elif (option == 6):
    seeTaskDetails()

  input("\nPress ENTER to continue...")


while True:
  os.system('clear')
  printMenu()

  opt = int(input("\nPick an option: "))
  processOption(opt)
