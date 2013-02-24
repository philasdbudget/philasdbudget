# Convert CSV to GeoJSON for Schools #
import csv
import json

csv_file = open('./SchoolMetaDataNotes/schools_geocoded.csv', 'r')
output = open('./SchoolMetaDataNotes/schools_geocoded.geojson', 'w')

json_container = []

csv_reader = csv.DictReader(csv_file)
for row in csv_reader:
	geo_obj = {"type": "Feature",
		"properties": {"code":row['school_code']},
		"geometry": {
			"type": "Point",
			"coordinates":[row['lng'], row['lat']]
		}
	}
	json_container.append(geo_obj)

output.write(json.dumps(json_container))
output.close()
