tasks = []
study_sessions = []

def add_task():
    title = input("Enter task: ")
    subject = input("Enter subject: ")
    due_date = input("Enter due date: ")
    priority = input("Enter priority: ")

    task = [title, subject, due_date, priority, "Pending"]
    tasks.append(task)

    print("Task added successfully!")


def show_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("\n===== TASKS =====")
        for i in range(len(tasks)):
            print(i + 1, "-", tasks[i][0])
            print("Subject:", tasks[i][1])
            print("Due Date:", tasks[i][2])
            print("Priority:", tasks[i][3])
            print("Status:", tasks[i][4])
            print()


def complete_task():
    show_tasks()

    if len(tasks) == 0:
        return

    number = int(input("Enter task number: "))

    if number >= 1 and number <= len(tasks):
        tasks[number - 1][4] = "Completed"
        print("Task completed!")
    else:
        print("Invalid task number.")


def add_study_session():
    subject = input("Enter subject: ")
    minutes = int(input("Enter study time in minutes: "))

    session = [subject, minutes]
    study_sessions.append(session)

    print("Study session added!")


def show_study_sessions():
    if len(study_sessions) == 0:
        print("No study sessions found.")
    else:
        print("\n===== STUDY SESSIONS =====")
        total = 0

        for i in range(len(study_sessions)):
            print(i + 1, "-", study_sessions[i][0],
                  "-", study_sessions[i][1], "minutes")
            total = total + study_sessions[i][1]

        print("Total study time:", total, "minutes")


while True:

    print("\n===== STUDYTRACK =====")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Complete Task")
    print("4. Add Study Session")
    print("5. Show Study Sessions")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        add_study_session()

    elif choice == "5":
        show_study_sessions()

    elif choice == "6":
        print("Thank you for using StudyTrack!")
        break

    else:
        print("Invalid choice!")
