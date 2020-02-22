# Alejandro Jiménez Rocha - sai993 - @01689144

"""Problem 3: 30 points
Part 3A: Create a nested Python dictionary denoted students.
 The 1st Dictionary key is the ID-number (e.g. 11) that points to a 2nd dictionary as
the value.
 The 2nd nested Dictionary should contain name and grade as key (e.g. ‘name’,
‘grade’) pointing to the Student and Grade as value (e.g. ‘Bob’, 2.5)
"""

# Here I'm defining the Dictionary (Part 3A). It's spaced out for aesthetic purposes.
students = {'11':
            {'name': 'Bob', 'grade': 2.5},
            '21':
            {'name': 'Mary', 'grade': 3.5},
            '31':
            {'name': 'David', 'grade': 4.2},
            '42':
            {'name': 'John', 'grade': 4.1},
            '53':
            {'name': 'Alex', 'grade': 3.8}
            }

# End of Part 3A

"""Part 3b: Create a python function named averageGrade that inputs the dictionary
students and will compute and returns the average_grade
"""


def averageGrade(students):
    """Adds each student's grade parameter and returns gradeAvg, computed using the addition of
     all the grades divided by the length of the dictionary."""
    grade_add = 0
    for x in students:
        grade = students[x]['grade']
        grade_add = grade + grade_add
    average_grade = grade_add / len(students)
    return average_grade  # Returns the variable average_grade when the function is called.


"""Create another python function named nameList that inputs the dictionary students and
will print the name of students in alphabetical order"""


def nameList(students):
    """Takes the names of each student, places them in a separate list and alphabetizes them by using .sort()"""
    alpha_students = []
    for x in students:
        alpha_students.append([students[x]['name']])
    alpha_students.sort()
    print(alpha_students)  # Prints the list when the function is called.


"""Create another python function named gradeList that inputs the dictionary students and
will print the name of students in grade order, highest grade first to lowest grade last"""


def gradeList(students):
    """I hope this works."""
    ordered_students = []  # Define a list for the end, where all the ordered students are put.
    ordered_grades = []  # Defines another list, this one I'm using in the first for loop.

    for x in students:  # Iterates through the Dictionary.
        ordered_grades.append([f"{students[x]['grade']}: ", f"{students[x]['name']}"])
        # ^ Adds both into a more accessible nested list, where I can use another for loop.
        # It's important that the grades come first so they're ordered correctly.
        ordered_grades.sort()  # Orders them from smallest to largest. (2.5... 4.2)
        ordered_grades.reverse()  # Flips that around, so now it's from largest to smallest (4.2... 2.5)
    student_length = len(ordered_grades)
    # ^ Failsafe in case the dictionary changes, so it can be sure to iterate through everything in the next for loop.

    for x in range(0, student_length):  # Goes from index zero to the length of the ordered grades list.
        ordered_students.append(ordered_grades[x][1])
        # Since the first for loop puts the names in index 1 of the nested list ordered_grades, it just adds the names
        # into ordered_students. Ex. ordered_grades[0][1] = 'David' since ordered_grades[0] = ['4.2', 'David'].

    print(ordered_students)  # Prints the list when the function is called.


"""Write a python script that invokes the averageGrade function and prints “The average
grade is “ average_grade"""


print(f'The average grade is {averageGrade(students)}')

# End of Part 3B. I'm a little wary since the end just implies averageGrade should be printed out, so hopefully that's
# all I have to do for this section. Forgive me if I missed anything!
