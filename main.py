# Barangay Incident Report Management System (Stable Release)
# Created by Zenica Nacua (Zenica Shin)

from datetime import datetime

incident_reports = []

def show_welcome():
    print("=======================================================")
    print("   👋 WELCOME TO BARANGAY INCIDENT REPORT SYSTEM (BIRMS)")
    print("=======================================================\n")
    print("This system helps barangay officials record, manage, and")
    print("monitor incident reports efficiently and securely.\n")
    print("Developed by: Group 6 (Zenica Shin)\n")

def add_report():
    while True:
        print("\n--- ADD INCIDENT REPORT ---")
        print("Note: Date must be PRESENT or FUTURE only.")

        today = datetime.today().date()

        # DATE VALIDATION
        while True:
            date_input = input("Enter Date (YYYY-MM-DD): ")
            try:
                date = datetime.strptime(date_input, "%Y-%m-%d").date()
                if date < today:
                    print("❌ ERROR: Past dates are NOT allowed.")
                else:
                    break
            except ValueError:
                print("❌ Invalid date format. Please use YYYY-MM-DD.")

        complainant = input("Enter Complainant Name: ").strip()
        respondent = input("Enter Name of the Person Being Complained (Respondent): ").strip()
        description = input("Enter Description of the Incident: ").strip()

        report = {
            "Date": str(date),
            "Complainant": complainant,
            "Respondent": respondent,
            "Description": description
        }

        incident_reports.append(report)
        print("✅ Report added successfully!\n")

        again = input("Would you like to ADD ANOTHER report? (yes/no): ").strip().lower()
        if again != "yes":
            break

def view_reports():
    print("\n--- VIEW INCIDENT REPORTS ---")
    if not incident_reports:
        print("No incident reports available.\n")
        return

    for i, report in enumerate(incident_reports, start=1):
        print(f"{i}. Date: {report['Date']}")
        print(f"   Complainant: {report['Complainant']}")
        print(f"   Respondent: {report['Respondent']}")
        print(f"   Description: {report['Description']}\n")

def edit_report():
    print("\n--- EDIT INCIDENT REPORT ---")
    if not incident_reports:
        print("No reports to edit.\n")
        return

    view_reports()

    try:
        index = int(input("Enter report number to edit: ").strip()) - 1
        if 0 <= index < len(incident_reports):
            r = incident_reports[index]
            print("Leave blank to keep current value.")

            new_date = input(f"New Date ({r['Date']}): ").strip() or r['Date']
            new_complainant = input(f"New Complainant ({r['Complainant']}): ").strip() or r['Complainant']
            new_respondent = input(f"New Respondent ({r['Respondent']}): ").strip() or r['Respondent']
            new_desc = input(f"New Description ({r['Description']}): ").strip() or r['Description']

            incident_reports[index] = {
                "Date": new_date,
                "Complainant": new_complainant,
                "Respondent": new_respondent,
                "Description": new_desc
            }
            print("✅ Report updated successfully!\n")
        else:
            print("Invalid report number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def delete_report():
    print("\n--- DELETE INCIDENT REPORT ---")
    if not incident_reports:
        print("No reports to delete.\n")
        return

    view_reports()
    name_to_delete = input("Enter COMPLAINANT NAME to delete: ").strip()

    for report in list(incident_reports):  # iterate over copy to safely remove
        if report["Complainant"].lower() == name_to_delete.lower():
            incident_reports.remove(report)
            print(f"🗑️ Report for '{report['Complainant']}' deleted!\n")
            return

    print(f"❌ No report found under the name '{name_to_delete}'.\n")

def search_reports():
    print("\n--- SEARCH INCIDENT REPORTS ---")
    if not incident_reports:
        print("No reports available.\n")
        return

    print("Search by:")
    print("[1] Date")
    print("[2] Complainant Name")
    print("[3] Respondent Name")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        key = "Date"
        value = input("Enter Date (YYYY-MM-DD): ").strip()
    elif choice == "2":
        key = "Complainant"
        value = input("Enter Complainant Name: ").strip()
    elif choice == "3":
        key = "Respondent"
        value = input("Enter Respondent Name: ").strip()
    else:
        print("❌ Invalid choice. Returning to menu.\n")
        return

    print(f"\n🔎 SEARCH RESULTS for '{value}':")
    found = False
    for report in incident_reports:
        # support exact match for date, case-insensitive partial match for names
        if key == "Date":
            match = (report["Date"] == value)
        else:
            match = (value.lower() in report[key].lower())

        if match:
            found = True
            print(f"\nDate: {report['Date']}")
            print(f"Complainant: {report['Complainant']}")
            print(f"Respondent: {report['Respondent']}")
            print(f"Description: {report['Description']}\n")

    if not found:
        print("❌ No matching reports found.\n")

def main_menu():
    show_welcome()
    while True:
        print("========== MAIN MENU ==========")
        print("[1] Add Incident Report")
        print("[2] View Incident Reports")
        print("[3] Edit Incident Report")
        print("[4] Delete Incident Report")
        print("[5] Search Incident Reports")
        print("[6] Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_report()
        elif choice == "2":
            view_reports()
        elif choice == "3":
            edit_report()
        elif choice == "4":
            delete_report()
        elif choice == "5":
            search_reports()
        elif choice == "6":
            print("👋 Exiting system. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()