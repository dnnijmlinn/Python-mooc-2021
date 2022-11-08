from datetime import datetime, timedelta

if True:
    file_name = input('Tiedosto: ')
    start_date = input('Aloituspäivä: ')
    how_many_days = int(input('Montako päivää: '))
else:
    file_name = 'kesakuun_loppu.txt'
    start_date = '24.6.2020'
    how_many_days = 5

start_date = datetime.strptime(start_date,'%d.%m.%Y')
print('Anna ruutuajat kunakin päivänä minuutteina (TV tietokone mobiililaite):')
data = {}
total_min = 0
for i in range(how_many_days):
    date = start_date + timedelta(days = i)
    s = input("Screen time " + date.strftime('%d.%m.%Y') +': ')
    #s = '1 1 1'
    hour = []
    part = s.strip().split(' ')
    for j in part:
        n = int(j)
        total_min += n
    data[(start_date + timedelta(i)).strftime('%d.%m.%Y')] = part[0]+'/'+part[1]+ '/' +part[2]

with open(file_name,'w') as f:
    start_date_str = start_date.strftime('%d.%m.%Y')
    end_data_str = (start_date + timedelta(days = how_many_days-1)).strftime('%d.%m.%Y')
    f.write(f'Ajanjakso: {start_date_str}-{end_data_str}\n')
    f.write(f'Yht. minuutteja: {total_min}\n')
    f.write(f'Keskim. minuutteja: {total_min/how_many_days}\n')
    for i in data:
        f.write(f'{i}: {data[i]}\n')