#Dependencies
import requests
import json
import pandas as pd

#json feeds for location of station, and various station statuses
url_stations = 'https://feeds.citibikenyc.com/stations/stations.json'
url_station_status = "https://gbfs.citibikenyc.com/gbfs/fr/station_status.json"


#get json information as a python variable
response_stations = requests.get(url_stations).json()
response_stations_status = requests.get(url_station_status).json()

#dictionary for storry 
response_dict_stations = {}
response_dict_status = {}
#response_data = response['data']

fieldnames = ['id', 'name', 'lat', 'long']

for each in response_stations['stationBeanList']:
    response_dict_stations[each['id']] = [each['stationName'], each['latitude'], each['longitude']]

response_stations_df = pd.DataFrame.from_dict(response_dict_stations, orient = 'index', columns= ['stationName', 'latitude', 'longitude'])
#print(response_df)
for each in response_stations_status['data']['stations']:
    response_dict_status[each['station_id']] = [each['is_installed'],each['num_docks_available'],each['is_returning'],each['num_bikes_disabled'],each['num_ebikes_available'],each['num_bikes_available']]

response_status_df = pd.DataFrame.from_dict(response_dict_status, orient = 'index', columns=['is_installed', 'num_docks_available', 'is_returning', 'num_bikes_disabled', 'num_ebikes_available', 'num_bikes_available'])


response_stations_df.to_csv('stations.csv', index = True, encoding='utf-8')
response_status_df.to_csv('stationsStatus.csv', index = True, encoding='utf-8')
#for each in response_stations_status['stationBeanList']:
 #   response_dict[each['id']] = [each['stationName'], each['latitude'], each['longitude']]


