def file_to_dict(filename: str):
    file_to_list = []
    file_to_dict = {}
    with open(filename) as new_file:
        for row in new_file:
            if "Longitude" not in row:
                row = row.replace("\n", "")
                file_to_list.append(row.split(";"))
        for station in file_to_list:
            file_to_dict[station[3]] = station
    return file_to_dict

def hae_asematiedot(filename: str):
    station_data = file_to_dict(filename)
    station_location = {}
    for key, value in station_data.items():
        station_location[key] = (float(value[0]), float(value[1]))
    return station_location
    
def etaisyys(stations: dict, station1: str, station2: str):
    import math
    x_km = (stations[station1][0] - stations[station2][0]) * 55.26
    y_km = (stations[station1][1] - stations[station2][1]) * 111.2
    etaisyys_km = math.sqrt(x_km**2 + y_km**2)
    return etaisyys_km
  
def suurin_etaisyys(stations: dict):
    max_etaisyys = 0.0
    for key in stations:
        for key2 in stations:
            if etaisyys(stations, key, key2) > max_etaisyys:
                max_etaisyys = etaisyys(stations, key, key2)
                station_max_etaisyys = (key, key2, max_etaisyys)
    return station_max_etaisyys
    
if __name__ == "__main__":
    stations = hae_asematiedot('stations1.csv')
    station1, station2, greatest = suurin_etaisyys(stations)
    print(station1, station2, greatest)