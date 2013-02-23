# Geocode Schools #
from geopy import geocoders
import csv

school_csv = open('./SchoolMetaDataNotes/schoolinformation.csv', 'r')
school_long_lat = open('./SchoolMetaDataNotes/schools_geocoded.csv', 'w')

school_reader = csv.DictReader(school_csv)

g = geocoders.Yahoo('YQEyGPDV34FG4bXzx_UKz0hQJjlnwOQ2pBjOPzIbnZ.xaMD9lln5zYAXkeyTj3O99K84AZmD6KX50BDkM57rx42T_chc0kg-')
school_long_lat.write("school_code,lat,lng")
for row in school_reader:
	address = "%s %s" % (row['ADDRESS'], row['SCHOOL_ZIP'])
	place, (lat, lng) = g.geocode(address)
	school_long_lat.write("%s,%s,%s\n" %(row['SCHOOL_CODE'], lat, lng))