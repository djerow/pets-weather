# README
**Overview:**

Historical weather data from the National Oceanic & Atmospheric Administration. Script parses station metadata along with historical weather data to produce CSV output of historical weather data for all major US cities.

Script output is a CSV file that contains the following:
1. Date 
2. City
3. State
4. Max Daily Temperature 
5. Min Temperature 
6. Precipatation 

Data Source URL: ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily

## Definitions 
### Station Text File Structure 
File: ghcnd-stations.txt 

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

### Weather Data Text File Structure 
Format: Variable | Columns | Type

1. ID | 1-11 | Character
2. YEAR | 12-15 | Integer
3. MONTH | 16-17 |Integer
4. ELEMENT | 8-21 | Character
5. VALUE1 | 22-26 | Integer
6. MFLAG1 | 27-27 | Character
7. QFLAG1 | 28-28 | Character
8. SFLAG1 | 29-29 | Character
9. VALUE2 | 30-34 | Integer
10. MFLAG2 | 35-35 | Character
11. QFLAG2 | 36-36 | Character
12. SFLAG2 | 37-37 | Character

### Data Definitions

#### Variable Definitions:

* ID: is the station identification code.  Please see "ghcnd-stations.txt" for a complete list of stations and their metadata.
* YEAR: is the year of the record.
* MONTH: is the month of the record.
* ELEMENT: is the element type. There are five core elements as well as a number of addition elements.  

#### Element Definitions:

The five core elements are:
1. PRCP = Precipitation (tenths of mm)
2. SNOW = Snowfall (mm)
3. SNWD = Snow depth (mm)
4. TMAX = Maximum temperature (tenths of degrees C)
5. TMIN = Minimum temperature (tenths of degrees C)

Additional Elements Included:
1. AWND = Average daily wind speed (tenths of meters per second)
2. DAPR = Number of days included in the multiday precipiation total (MDPR)
3. DASF = Number of days included in the multiday snowfall total (MDSF)		  
4. DATN = Number of days included in the multiday minimum temperature (MDTN)
5. DATX = Number of days included in the multiday maximum temperature (MDTX)
6. DWPR = Number of days with non-zero precipitation included in multiday precipitation total (MDPR)
7. MDPR = Multiday precipitation total (tenths of mm; use with DAPR and DWPR, if available)
8. MDSF = Multiday snowfall total 
9. MDTN = Multiday minimum temperature (tenths of degrees C; use with DATN)
10. MDTX = Multiday maximum temperature (tenths of degress C; use with DATX)

#### Day Value Format
**VALUE1** is the value on the first day of the month (missing = -9999).

**MFLAG1** is the measurement flag for the first day of the month. There are ten possible values:
* Blank = no measurement information applicable
* B = precipitation total formed from two 12-hour totals
* D = precipitation total formed from four six-hour totals
* H = represents highest or lowest hourly temperature (TMAX or TMIN) or the average of hourly values (TAVG)
* K = converted from knots 
* L = temperature appears to be lagged with respect to reported hour of observation 
* O = converted from oktas 
* P = identified as "missing presumed zero" in DSI 3200 and 3206
* T = trace of precipitation, snowfall, or snow depth
* W = converted from 16-point WBAN code (for wind direction)

**QFLAG1** is the quality flag for the first day of the month. There are fourteen possible values:
* Blank = did not fail any quality assurance check
* D = failed duplicate check
* G = failed gap check
* I = failed internal consistency check
* K = failed streak/frequent-value check
* L = failed check on length of multiday period 
* M = failed megaconsistency check
* N = failed naught check
* O = failed climatological outlier check
* R = failed lagged range check
* S = failed spatial consistency check
* T = failed temporal consistency check
* W = temperature too warm for snow
* X = failed bounds check
* Z = flagged as a result of an official Datzilla investigation

**SFLAG1** is the source flag for the first day of the month. There are thirty possible values (including blank, upper and lower case letters):
* Blank = No source (i.e., data value missing)
* 0 = U.S. Cooperative Summary of the Day (NCDC DSI-3200)
* 6 = CDMP Cooperative Summary of the Day (NCDC DSI-3206)
* 7 = U.S. Cooperative Summary of the Day -- Transmitted via WxCoder3 (NCDC DSI-3207)
* A = U.S. Automated Surface Observing System (ASOS) real-time data (since January 1, 2006)
* a = Australian data from the Australian Bureau of Meteorology
* B = U.S. ASOS data for October 2000-December 2005 (NCDC DSI-3211)
* b     = Belarus update
* C     = Environment Canada
* D     = Short time delay US National Weather Service CF6 daily summaries provided by the High Plains Regional Climate Center
* E     = European Climate Assessment and Dataset (Klein Tank et al., 2002)	   
* F     = U.S. Fort data 
* G     = Official Global Climate Observing System (GCOS) or other government-supplied data
* H     = High Plains Regional Climate Center real-time data
* I     = International collection (non U.S. data received through personal contacts)
* K     = U.S. Cooperative Summary of the Day data digitized from paper observer forms (from 2011 to present)
* M     = Monthly METAR Extract (additional ASOS data)
* m     = Data from the Mexican National Water Commission (Comision National del Agua -- CONAGUA)
* N     = Community Collaborative Rain, Hail,and Snow (CoCoRaHS
* Q     = Data from several African countries that had been "quarantined", that is, withheld from public release until permission was granted from the respective meteorological services
* R     = NCEI Reference Network Database (Climate Reference Network and Regional Climate Reference Network)
* r     = All-Russian Research Institute of Hydrometeorological Information-World Data Center
* S     = Global Summary of the Day (NCDC DSI-9618)
  * NOTE: "S" values are derived from hourly synoptic reports exchanged on the Global Telecommunications System (GTS). Daily values derived in this fashion may differ significantly from "true" daily data, particularly for precipitation (i.e., use with caution).
* s     = China Meteorological Administration/National Meteorological Information Center/Climatic Data Center (http://cdc.cma.gov.cn)
* T     = SNOwpack TELemtry (SNOTEL) data obtained from the U.S.
* Department of Agriculture's Natural Resources Conservation Service
* U     = Remote Automatic Weather Station (RAWS) data obtained from the Western Regional Climate Center	 
* u     = Ukraine update	   
* W     = WBAN/ASOS Summary of the Day from NCDC's Integrated Surface Data (ISD).  
* X     = U.S. First-Order Summary of the Day (NCDC DSI-3210)
* Z     = Datzilla official additions or replacements 
* z     = Uzbekistan update
	   
When data are available for the same time from more than one source,
the highest priority source is chosen according to the following
priority order (from highest to lowest):\n
Z,R,D,0,6,C,X,W,K,7,F,B,M,m,r,E,z,u,b,s,a,G,Q,I,A,N,T,U,H,S
	   
**VALUE2** is the value on the second day of the month

**MFLAG2** is the measurement flag for the second day of the month.

**QFLAG2** is the quality flag for the second day of the month.

**SFLAG2** is the source flag for the second day of the month.

... and so on through the 31st day of the month.  Note: If the month has less than 31 days, then the remaining variables are set to missing (e.g., for April, VALUE31 = -9999, MFLAG31 = blank, QFLAG31 = blank, SFLAG31 = blank).


## Citations
Menne, M.J., I. Durre, B. Korzeniewski, S. McNeal, K. Thomas, X. Yin, S. Anthony, R. Ray, R.S. Vose, B.E.Gleason, and T.G. Houston, 2012: 

Global Historical Climatology Network - Daily (GHCN-Daily)

NOAA National Climatic Data Center. 
http://doi.org/10.7289/V5D21VHZ.
