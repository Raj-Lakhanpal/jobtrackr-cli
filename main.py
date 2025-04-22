from database import initialize_database
from job_actions import add_job, view_jobs, search_jobs, edit_job, delete_job, show_stats

# Initialize database when the app starts
initialize_database()

while True:
    print("\n")
    print("1. Add a job")
    print("2. View all jobs")
    print("3. Search jobs")
    print("4. Edit job")
    print("5. Delete job")
    print("6. Application stats")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_job()
    elif choice == "2":
        view_jobs()
    elif choice == "3":
        search_jobs()
    elif choice == "4":
        edit_job()
    elif choice == "5":
        delete_job()
    elif choice == "6":
        show_stats()
    elif choice == "7":
        exit()
