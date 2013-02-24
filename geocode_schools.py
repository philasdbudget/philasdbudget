# Geocode Schools #
from geopy import geocoders
import csv

school_csv = open('./SchoolMetaDataNotes/schoolinformation.csv', 'r')
school_long_lat = open('./SchoolMetaDataNotes/schools_geocoded.csv', 'w+')
charter_csv = open('./SchoolMetaDataNotes/charterinformation.csv', 'rU')
school_reader = csv.DictReader(school_csv)
charter_reader = csv.DictReader(charter_csv)

g = geocoders.Yahoo('YQEyGPDV34FG4bXzx_UKz0hQJjlnwOQ2pBjOPzIbnZ.xaMD9lln5zYAXkeyTj3O99K84AZmD6KX50BDkM57rx42T_chc0kg-')
school_long_lat.write("school_code,lat,lng")

print "Geocoding Philadelphia School District Schools"
for counter, row in enumerate(school_reader):
	if counter % 25 == 0:
		print counter
	address = "%s %s" % (row['ADDRESS'], row['SCHOOL_ZIP'])
	place, (lat, lng) = g.geocode(address)
	school_long_lat.write("%s,%s,%s\n" %(row['SCHOOL_CODE'], lat, lng))

print "Geocoding Philadelphia Charter Schools"
for counter, row in enumerate(charter_reader):
	if counter % 25 == 0:
		print counter
	address = "%s %s" % (row['ADDRESS'], row['SCHOOL_ZIP'])
	try:
		place, (lat, lng) = g.geocode(address)
	except Exception, e:
		print "%s\nCode:%s\nAddress%s" % (e, row['SCHOOL_CODE'], address)
	school_long_lat.write("%s,%s,%s\n" %(row['SCHOOL_CODE'], lat, lng))
