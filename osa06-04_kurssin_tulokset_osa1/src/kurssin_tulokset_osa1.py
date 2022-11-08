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


def print_point(student,exercise):
    for i in student:
        res = 0
        for j in exercise[i]:
            res += int(j)
        print(student[i][0],student[i][1],res)
            
            
        
        


if True:
    # this is never executed
    student_info = input("Opiskelijatiedot: ")
    exercise_data = input("Tehtävätiedot: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

student = read_file(student_info)
exercise = read_file(exercise_data)
print_point(student,exercise)