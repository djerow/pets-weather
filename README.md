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

Data Source URL: ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily

## Definitions 
### Weather Stations Text Structure 
Format: Variable | Columns | Type

1. ID | 1-11 | Character
2. LATITUDE | 13-20 | Real
3. LONGITUDE | 22-30 | Real
4. ELEVATION | 32-37 | Real
5. STATE | 39-40 | Character
6. NAME | 42-71 | Character
7. GSN FLAG | 73-75 | Character
8. HCN/CRN FLAG | 77-79 | Character
9. MO ID | 81-85 | Character

## Citations
Menne, M.J., I. Durre, B. Korzeniewski, S. McNeal, K. Thomas, X. Yin, S. Anthony, R. Ray, R.S. Vose, B.E.Gleason, and T.G. Houston, 2012: 

Global Historical Climatology Network - Daily (GHCN-Daily)

NOAA National Climatic Data Center. 
http://doi.org/10.7289/V5D21VHZ.
