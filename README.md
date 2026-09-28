# StudyTrack

## 1\. Project Title

**StudyTrack – A Basic Student Study Management System**

## 2\. Overview of the Project

studyTrack is a simple Python program for students. It helps them add tasks, complete tasks, record study time, and check their total study time.

## 3\. Features

Add a new task
Enter task details
View all tasks
Mark a task as completed
Add study time
View study sessions
See total study time
Show error messages for wrong inputs

## 4\. Technologies / Tools Used

* **Python**
* Python Lists
* Python Functions
* `input()` and `print()`
* `if / elif / else`
* `for` loop
* `while` loop
* Basic arithmetic

## 5\. Steps to Install \& Run the Project

### Requirements

* Python 3 installed on the computer
* Any Python editor or terminal

### Steps

1. Download the project.
2. Open the project folder.
3. Open the `main.py` file.
4. Run the program using a Python editor or terminal.

In the terminal, use:

```bash
python main.py
```

If required, use:

```bash
python3 main.py
```

## 6\. Instructions for Testing

Run the program and test each menu option one by one.

### Test 1 – Add Task

1. Select **1. Add Task**.
2. Enter the task, subject, due date, and priority.
3. Check that the task is added with **Pending** status.

### Test 2 – Show Tasks

1. Select **2. Show Tasks**.
2. Check that the added task details are displayed.

### Test 3 – Complete Task

1. Select **3. Complete Task**.
2. Enter the task number.
3. Check that the selected task status changes to **Completed**.

### Test 4 – Add Study Session

1. Select **4. Add Study Session**.
2. Enter the subject and study time in minutes.
3. Check that the study session is added.

### Test 5 – Show Study Sessions

1. Select **5. Show Study Sessions**.
2. Check that the study sessions and total study time are displayed.

### Test 6 – Invalid Task Number

1. Select **3. Complete Task**.
2. Enter an invalid task number.
3. Check that the program displays an invalid task number message.

### Test 7 – Invalid Menu Choice

1. Enter a menu number that is not between 1 and 6.
2. Check that the program displays **Invalid choice!**.

