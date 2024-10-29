grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
s = sorted(students)
zipped = zip(s, grades)
students_grades = dict(zipped)
#print(students_grades)
students_grades.update({'Aaron':sum(students_grades['Aaron']) / len(students_grades['Aaron']),
                        'Bilbo':sum(students_grades['Bilbo']) / len(students_grades['Bilbo']),
                        'Johnny':sum(students_grades['Johnny']) / len(students_grades['Johnny']),
                        'Khendrik':sum(students_grades['Khendrik']) / len(students_grades['Khendrik']),
                        'Steve':sum(students_grades['Steve']) / len(students_grades['Steve'])})
print(students_grades)
