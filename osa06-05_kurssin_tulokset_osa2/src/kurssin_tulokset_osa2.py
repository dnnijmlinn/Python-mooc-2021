import math


def read_file(file :str):
    with open(file) as f:
        students = {}
        s = f.read()
        s = s.strip().split("\n")
        header = s.pop(0)
        header = header.strip().split(";")
        for i in s:
            part = i.split(";")
            temp = []
            for j in range(1,len(part)):
                temp.append(part[j])
            students[part[0]] = temp    
    return students

def point(student,exercise):
    point = {}
    for i in student:
        res = 0
        for j in exercise[i]:
            res += int(j)
        point[i] = math.floor(res/4)
    return point

def grade(exercise,exam):
    student_grade = {}
    for i in exam:
        summary = 0
        for j in exam[i]:
            summary += int(j)
        student_grade[i] = summary
    exercise_score = point(student,exercise)
    for i in exam:
        student_grade[i] += exercise_score[i]
        if student_grade[i] < 15:
            student_grade[i] = 0
        elif student_grade[i] < 18:
            student_grade[i] = 1
        elif student_grade[i] < 21:
            student_grade[i] = 2
        elif student_grade[i] < 24:
            student_grade[i] = 3
        elif student_grade[i] < 28:
            student_grade[i] = 4
        else :
            student_grade[i] = 5
    return (student_grade)
            
if True:
    # this is never executed
    student_info = input("Opiskelijatiedot: ")
    exercise_data = input("Tehtävätiedot: ")
    exam_point_data = input('Koepisteet: ')



student = read_file(student_info)
exercise = read_file(exercise_data)
exam = read_file(exam_point_data)
student_grade = grade(exercise,exam)
for i in student:
    print(student[i][0],student[i][1],student_grade[i])