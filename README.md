# module-noaa-stations

Zimagi module for collecting data from NOAA weather station data

Historical through current weather data, by station, is available at:

> https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/

Metadata about meaning of station data fields is at:

> https://www.ncei.noaa.gov/data/global-summary-of-the-day/doc/readme.txt

Cross reference station information by identifier is (probably) at:

> https://www.ncdc.noaa.gov/homr/file/mshr_enhanced.txt.zip

Metadata about the meaning of station fields is at:

> https://www.ncdc.noaa.gov/homr/file/MSHR_Enhanced_Table.txt

General station metadata landing page:

> https://www.ncdc.noaa.gov/homr/reports

Additional 3rd-party human-readable documentation of station metadata details:

> http://www.weathergraphics.com/identifiers/master-location-identifier-database.pdf

## Initializing Zimagi

```bash
(local) vagrant up
(local) vagrant ssh
```

```bash
(vagrant) zimagi env get
(vagrant) zimagi module add https://github.com/zimagi/module-noaa-stations.git
(vagrant) zimagi env get
```

```bash
(local) cd lib/modules/default/
(local) ls noaa-stations
```

After editing e.g. station.yml:

```bash
(vagrant) # Pull changes from GitHub:
(vagrant) zimagi module save noaa-stations
(vagrant) zimagi makemigrations
```

Add a remote to the working zimagi repo for the module 

```bash
(local) git remote add noaa git@github.com:zimagi/module-noaa-stations.git
(local) git push noaa master
```

