grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
avg_0 = sum(grades[0])/len(grades)
avg_1 = sum(grades[1])/len(grades[1])
avg_2 = sum(grades[2])/len(grades[2])
avg_3 = sum(grades[3])/len(grades[3])
avg_4 = sum(grades[4])/len(grades[4])
grades_avg = [[avg_0], [avg_1], [avg_2], [avg_3], [avg_4]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sort = sorted(students)
students_avg_grades = dict(zip(students_sort, grades_avg))
print (students_avg_grades)
