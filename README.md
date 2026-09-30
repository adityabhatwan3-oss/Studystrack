# Study Track

## Project Title
**Study Track – A Basic Student Study Management System**

## Overview
Study Track is a simple Python program made to help student manage their study tasks and keep track of their study time.

The program has a menu where students can add tasks, view their tasks, mark tasks as completed, add study sessions, and see their total study time. The project is made using basic Python concepts covered in the Python Essentials course.

## Features


- Add a new study task

- Enter task titl, subject, due date, and priority

- View all added tasks

- Mark a selected task as completed

- Add a study session with subject and time in minutes

- View recorded study sessions

- Calculate and display total study time

- Handle invalid task numbers and invalid menu choices

## Technologies / Tools Used

- **Python**

- Python lists

- Python functions

- `input()` and `print()`

- `if / elif / else`

- `for` loop

- `while` loop

- Basic arithmetic

## Project Structure

The current project is a simple Python program and mainly contains:

- `main.py` – contains the complete StudyTrack program

The program uses two lists during execution:

- `tasks = []` – stores task details
- `study_sessions = []` – stores subject and study-time details

## How to Install and Run

### Requirements

- Python 3 installed on your computer
- Any Python editor or terminal

### Steps

1. Download or clone this project.
2. Open the project folder.
3. Open `main.py` in a Python editor or terminal.
4. Run the program.

For terminal, use:

```bash
python main.py
```

If your system uses `python3`, you can use:

```bash
python3 main.py
```

## How to Use

After starting the program, the main menu is displayed:

```text
===== STUDYTRACK =====
1. Add Task

2. Show Tasks

3. Complete Task

4. Add Study Session

5. Show Study Sessions

6. Exit
```

Enter the number of the operation you want to perform.

### Add Task

The program asks for:

- Task
- Subject
- Due date
- Priority

The task is then stored with a **Pending** status.

### Show Tasks

This option displays the tasks that have been add, along with their subject, due date, priority, status.

### Complete Task

Enter the task number to change its status from **Pending** to **Completed**.

### Add Study Session

Enter the subject and the amount of study time in minute. The session is stored in the program.

### Show Study Sessions

This option displays the recorded study sessions and calculates the total study time in minute.

## Testing

The program can be tested using normal inputs for all six menu option.

The following cases should be checked:

| Test | Action | Expected Result |
|---|---|---|
| 1 | Add Task | Task is added with Pending status |
| 2 | Show Tasks | Task details are displayed |
| 3 | Complete Task | Selected task becomes Completed |
| 4 | Add Study Session | Study session is stored |
| 5 | Show Study Sessions | Sessions and total study time are displayed |
| 6 | Invalid task number | Invalid task number message is displayed |
| 7 | Invalid menu choice | Invalid choice message is displayed |

## Important Note

Study Track currently stores its data in lists while the program is running. The current version does not use a database or permanent file storage, so the stored tasks and study sessions are not saved after the program is closed.

## Future Enhancements

Some features that can be added in the future are:

- Save tasks and study sessions permanently in a file
- Add a graphical user interface
- Add reminders for pending tasks
- Add daily and subject-wise study statistics
- Improve input validation for incorrect values

## Project Purpose

This project was made as part of the **Python Essentials** course to understand how basic Python concepts can be used together to create a simple working application.

## References

- VITyarthi – Build Your Own Project: General Project Instructions & Submission Guidelines
- Python Essentials course concepts and classroom material
