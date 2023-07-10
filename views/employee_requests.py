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