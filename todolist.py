from database import create_database, session
from tasks import Task
from datetime import datetime, timedelta, date


def information_menu():
    print("1) Today's tasks" "\n" "2) Week's tasks" "\n" "3) All tasks" "\n" "4) Missed tasks" 
          "\n" "5) Add a task" "\n" "6) Delete a task" "\n" "0) Exit")


def get_missed_tasks():
    print("Missed tasks:")
    rows = session.query(Task).filter(Task.deadline < datetime.today().date()).all()
    number_of_tasks = len(rows)
    if number_of_tasks == 0:
        print('All tasks have been completed! ')
    else:
        for num in range(0, number_of_tasks):
            row = rows[num]
            print(f"{num+1}. {row.task}. {row.deadline.strftime('%#d %B')}")
    print()


def delete_tasks():
    print("Choose the number of the task you want to delete:")
    rows = session.query(Task).order_by(Task.deadline).all()
    number_of_tasks = len(rows)
    if number_of_tasks == 0:
        print('Nothing to delete!')
    else:
        for num in range(0, number_of_tasks):
            row = rows[num]
            print(f"{num+1}. {row.task}. {row.deadline.strftime('%#d %B')}")
        number_of_delete_task = int(input()) - 1
        delete_task = rows[number_of_delete_task]
        session.delete(delete_task)
        session.commit()
        print("The task has been deleted!")


def add_task():
    print()
    user_task = input("Enter a task\n")
    user_deadline = input("Enter a deadline\n")
    print()
    deadline = datetime.strptime(user_deadline, "%Y-%m-%d").date()
    new_task = Task(task=user_task, deadline=deadline)

    session.add(new_task)
    session.commit()
    print('The task has been added!')


def all_tasks():
    print()
    print("All tasks: ")
    rows = session.query(Task).order_by(Task.deadline).all()
    number_of_tasks = len(rows)
    if number_of_tasks == 0:
        print('Nothing to do!')
    else:
        for num in range(0, number_of_tasks):
            row = rows[num]
            print(f"{num+1}. {row.task}. {row.deadline.strftime('%#d %B')}")
    print()


def print_week_tasks():

    for i in range(0, 7):
        week_days = datetime.today() + timedelta(days=i)
        rows = session.query(Task).filter(Task.deadline == week_days.date()).all()
        number_of_tasks = len(rows)
        print("\n"f"{week_days.strftime('%A %d %b')}")
        if number_of_tasks == 0:
            print("Nothing to do!")
        else:

            for num in range(0, number_of_tasks):
                row = rows[num]
                print(f"{num+1}. {row.task}")


def print_today_tasks():
    today = datetime.today()
    rows = session.query(Task).filter(Task.deadline == today.date()).all()

    number_of_tasks = len(rows)
    if number_of_tasks == 0:
        print(f"Today {today.strftime('%A %d %b')}")
        print("Nothing to do!" "\n")
    else:
        d = date.today()
        print("\n" f"Today {d.strftime('%d %B')}")
        for num in range(0, number_of_tasks):
            row = rows[num]
            print(f"{row.id}. {row.task}")
        print()


def main():
    while True:
        information_menu()
        user_choice = input()
        if user_choice == "1":
            print_today_tasks()
        elif user_choice == "2":
            print_week_tasks()
        elif user_choice == "3":
            all_tasks()
        elif user_choice == "5":
            add_task()
        elif user_choice == "4":
            get_missed_tasks()
        elif user_choice == "6":
            delete_tasks()
        elif user_choice == "0":
            print()
            print("Bye!")
            quit()


if __name__ == "__main__":
    create_database()
    main()
