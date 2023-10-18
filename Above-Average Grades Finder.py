grades = input("Enter the grades separated by spaces: ").split()
grades = [int(grade) for grade in grades]
average = sum(grades) / len(grades)
above_average = [grade for grade in grades if grade > average]
print("Grades above the average:", above_average)
