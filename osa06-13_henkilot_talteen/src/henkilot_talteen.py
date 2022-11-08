# tee ratkaisu tänne

def tallenna_henkilo(henkilo: tuple):
    with open('henkilot.csv', 'a') as file:
        henkilo_data = []
        henkilo_data.append(henkilo[0])
        henkilo_data.append(str(henkilo[1]))
        henkilo_data.append(str(henkilo[2]))
        line = ';'.join(henkilo_data) + '\n'
        file.write(line)