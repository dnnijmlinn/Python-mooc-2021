# Korjaa ohjelma
points = int(input("Kuinka paljon pisteitä? "))
if points < 100:
    value = points * 1.1
    print("Sait 10 %" + "bonusta")
if points >= 100:
    value = points * 1.15
    print("Sait 15 %")
print(f"Pisteitä on nyt {value} ")