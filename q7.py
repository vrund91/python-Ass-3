emp_name=""
emp_salary=""

def employee(emp_name,emp_salary=10000):
    emp_name=input("Enter a name:")
    salary_input=input("Enter a salary:")

    if salary_input == "":
        emp_salary=10000
    else:
        emp_salary=int(salary_input)

    print(emp_name)
    print(emp_salary)


employee(emp_name,emp_salary)