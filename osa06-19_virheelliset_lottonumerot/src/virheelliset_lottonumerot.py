def is_week_valid(week: str):
    try:
        week = int(week)
        return True
    except:
        return False

def are_numbers_valid(numbers: list):
    try:
        numbers = numbers.split(',')

        if len(numbers) != 7:
            return False
        
        for num in numbers:
            number = int(num)
            if number < 1 or number > 39 or numbers.count(num) > 1:
                return False

        return True
    
    except:
        return False

def suodata_virheelliset():
    open('korjatut_numerot.csv', 'w').close()
    correct_file = open('korjatut_numerot.csv', 'a')
    with open('lottonumerot.csv') as lottery_file:
        for line in lottery_file:
            original_line = line
            line = line.replace('\n','')
            parts = line.split(';')
            week = parts[0].split(' ')[1]
            numbers = parts[1]
            if is_week_valid(week) and are_numbers_valid(numbers):
                correct_file.write(original_line)
    correct_file.close()

if __name__ == "__main__":        
    suodata_virheelliset()