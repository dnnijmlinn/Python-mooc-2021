# tee ratkaisu tänne
def eniten_kirjainta(my_string: str):
    most_common = my_string[0]
    for character in my_string:
        if my_string.count(character) > my_string.count(most_common):
            most_common = character
 
    return most_common
    

if __name__ == "__main__":
    second_string = "exemplaryelementary"
    print(eniten_kirjainta(second_string))