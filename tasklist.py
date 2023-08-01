  
class TaskList:
  def __init__(self):
    self.list = []

  def addTask(self, task):
    self.list.append(task)

  def removeTask(self, task):
    self.list.remove(task)

  def clear(self):
    self.list.clear()

  def printList(self):
    print("\nTODO List:\n")
    if (len(self.list) == 0):
      print("EMPTY LIST")
      return
    for index, task in enumerate(self.list):
      print(f"{index}. {task}")