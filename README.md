This Python program is a small console application that helps you add, view, and remove tasks from a to-do list. The special feature is that the tasks are saved in a text file tasks.txt, so they remain even after you close the program.
1. Loading Tasks
At the beginning, the program tries to read tasks from a file called tasks.txt.If the file exists, it loads all the tasks into a list.If the file does not exist, it starts with an empty task list.
2. Saving Tasks
Whenever you add or remove a task, the program updates the tasks.txt file.This ensures your tasks are stored permanently.
3. Adding a Task
When you choose the "Add Task" option:The program asks you to type a task.It adds the task to the list.Then it saves the updated list into the file.
4. Viewing Tasks
When you choose the "View Tasks" option:The program prints all the tasks one by one.Every task is shown with a number (1, 2, 3…) so it is easy to identify them.
5. Removing a Task
When you choose "Remove Task":The program shows the list of tasks.You enter the task number you want to delete.It removes that task from the list.Then it saves the new list in the file.
6. Menu System
The program repeatedly shows a menu with four choices:
Add Task
View Tasks
Remove Task
Exit
You can choose any option using the keyboard.
If you choose Exit, the program saves the tasks one last time and closes.
