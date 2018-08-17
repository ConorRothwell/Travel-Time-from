import simplejson, urllib
from urllib.request import urlopen

def travel_time(location1_latitude, location1_longitude, location2_latitude, location2_longitude, time_units):
   
    if time_units == "hours" or time_units == "Hours":
        time_unit_correction = 3600
    elif time_units == "minutes" or time_units == "Minutes":
        time_unit_correction = 60
    elif time_units == "seconds" or time_units == "Seconds":
        time_unit_correction = 1
    else:
        print("Incorrect time unit entered. Please set time_units to either hours, minutes, or seconds")
        quit()
        
    orig_coord = str(str(location1_latitude) + "," + str(location1_longitude))
    dest_coord = str(str(location2_latitude) + "," + str(location2_longitude))
    url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false".format(orig_coord,dest_coord)
    result= simplejson.load(urllib.request.urlopen(url))
    
    driving_time = result['rows'][0]['elements'][0]['duration']['value'] # initially reported in seconds
    driving_time = round(driving_time/time_unit_correction,2)

    return driving_time
