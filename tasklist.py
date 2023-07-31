  
class TaskList:
  def __init__(self):
    self.list = []

  def addTask(self, task):
    self.list.append(task)

  def removeTask(self, task):
    self.list.remove(task)

  def clear(self):
    self.list.clear()