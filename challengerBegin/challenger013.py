print("="*17)
print("==CHALLENGER012==")
print("="*17)
print("The purpose of this programme is to calculate how much an employee's salary increase will be")
print("="*17)

currentSalary = float(input("Please provide the employee's current salary: "))
percentage = int(input("Indicate how many per cent will be added to the employee's salary. "))

addedValue = (currentSalary/100)*percentage
newSalary = currentSalary+addedValue

print("The new salary of the employee is R${:.2f}: ".format(newSalary))