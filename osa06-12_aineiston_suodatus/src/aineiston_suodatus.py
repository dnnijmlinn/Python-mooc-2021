def suodata_laskut():
    file_to_list = []
    
    with open("laskut.csv") as solutions, open("oikeat.csv", "w") as correct_file, open("vaarat.csv", "w") as incorrect_file:
        for row in solutions:
            row = row.replace("\n", "")
            file_to_list.append(row.split(";"))
        
        for solution in file_to_list:
            line = ""
            if "-" in solution[1]:
                solution[1] = solution[1].split("-")
                correct = int(solution[1][0]) - int(solution[1][1]) == int(solution[2])
                solution.append("-")
                
            elif "+" in solution[1]:               
                solution[1] = solution[1].split("+")
                correct = int(solution[1][0]) + int(solution[1][1]) == int(solution[2])
                solution.append("+")
                
            line = f"{solution[0]};{solution[1][0]}{solution[3]}{solution[1][1]};{solution[2]}"
            if correct:
                correct_file.write(line + "\n")
            else:
                incorrect_file.write(line + "\n")
            
        

if __name__ == "__main__":
    suodata_laskut()