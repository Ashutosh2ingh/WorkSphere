# WorkSphere – Office Management System

WorkSphere is a full-fledged Office Management System built using Django. It helps organizations manage employees, attendance, payroll, assets, and performance in one place.

---

## 📌 Features

### 👤 Employee Management
- Add / Update / Delete Employees
- Department & Role Management
- Manager hierarchy

### ⏱ Attendance System
- Daily check-in / check-out
- Total working hours calculation
- Attendance status (Present, Absent, Leave)

### 💰 Payroll System
- Salary management
- Bonuses & deductions
- Monthly salary tracking

### 🏖 Leave Management
- Apply for leave
- Approval / Rejection workflow
- Leave types (Sick, Casual, Paid)

### 📊 Performance Tracking
- Employee reviews
- Ratings & feedback

### 💻 Asset Management
- Assign assets (Laptop, Phone, etc.)
- Track allocation & return

### 🔔 Notifications
- System alerts & updates

### 🧾 Audit Logs
- Track system activities

---

## 🛠 Tech Stack

- Backend: Django
- Database: SQLite (default) / PostgreSQL
- Frontend: Django Templates (initial) / React (future)
- Version Control: Git & GitHub

---

## ⚙️ Installation

Follow the steps below to run the project locally.

```bash
# Clone the repository
git clone https://github.com/Ashutosh2ingh/WorkSphere.git

# Navigate to project folder
cd WorkSphere

# Activate virtual environment
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Run server
python manage.py runserver