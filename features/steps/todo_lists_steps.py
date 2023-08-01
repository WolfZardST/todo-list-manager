from task import Task
from tasklist import TaskList
from behave import given, then, when, step

to_do_list = TaskList()
task = None

@given('the to-do list is empty')
def setp_impl(context):
  to_do_list.clear()


@when('the user adds a task with title "{title}" description "{description}" and person "{person}"')
def setp_impl(context, title, description, person):
  global task
  task = Task(title, description, False, person)
  to_do_list.addTask(task)


@then('the to-do list should contain task "{title}"')
def setp_impl(context, title):
  assert any(task.title == title for task in to_do_list.list), f'Task "{title}" not found'


@given('the to-do list contains task "{title}"')
def setp_impl(context, title):
  global task
  task = Task(title, "", False, "")
  to_do_list.addTask(task)


@when('the user clears the to-do list')
def setp_impl(context):
  to_do_list.clear()


@then('the to-do list should be empty')
def setp_impl(context):
  assert len(to_do_list.list) == 0, "The to-do list should be empty"


@given('the to-do list contains task in index {index} set completed as False')
def setp_impl(context, index):
  i_index = int(index)
  to_do_list.clear()
  global task
  task = Task("", "", False, "")
  to_do_list.addTask(task)
  task = to_do_list.list[i_index]
  task.completed = False

@when('the user marks a task with index {index}')
def setp_impl(context, index):
  i_index = int(index)
  to_do_list.list[i_index].complete()
  

@then('the to-do list should contain a task in index {index} marked True')
def setp_impl(context, index):
  i_index = int(index)
  assert to_do_list.list[i_index].completed == True, "The task is not completed"


@given('the to-do list contains tasks "{title}"')
def setp_impl(context, title):
  to_do_list.clear()
  global task
  task = Task(title, "", False, "")
  to_do_list.addTask(task)

@when('the user lists all tasks')
def step_impl(context):
  

@given('the to-do list contains a task with the title "{title}" at a certain position')
def setp_impl(context, title):
  taskOne = Task("Read Suggested Reading", "", False, "Benjamin Dunes")
  taskTwo = Task(title, "", False, "Benjamin Dunes")
  to_do_list.addTask(taskOne)
  to_do_list.addTask(taskTwo)

@and('the to-do list has a length greater than or equal to 1')
def setp_impl(context):
  assert len(to_do_list.list) >= 1, "The to-do list contains at least one item"

@when('the user removes the task with title "{title}" at a certain position')
def setp_impl(context, title):
  task = to_do_list.list[1]
  assert task.title == title
  to_do_list.removeTask(task)

@then('the to-do list no longer contains the task with the title "{title}" in the specified position')
def setp_impl(context, title):
  taskStillExists = False
  if(len(to_do_list.list > 1)):
    task = to_do_list.list[1]
    if(task.title == title):
      taskStillExists = True
  assert !taskStillExists, ""