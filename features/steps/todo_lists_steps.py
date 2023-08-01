import io
from task import Task
from tasklist import TaskList
from behave import given, then, when, step
import sys

to_do_list = TaskList()
task = None
capturedOutput = None

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
  global captured_output
  captured_output = io.StringIO()
  sys.stdout = captured_output
  to_do_list.printList()
  sys.output = sys.__stdout__

@then('the output should contain "{expected_output}"')
def step_impl(context, expected_output):
  global captured_output
  assert expected_output.strip() in captured_output.getvalue().strip(), 'Task not found in list'
  

@given('the to-do list contains a task with the title "{title}" at a certain position')
def setp_impl(context, title):
  to_do_list.clear()
  taskOne = Task("Read Suggested Reading", "", False, "Benjamin Dunes")
  taskTwo = Task(title, "", False, "Benjamin Dunes")
  to_do_list.addTask(taskOne)
  to_do_list.addTask(taskTwo)

@step('the to-do list has a length greater than or equal to 1')
def setp_impl(context):
  assert len(to_do_list.list) >= 1, "The to-do list does not contain at least one item"

@when('the user removes the task with title "{title}" at a certain position')
def setp_impl(context, title):
  task = to_do_list.list[1]
  assert task.title == title
  to_do_list.removeTask(task)

@then('the to-do list no longer contains the task with the title "{title}" in the specified position')
def setp_impl(context, title):
  taskStillExists = False
  if(len(to_do_list.list) > 1):
    task = to_do_list.list[1]
    if(task.title == title):
      taskStillExists = True
  assert not taskStillExists, "Task not removed from the to-do list"

@step('the to-do list length has decreased by 1')
def setp_impl(context):
  assert len(to_do_list.list) == 1, "The to-do list length did not decreased correctly"


@given('the to-do list contains a task with title "{title}" description "{description}" and person "{person}" at position {index}')
def setp_impl(context, title, description, person, index):
  to_do_list.clear()
  task = Task(title, description, False, person)
  to_do_list.addTask(task)

@when('the user prints the details of the task at position {index}')
def setp_impl(context, index):
  global capturedOutput
  task = to_do_list.list[int(index)]
  capturedOutput = io.StringIO()
  sys.stdout = capturedOutput
  print(task.details())                                  
  sys.stdout = sys.__stdout__ 

@then('the details output should be "{expectedOutput}"')
def setp_impl(context, expectedOutput):
  global capturedOutput
  expectedOutput = expectedOutput.replace('\\n', '\n')
  assert capturedOutput.getvalue().strip() == expectedOutput.strip(), 'Incorrect details printed'


@given('an empty to-do list')
def setp_impl(context):
  to_do_list.clear()

@when('the user prints the list')
def setp_impl(context):
  global capturedOutput
  capturedOutput = io.StringIO()
  sys.stdout = capturedOutput
  to_do_list.printList()
  sys.stdout = sys.__stdout__ 

@then('the output should be EMPTY LIST')
def setp_impl(context):
  global capturedOutput
  assert capturedOutput.getvalue().strip() == "EMPTY LIST", 'Output is not EMPTY LIST'