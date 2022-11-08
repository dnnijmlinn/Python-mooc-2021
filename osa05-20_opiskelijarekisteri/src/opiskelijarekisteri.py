def lisaa_opiskelija(students: dict, name: str):
    students[name] = []
   
def lisaa_suoritus(students: dict, name: str, course: tuple):
    if name in students and course[1] > 0:
        if len(students[name]) == 0:
            students[name].append(course)
        else:
            l = len(students[name])
            for x in range(l):
                if course[0] != students[name][x][0]:
                    students[name].append(course)
                    return
                else:
                    if course[1] > students[name][x][1]:
                        students[name].pop(x)
                        students[name].append(course)
                                               
def tulosta(students: dict, name: str):
    if name not in students:
        print(f"ei löytynyt ketään nimellä {name}")
    else:
        grade_sum = 0
        print(f"{name}:")
        if students[name] == []:
            print(f" ei suorituksia")
        else:
            print(f" suorituksia {len(students[name])} kurssilta:")
            for course in range(len(students[name])):
                print(f"  {students[name][course][0]} {students[name][course][1]}")
                grade_sum += students[name][course][1]
            print(f" keskiarvo {grade_sum / len(students[name])}")

def kooste(students: dict):
    print(f"opiskelijoita {len(students)}")
    total = 0
    for key in students:
        if total < len(students[key]):
            total = len(students[key])
            name = key
    print(f"eniten suorituksia {total} {name}")
    
    grade_sum = 0
    average = 0
    for key in students:
        grade_sum = 0
        for course in range(len(students[key])):
            grade_sum += students[key][course][1]
        if average < grade_sum / len(students[key]):
            average = grade_sum / len(students[key])
            name_av = key
    print(f"paras keskiarvo {average} {name_av}")
    

if __name__ == "__main__":
    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "emilia")
    lisaa_opiskelija(opiskelijat, "pekka")
    lisaa_suoritus(opiskelijat, "emilia", ("ohpe", 4))
    lisaa_suoritus(opiskelijat, "emilia", ("ohpe", 5))
    lisaa_suoritus(opiskelijat, "pekka", ("tira", 3))
    lisaa_suoritus(opiskelijat, "pekka", ("lama", 0))
    lisaa_suoritus(opiskelijat, "pekka", ("tira", 2))
    lisaa_suoritus(opiskelijat, "pekka", ("jtkt", 1))
    lisaa_suoritus(opiskelijat, "pekka", ("ohtu", 3))
    kooste(opiskelijat)
    kooste(opiskelijat)
