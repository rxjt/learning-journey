# A student Grade Analyer.

# To make sure the user enters only five grades.
number = 5 

# A list to store the grades.
grades = [] 

# A loop that ask the user to enter the grades.
for i in range(number):
    n = int(input("Enter the student's grades, please:"))

    while n < 0 or n > 100:
     n = int(input("Invalid grade! Try again, please: "))
    grades.append(n)
 
# Calculate the Average.
AverageGs = sum(grades) / len(grades)
print(f"The Averages grade is : {AverageGs}")

# Find the highest grade.
MaxGs = max(grades)
print(f"The highest grade is: {MaxGs}")

# Find the lowest grade.
MinGs = min(grades)
print(f"The lowest grade is: {MinGs}")

