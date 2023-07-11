EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis"
    },
    {
        "id": 2,
        "name": "Rip Van Winkle"
    }
]

def get_all_employees():
    #making a function to grab all employees
    return EMPLOYEES

def get_single_employee(id):
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]
    correct_id = max_id + 1
    employee["id"] = correct_id
    EMPLOYEES.append(employee)
    return employee

def delete_employee(id):
    employee_index = -1 
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index
        if employee_index >= 0:
            EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Update the value.
            EMPLOYEES[index] = new_employee
            break

