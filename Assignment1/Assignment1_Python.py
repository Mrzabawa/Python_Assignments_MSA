#Aug 20, 2019
#Michael Zabawa
#Python Assignment 1 for NCSU

#imports packages
from forecastiopy import *
import csv
#michael Zabawa api key for Dark Sky API https://darksky.net/dev
api_key = '6833ed31b7c59925b67a7b578f78b544'

#locations to query for assignment stored in a dict
#location is a string, latitude and longitude are stored in an array, key = location : value is an array of latitude and longitude
locations = {
"Anchorage, Alaska":[61.2181, -149.9003],
"Buenos Aires, Argentia":[-34.6037, -58.3816],
"Sao Jose dos Campos, Brazil":[-23.2237, -45.9009],
"San Jose, Costa Rica":[9.9281, -84.0907],
"Nanaimo, Canada":[49.1659, -123.9401],
"Ningbo, China":[29.8683, 121.5440],
"Giza, Egypt":[30.0131, 31.2089],
"Mannheim, Germany":[49.4875, 8.4660],
"Hyderabad, India":[17.3850, 78.4867],
"Tehran, Iran":[35.6892, 51.3890],
"Bishkek, Kyrgyzstan":[42.8746, 74.5698],
"Riga, Latvia":[56.9496, 24.1052],
"Quetta, Pakistan":[30.1798, 66.9750],
"Warsaw, Poland":[52.2297, 21.0122],
"Dhahran, Saudia Arabia":[26.2361, 50.0393],
"Madrid, Spain":[40.4168, -3.7038],
"Oldham, United Kingdom":[53.5409, -2.1114]}
##########################################################################################################
#defines an empty dict to store the temps to keep from querying too much
temps = {}
#queries temps for each location and stores them in temps with location as key
for loc in locations:
    weather = ForecastIO.ForecastIO( api_key, units=ForecastIO.ForecastIO.UNITS_SI, latitude=locations[loc][0], longitude=locations[loc][1] )
    daily = FIODaily.FIODaily( weather )
    temps[loc] = daily

##########################################################################################################
#open File
out = open( 'temp.csv', 'a')
#outputs header
out.write("City, Min 1, Max 1, Min 2, Max 2, Min 3, Max 3, Min 4, Max 4, Min 5, Max 5, Min Avg, Max Avg")
out.write("\r\n")
#decomposes temps by location, adds average temps and stores in temps.csv
for local in temps:
    #create Array to store min and max temps for average
    minTemps = [0]*5
    maxTemps = [0]*5
    #write out city
    out.write('"' + str(local) + '"')
    out.write(',')
    #Get Forecast for each city
    for day in range( 2, 7):
        val = temps[local].get( day )
        min = val[ 'temperatureMin' ]
        max = val[ 'temperatureMax' ]
        out.write( str("% .2f "% min))#Write out min and set format to exactly 2 dec
        out.write(',')#for csv
        out.write( str("% .2f "% max))#Write out max and set format to 2 dec
        out.write(',')#for csv
        minTemps[day-2] = float(val[ 'temperatureMin' ])#store min and max for average
        maxTemps[day-2] = float(val[ 'temperatureMax' ])
    avgMin = ((minTemps[0]+minTemps[1]+minTemps[2]+minTemps[3]+minTemps[4]) / 5.0)#compute average
    avgMax = ((maxTemps[0]+maxTemps[1]+maxTemps[2]+maxTemps[3]+maxTemps[4]) / 5.0)
    out.write(str("%3.2f "%avgMin))
    out.write(',')
    out.write(str("%3.2f "%avgMax))
    out.write("\n")

out.close()





