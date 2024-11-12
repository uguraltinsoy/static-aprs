# Static - APRS

This application is a simple APRS bridge for amateurs using static location via computer. As long as the program remains open, it will send data continuously during the specified interval.

### Variables
- ```Callsign: NOCALL``` -> Your callsign and ssid
- ```Server Europe/Africa: euro.aprs2.net``` ->  Server used for APRS
- ```Comment: No comment``` -> Your APRS description
- ```latitude: 40.9690591``` -> Latitude Location
- ```longitude: 29.1041687``` -> Longitude Location
- ```Symbol: / - ```-> Symbol table and symbol
- ```Interval: 60 ```-> Renewal interval

## Installation 1
```Cmd
docker run -d --name aprs-container -e TERM=xterm -e SERVER=4 -e CALLSIGN=NOCALL -e SSID=10 -e LAT=0.0 -e LON=0.0 -e SYMBOL_TABLE="/" -e SYMBOL="-" -e COMMENT="No comment" -e INTERVAL=900 uguraltnsy/static-aprs
```
```Dockfile
docker run -d \ 
	--name aprs-container \ 
	-e TERM=xterm \ 
	-e SERVER=4 \ 
	-e CALLSIGN=NOCALL \ 
	-e SSID=10 \ 
	-e LAT=0.0 \ 
	-e LON=0.0 \ 
	-e SYMBOL_TABLE="/" \ 
	-e SYMBOL="-" \ 
	-e COMMENT="No comment" \ 
	-e INTERVAL=900 \ 
	uguraltnsy/static-aprs
```

## Installation 2 Compose Method ```docker-compose.yml```
## !Edit the ```docker-compose.yml``` file before running
```Cmd
docker-compose up -d
```
or
```Cmd
docker compose up -d
```
## Stop application
```Cmd
docker compose down
```
