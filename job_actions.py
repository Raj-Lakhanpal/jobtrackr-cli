import sqlite3  # Import the SQLite module for database operations

def add_job():
    # Prompt the user for job details and clean the input
    company = input("Enter company name: ").strip().title()
    role = input("Enter role title: ").strip().title()
    status = input("Enter application status (Applied/Interviewing/etc.): ").strip().title()
    applied_date = input("Enter date applied (e.g., 2024-04-21): ").strip()
    notes = input("Optional notes (press Enter to skip): ").strip()

    # Open a connection to the jobtrackr database and insert the job details
    with sqlite3.connect("jobtrackr.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO jobs (company, role, status, applied_date, notes)
            VALUES (?, ?, ?, ?, ?)
        """, (company, role, status, applied_date, notes))

def view_jobs():
    # Connect to the database and fetch all job records
    with sqlite3.connect("jobtrackr.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM jobs ORDER BY id DESC")  # Order jobs by newest first
        rows = cursor.fetchall()

        if not rows:
            print("No job applications found")

        # Print each job in a clean format
        for row in rows:
            print(f'ID: {row[0]}')
            print(f'Company: {row[1]}')
            print(f'Role: {row[2]}')
            print(f'Status: {row[3]}')
            print(f'Date applied: {row[4]}')
            print(f'Notes: {row[5]}')


def search_jobs():
    # Ask user how they want to search
    search = input("Would you like to search the job by a company name or status (company/status): ")

    with sqlite3.connect("jobtrackr.db") as conn:
        cursor = conn.cursor()

        # Search by company name
        if search.strip().lower() == 'company':
            company_name = input("Please enter a company name: ")
            cursor.execute("SELECT * FROM jobs WHERE company LIKE ?", (f"%{company_name}%",))
        # Search by status
        elif search.strip().lower() == 'status':
            status = input("Please enter a status: ")
            cursor.execute("SELECT * FROM jobs WHERE status LIKE ?", (f"%{status}%",))

        rows = cursor.fetchall()

        if not rows:
            print("❌ No matching job applications found.")

        # Print matched results
        for row in rows:
            print(f"🧑‍💼 Role: {row[2]}")
            print(f"🏢 Company: {row[1]}")
            print(f"📌 Status: {row[3]}")
            print(f"🗕️ Date Applied: {row[4]}")
            print(f"📝 Notes: {row[5]}")
            print("-" * 40)


def edit_job():
    # Prompt for company name to search/edit
    company_name = input("Enter the company name to edit: ")
    rows = get_matching_jobs(company_name)  # Fetch matching jobs
    print("DEBUG: rows = ", rows)

    if not rows:
        return

    print("DEBUG: About to call display_jobs...")
    display_jobs(rows)  # Show matched jobs

    selected_id = int(input("Enter the ID of the job you want to edit: "))

    for row in rows:
        if row[0] == selected_id:
            current_status = row[3]  # Get existing status
            current_notes = row[5]  # Get existing notes

    choice = prompt_for_update_choice()  # Ask what user wants to update
    new_status, new_notes = get_updated_values(choice, current_status, current_notes)  # Get new values
    update_job_in_db(selected_id, new_status, new_notes)  # Apply update


def get_matching_jobs(company_name):
    # Connect and search by lowercased company name for case-insensitive match
    with sqlite3.connect('jobtrackr.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM jobs WHERE LOWER(company) LIKE ?", (f"%{company_name.lower()}%",))

        rows = cursor.fetchall()
        print(f"DEBUG: found {len(rows)} rows")

        if not rows:
            print("❌ No company by this name.")
            return

        return rows

def display_jobs(rows):
    print("DEBUG: Displaying jobs...")

    for row in rows:
        print(f"🆔 Job ID: {row[0]}")
        print(f"🧑‍💼 Role: {row[2]}")
        print(f"🏢 Company: {row[1]}")
        print(f"📌 Status: {row[3]}")
        print(f"🗕️ Date Applied: {row[4]}")
        print(f"📝 Notes: {row[5]}")
        print("-" * 40)


def prompt_for_update_choice():
    # Ask user what they want to update
    print("What would you like to update?")
    print("1. Status")
    print("2. Notes")
    print("3. Both")

    update_choice = input("Enter your choice (1/2/3): ")
    return update_choice  # Return selected option


def get_updated_values(choice, current_status, current_notes):
    # Based on user choice, prompt for updates or keep old values
    if choice == "1":
        new_status = input("Enter new status: ")
        new_notes = current_notes
    elif choice == "2":
        new_notes = input("Enter new notes: ")
        new_status = current_status
    elif choice == "3":
        new_status = input("Enter new status: ")
        new_notes = input("Enter new notes: ")
    return new_status, new_notes


def update_job_in_db(job_id, new_status, new_notes):
    # Update a job with new status and notes based on job ID
    with sqlite3.connect("jobtrackr.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE jobs SET status = ?, notes = ? WHERE id = ?", (new_status, new_notes, job_id))
        conn.commit()  # Save changes
        print("Job updated successfully!")


def delete_job():
    # Prompt user for the company to delete from
    company_name = input("Enter the company name: ")
    rows = get_matching_jobs(company_name)  # Search jobs
    display_jobs(rows)  # Show results

    selected_id = int(input("Enter the ID of the job you want to delete:"))
    selected_id_answer = input("Are you sure you want to delete this job? (y/n)")

    if selected_id_answer.lower() == "y":
        with sqlite3.connect("jobtrackr.db") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM jobs WHERE id = ?", (selected_id,))
        print("✅ Job has been deleted from your tracker.")
    else:
        print("❌ Deletion canceled.")


def show_stats():
    with sqlite3.connect("jobtrackr.db") as conn:
        cursor = conn.cursor()

        # Total jobs count
        cursor.execute("SELECT COUNT(*) FROM jobs")
        total_job_apps = cursor.fetchone()[0]  # Result: (12,) → take the first value

        # Jobs grouped by status
        cursor.execute("SELECT status, COUNT(*) FROM jobs GROUP BY status")
        status_rows = cursor.fetchall()  # Result: [('Applied', 5), ('Interviewing', 3), ...]

        # Display results
        print("📊 Job Application Stats")
        print("-" * 30)
        print(f"✅ Total Jobs: {total_job_apps}")
        print("\nStatus Breakdown:")

        for status, count in status_rows:
            print(f"{status}: {count}")
