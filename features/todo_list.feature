Feature: To-Do List

@addTask
Scenario: Add a task to the to-do list
  Given the to-do list is empty
  when the user adds a task with title "Buy groceries" description "buy somethings" and person "Giancarlo"
  Then the to-do list should contain task "Buy groceries"

@clearTaskList
Scenario: Clear entire to-do list
  Given the to-do list contains task "Buy groceries"
  When the user clears the to-do list
  Then the to-do list should be empty

@completeTask
Scenario: Mark a task as complete
  Given the to-do list contains task in index 0 set completed as False
  When the user marks a task with index 0
  Then the to-do list should contain a task in index 0 marked True 

@listTaskList 
Scenario: List all tasks in the to-do list 
  Given the to-do list contains tasks "Buy groceries" 
  When the user lists all tasks 
  Then the output should contain "Buy groceries"

@removeTask
Scenario: Remove a task from the to-do list
  Given the to-do list contains a task with the title "Finish Workshop" at a certain position
  And the to-do list has a length greater than or equal to 1
  When the user removes the task with title "Finish Workshop" at a certain position
  Then the to-do list no longer contains the task with the title "Finish Workshop" in the specified position
  And the to-do list length has decreased by 1

@seeDetails
Scenario: See the details of a specific task from the to-do list
  Given the to-do list contains a task with title "Push Commits" description "Push all the commits made to the repo" and person "Erwing" at position 0
  When the user prints the details of the task at position 0
  Then the details output should be "\nTitle: Push Commits\nDescription: Push all the commits made to the repo\nPerson: Erwing"

@printEmptyList
Scenario: When the list is empty and the user wants to print the list, show a empty print
  Given an empty to-do list
  When the user prints the list
  Then the output should be "EMPTY LIST"