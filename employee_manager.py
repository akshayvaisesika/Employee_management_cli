import os
import json
from validators import(validate_age,validate_email,validate_employee_id,validate_name,validate_salary)
from logger import logger

DATA_FILE = "data/employees.json"

def load_employees(): 
    try:
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, "r") as file:
            employees = json.load(file)
        logger.info("Employee data loaded successfully.")
        return employees

    except json.JSONDecodeError:
        logger.error("Employee JSON file contains invalid data.")
        print("Error: Employee data file is corrupted.")
        return []

    except OSError as e:
        logger.error(f"Error reading employee data: {e}")
        print("Error: Unable to read employee data.")
        return []




#saving employees
def save_employees(employees):

    try:
        with open(DATA_FILE, "w") as file:
            json.dump(employees, file, indent=4)

        logger.info("Employee data saved successfully.")

    except OSError as e:
        logger.error(f"Error saving employee data: {e}")
        print("Error: Unable to save employee data.")



# adding employees

def add_employee(employees):

    # Employee ID validation
    while True:
        try:
            emp_id = validate_employee_id(input("Enter employee ID: "))
            duplicate = False

            for employee in employees:
                if employee["id"] == emp_id:
                    duplicate = True
                    break

            if duplicate:
                print("Error: Employee ID already exists.")
                logger.warning(f"Duplicate employee ID attempted: {emp_id}")
                continue
            break

        except ValueError as e:
            print(f"Invalid employee ID: {e}")

    # Employee name
    name = validate_name(input("Enter employee name: "))

    # Age validation
    while True:
        try:
            age = validate_age(input("Enter employee age: "))
            break

        except ValueError as e:
            print(f"Invalid age: {e}")

    # Department
    department = input("Enter department: ").strip()


    # Role
    role = input("Enter role: ").strip()



    # Salary validation
    while True:
        try:
            salary = validate_salary(input("Enter salary: "))
            break

        except ValueError as e:
            print(f"Invalid salary: {e}")


    # Email validation
    while True:
        try:
            email = validate_email(input("Enter email: "))
            break

        except ValueError as e:
            print(f"Invalid email: {e}")

    # Create employee
    employee = {
        "id": emp_id,
        "name": name,
        "age": age,
        "department": department,
        "role": role,
        "salary": salary,
        "email": email
    }

    employees.append(employee)

    save_employees(employees)

    logger.info(f"Employee {emp_id} added successfully.")
    print("Employee added successfully.")


        

#searching employee

def search_employee(employees):
    try:
        emp_id = validate_employee_id(input("Enter employee ID to search: "))
        for employee in employees:
            if employee["id"] == emp_id:
                print("\nEmployee Found")
                print("-" * 30)

                for key, value in employee.items():
                    print(f"{key.capitalize()}: {value}")
                logger.info(f"Employee {emp_id} searched successfully.")
                return employee

        print("Employee not found.")
        logger.warning(f"Employee {emp_id} not found during search.")
        return None

    except ValueError as e:
        print(f"Invalid input: {e}")
        logger.error(f"Invalid search input: {e}")
        return None



#updating_employee

def update_employee(employees):
    try:
        emp_id = validate_employee_id(input("Enter employee ID to update: "))
        for employee in employees:

            if employee["id"] == emp_id:
                print("\nEmployee found.")
                print("Press Enter to keep the existing value.\n")

                name = input(f"Name [{employee['name']}]: ").strip()
                age = input(f"Age [{employee['age']}]: ").strip()
                department = input(f"Department [{employee['department']}]: ").strip()
                role = input(f"Role [{employee['role']}]: ").strip()
                salary = input(f"Salary [{employee['salary']}]: ").strip()
                email = input(f"Email [{employee['email']}]: ").strip()

                if name:
                    employee["name"] = validate_name(name)

                if age:
                    employee["age"] = validate_age(age)

                if department:
                    employee["department"] = department

                if role:
                    employee["role"] = role

                if salary:
                    employee["salary"] = validate_salary(salary)

                if email:
                    employee["email"] = validate_email(email)

                save_employees(employees)

                logger.info(f"Employee {emp_id} updated successfully.")
                print("Employee updated successfully.")
                return employee

        print("Employee not found.")
        logger.warning(f"Employee {emp_id} not found during update.")
        return None

    except ValueError as e:
        print(f"Invalid input: {e}")
        logger.error(f"Invalid update input: {e}")
        return None


#deleting_employee

def delete_employee(employees):
    try:
        emp_id = validate_employee_id(input("Enter employee ID to delete: "))

        for employee in employees:
            if employee["id"] == emp_id:
                employees.remove(employee)
                save_employees(employees)
                logger.info(f"Employee {emp_id} deleted successfully.")
                print("Employee deleted successfully.")
                return

        print("Employee not found.")
        logger.warning(f"Employee {emp_id} not found during deletion.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        logger.error(f"Invalid delete input: {e}")



#filtering_record
def filter_employees(employees):

    department = input("Enter department (leave blank to ignore): ").strip().lower()
    role = input("Enter role (leave blank to ignore): ").strip().lower()
    age_input = input("Enter age (leave blank to ignore): ").strip()

    try:
        age = int(age_input) if age_input else None
        results = []
        for employee in employees:
            department_match = (not department or employee["department"].lower() == department)
            role_match = (not role or employee["role"].lower() == role)
            age_match = (age is None or employee["age"] == age)

            if department_match and role_match and age_match:
                results.append(employee)

        if not results:
            print("No matching employees found.")
            logger.warning("Employee filter returned no results.")
            return []

        print("\nMatching Employees")
        print("-" * 30)

        for employee in results:
            print(employee)
        logger.info(f"Employee filter returned {len(results)} result(s).")
        return results

    except ValueError:
        print("Invalid age. Please enter a valid number.")
        logger.error("Invalid age entered during employee filtering.")
        return []



#viewing all employee record
def view_all_employees(employees):

    if not employees:
        print("\nNo employees available.")
        return

    print("\n" + "=" * 80)
    print("                         ALL EMPLOYEES")
    print("=" * 80)

    for employee in employees:
        print(f"ID         : {employee['id']}")
        print(f"Name       : {employee['name']}")
        print(f"Age        : {employee['age']}")
        print(f"Department : {employee['department']}")
        print(f"Role       : {employee['role']}")
        print(f"Salary     : {employee['salary']}")
        print(f"Email      : {employee['email']}")

        print("-" * 80)

    logger.info(f"Displayed {len(employees)} employee record(s).")
