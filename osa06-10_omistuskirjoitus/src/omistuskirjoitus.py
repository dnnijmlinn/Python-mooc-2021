# tee ratkaisu tänne
name = input("Whom should I sign this to: ")
file = input("Where shall I save it: ")

with open(file, "w") as new_file:
    new_file.write(f"Hei {name}, toivomme viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi")