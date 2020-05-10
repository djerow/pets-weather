# README
**Overview:**

Script to get historical weather data from the National Oceanic & Atmospheric Administration for all US Weather stations and translate that to average temperature metrics for all major US cities.

Script output is a CSV file that contains the following:
1. Date 
2. City
3. State
4. Max Daily Temperature 
5. Min Temperature 
6. Precipatation 

Data Source URL: ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/

## License:


## Tasks:
1.  Get Historical weather data for every weather station in from U.S. Historical Climatology Network 
    (U.S. HCN) using: "ghcnd-hcn.tar.gz"
2.  Filter weather list for all weather locations 
3.  Provide script that generates CSV file of following data for specified cities list:
    1.   Max Daily Temperature 
    2.   Min Daily Temperature 
    3.   Precipitation   
4. GET NOAA - NCEI Historical Daily weather CSV file through NCEI FTP server for all weather reading locations 
5. Parse CSV file for only US locations and append to newly generated CSV file 
6. Remove non-specified columns from newly generated files 

## Questions
1. Does it matter if there are multiple weather stations within a given city? 


