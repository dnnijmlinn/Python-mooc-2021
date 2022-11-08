import math
from unicodedata import name
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

def summary_score(x):
    point = {}
    for i in x:
        res = 0
        for j in x[i]:
            res += int(j)
        point[i] = res
    return point


def grade(exercise_point,exam_point):
    student_grade = {}
    for i in exercise_point:
        student_grade[i] = exam_point[i] + math.floor(exercise_point[i]/4)
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



def print_statistic(student,exam_point,exercise_point,student_grade):
    print(f"{'nimi':30}teht_lkm  teht_pist koe_pist  yht_pist  arvosana")
    for i in student:
        print(f"{student[i][0]+' '+student[i][1]:30}{exercise_point[i]:<10}{math.floor(exercise_point[i]/4):<10}{exam_point[i]:<10}{math.floor(exercise_point[i]/4)+exam_point[i]:<10}{student_grade[i]:<10}")

    
            
if True:
    # this is never executed
    student_info = input("Opiskelijatiedot: ")
    exercise_data = input("Tehtävätiedot: ")
    exam_point_data = input('Koepisteet: ')
else:
    # hard-coded input
    student_info = "opiskelijat1.csv"
    exercise_data = "tehtavat1.csv"
    exam_point_data = "koepisteet1.csv"


student = read_file(student_info)
exercise = read_file(exercise_data)
exam = read_file(exam_point_data)
exam_point = summary_score(exam)
exercise_point = summary_score(exercise)
student_grade = grade(exercise_point,exam_point)
print_statistic(student,exam_point,exercise_point,student_grade)