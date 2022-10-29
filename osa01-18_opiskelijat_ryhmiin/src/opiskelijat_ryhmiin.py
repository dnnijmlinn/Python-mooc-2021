students = int(input("Montako opiskelijaa? "))
size = int(input("Mikä on ryhmän koko? "))

groups = (students + size -1) // size

print("Ryhmien määrä: ", groups)