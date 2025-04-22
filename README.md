# 🎯 JobTrackr - Job Application Tracker (CLI)

**Track your job applications from the terminal using this clean, modular Python + SQLite CLI app.**

---

## 📦 Features

- ✅ Add a job application (company, role, status, date, notes)
- 📋 View all job applications
- 🔍 Search jobs by company or application status
- ✏️ Edit an existing job’s status or notes
- 🗑️ Delete a job from the tracker
- 📊 Coming Soon: Stats dashboard (e.g., total jobs applied)
- 🧪 Coming Soon: Unit tests for job logic

---

## ⚙️ Requirements

- Python 3.7+
- No external dependencies (uses built-in `sqlite3`)

---

## 🛠️ Project Structure

```
jobtrackr/
├── main.py                # CLI entry point
├── job_actions.py         # All job-related functions (add, view, edit, delete)
├── jobtrackr.db           # SQLite database (auto-created)
├── README.md              # Project documentation
├── .gitignore             # Git exclusions for environment, db, etc.
```

---

## 🚀 How to Run the App

1. **Clone the repo:**

```bash
git clone https://github.com/your-username/jobtrackr-cli.git
cd jobtrackr-cli
```

2. **Create a virtual environment (recommended):**

```bash
python3 -m venv v-jobtrackr
source v-jobtrackr/bin/activate  # Windows: v-jobtrackr\Scripts\activate
```

3. **Run the app:**

```bash
python main.py
```

---

## 🔄 Menu Options

```
1. Add a job
2. View all jobs
3. Search jobs
4. Edit job
5. Delete job
6. Exit
```

---

## 🧠 How It Works

- All data is stored in a local SQLite database `jobtrackr.db`.
- Each job entry includes:
  - Company
  - Role
  - Application Status
  - Date Applied
  - Notes

---

## 🧑‍💻 Author

Built step-by-step by **Raj**, to practice Python, SQL, clean architecture, and debugging.

---

## 💡 Tips for Use

- Confirm deletion before removing a job
- Edit either the status, notes, or both
- Use clear status labels (e.g., Applied, Interviewing, Rejected, Offer)

---

## 📈 What's Next

- 📊 Stats Dashboard (e.g., applied/interviewing count)
- 📤 Export to CSV
- ✅ Unit Tests for core logic
- 📂 Add `job_model.py` for query abstraction (advanced refactor)

---

## 🔗 GitHub Repo Summary (One-Liner)

> Track your job applications from the command line using this clean, modular Python CLI app with a real SQLite backend.