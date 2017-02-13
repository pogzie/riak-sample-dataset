import csv
import sys
#import os
#import subprocess
from subprocess import call

RIAK_HOST = "http://127.0.0.1:10018"

f = open(sys.argv[1], 'rt')
try:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        position = row[0]
	jersey = row[1]
	name = row[2]
	height = row[3]
	weight = row[4]
	dob = row[5]
	location = row[6]
	team = row[7]
	division = row[8]
	conference = row[9]
	#print jersey
	
	# Compose the JSON here
	json_string = '{"position_s":"' + position + '", "jersey_s":"' + jersey + '", "name_s":"' + name + '", "height_s":"' + height + '", "weight_s":"' + weight + '", "dob_s":"' + dob + '", "location_s":"' + location + '", "team_s":"' + team + '", "division_s":"' + division + '", "conference_s":"' + conference + '"}'
	#print json_string

	key = jersey + team
	key = key.replace(" ","")

	# Assemble the URL
	assembled_url = "curl -XPUT " + RIAK_HOST + "/types/nba_players/buckets/players/keys/" + key + " -H 'Content-Type: application/json' -d '" + json_string + "'" 
	print assembled_url

	# Run the curl here
	# For less complication, lets just invoke a system command
	# shell=True is unsafe, but.. meh.
	call(assembled_url, shell=True)

finally:
    f.close()
