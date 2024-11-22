grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [sum(sublist)/len(sublist) for sublist in grades]
grades_student = dict(zip(sorted(students), grades))
print(grades_student)


    