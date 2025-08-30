employees = []
def payroll():
    employee_count = 0
    while True:
      print("\nWELCOME TO SEMICOLON EMPLOYEES PAYROLL")
      print("1. Add Employee Payroll")
      print("2. View Employees Payroll")
      print("3. Update Employee Payroll")
      print("4. Exit")
      choice = int(input("Enter input: "))
   
    if choice == 1:
      name = input("Enter Employee Name: ")
      exists = False
    for currentEmployee in range(employee_count):
      employee_name = employees[currentEmployee]["name"]
    if employee_name == name:
      print(name + " already exists")
      exists = True
      break
    if not exists:
      hours = float(input("Enter number of hours worked in a week: "))
    if hours >= 160:
      print("hours exceeded")
      continue_choice = input("do you wish to continue (yes/no): ")
    if continue_choice.lower() != "yes":
      continue
      pay_rate = float(input("Enter hourly pay rate: "))
      federal_tax_rate = float(input("Enter Federal tax withholding rate: "))
      state_tax_rate = float(input("Enter state tax withholding rate: "))
      employee = {"name": name, "hours": hours, "pay_rate": pay_rate, "federal_tax_rate": federal_tax_rate, "state_tax_rate": state_tax_rate}
      employees.append(emp)
      employee_count += 1
      print("Employee payroll added")
    
    elif choice == 2:
      name = input("Enter Employee Name: ")
    for currentEmployee in range(employee_count):
      employee_name = employees[currentEmployee]["name"]
    if employee_name == name:
      hours = employees[currentEmployee]["hours"]
      pay_rate = employees[currentEmployee]["pay_rate"]
      federal_tax_rate = employees[currentEmployee]["federal_tax_rate"]
      state_tax_rate = employees[currentEmployee]["state_tax_rate"]
      gross_pay = hours * pay_rate
      federal_tax = gross_pay * (federal_tax_rate / 100)
      state_tax = gross_pay * (state_tax_rate / 100)
      total_deduction = federal_tax + state_tax
      net_pay = gross_pay - total_deduction

      print("\nEmployee name: " + emp_name)
      print("Hours Worked: " + str(hours))
      print("Pay rate: " + str(pay_rate))
      print("Gross pay: $" + str(gross_pay))
      print("Deductions:")
      print("\tFederal withholding (" + str(federal_tax_rate) + "%): " + str(federal_tax))
      print("\tState withholding (" + str(state_tax_rate) + "%): " + str(state_tax))
      print("\tTotal Deduction: " + str(total_deduction))
      print("Net Pay: " + str(net_pay))
      break

    elif choice == 3:
      name = input("Enter Employee Name: ")
    for currentEmployee in range(employee_count):
      employee_name = employees[currentEmployee]["name"]
    if employee_name == name:
      hours = float(input("Enter number of hours worked in a week: "))
    if hours >= 160:
      print("hours exceeded")
      continue_choice = input("do you wish to continue (yes/no): ")
    if continue_choice.lower() != "yes":
      break
      pay_rate = float(input("Enter hourly pay rate: "))
      federal_tax_rate = float(input("Enter Federal tax withholding rate: "))
      state_tax_rate = float(input("Enter state tax withholding rate: "))
      employees[currentEmployee]["hours"] = hours
      employees[currentEmployee]["pay_rate"] = pay_rate
      employees[currentEmployee]["federal_tax_rate"] = federal_tax_rate      
      print("Employee payroll updated")
      break

    elif choice == 4:
      print("Exiting...")
      break
if __name__ == "__payroll__":
      payroll()