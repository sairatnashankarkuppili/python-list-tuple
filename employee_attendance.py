from datetime import datetime

employees = [
    (101, "Alice Johnson", "HR"),
    (102, "Bob Smith", "IT"),
    (103, "Charlie Brown", "Finance"),
    (104, "David White", "IT"),
    (105, "Eve Black", "Marketing")
]
attendance_records = []

def mark_attendance():
    emp_id = int(input("\nEnter Employee ID: "))
    date = datetime.now().strftime("%Y-%m-%d")
    status = input("Enter Attendance (Present/Absent): ").capitalize()

    if any(emp[0] == emp_id for emp in employees):
        attendance_records.append((emp_id, date, status))
        print(f"Attendance marked for Employee {emp_id} on {date}: {status}")
    else:
        print("Invalid Employee ID!")


def search_attendance_by_id():
    emp_id = int(input("\n Enter Employee ID to search attendance: "))
    records = [rec for rec in attendance_records if rec[0] == emp_id]

    if records:
        print(f"\n Attendance Records for Employee {emp_id}:")
        for rec in records:
            print(f"  Date: {rec[1]}, Status: {rec[2]}")
    else:
        print("No records found!")

def attendance_summary():
    print("\n Attendance Summary:")
    for emp in employees:
        emp_id = emp[0]
        total_days = sum(1 for rec in attendance_records if rec[0] == emp_id)
        present_days = sum(1 for rec in attendance_records if rec[0] == emp_id and rec[2] == "Present")

        percentage = (present_days / total_days * 100) if total_days > 0 else 0
        print(f"  {emp[1]}: {percentage:.2f}% Present")

while True:
    print("\n Employee Attendance System")
    print("1. Mark Attendance")
    print("2. Search Attendance by ID")
    print("3. View Attendance Summary")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        mark_attendance()
    elif choice == "2":
        search_attendance()
    elif choice == "3":
        attendance_summary()
    elif choice == "4":
        print("Thank You!")
        break
    else:
        print("Invalid choice! Please try again.")
