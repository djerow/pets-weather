#build list of US weather station facilities

#class definitions 
class WeatherStation:
    def __init__(self):
        self.station_ID = None
        self.latitude = 0.0
        self.longitude = 0.0
        self.state = None
        self.name = None

def main():
    station = WeatherStation()
    station_list = []

    #open ghcnd-states file to build list of weather stations w/ station metadata
    with open("NOAA/ghcnd-stations.txt", 'r') as f:
        for i, line in enumerate(f):
            content = f.readline()
            #loop through file to get list of stations that have a US state
            if content[38] == " ":
                pass
            else:
                station.station_ID = content[0:11]
                station.latitude = content[12:20]
                station.longitude = content[21:30]
                station.state = content[38:40]
                station.name = content[41:71]
                station_list.append(station) 
    
    #test cases for weather 
    total_stations = len(station_list)
    print(station_list[1245].station_ID)
    print(station_list[1245].latitude)
    print(station_list[1245].longitude)
    print(station_list[1245].state)
    print(station_list[1245].name)

    print("total station count is: " + str(total_stations))

    #This is serving as a check for all rows within station file 
    with open("NOAA/ghcnd-stations.txt", 'r') as f:
        line_count = 0
        for i, line in enumerate(f):
            pass        
        line_count = i + 1
    print("total line count: " + str(line_count))

if __name__ == "__main__":
    main()
