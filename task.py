class Task:

  def __init__(self, title, description, completed, person):
    self.title = title
    self.description = description
    self.completed = completed
    self.person = person

  def complete(self):
    self.completed = True

  def details(self):
    return "\nTitle: " + self.title + "\nDescription: " + self.description + "\nPerson: " + self.person

  def __str__(self):
    return f"[{'X' if self.completed else ' '}] {self.title}"
