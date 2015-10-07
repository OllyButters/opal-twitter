import sys

if len(sys.argv) > 1:
    line_generator = open(sys.argv[1])
else:
    line_generator = sys.stdin

import json
import csv
import os

output_csv_file = '/tmp/tweets.csv'
with open(output_csv_file,'wb') as csvfile:
    string_file = csv.writer(csvfile)

    #opal likes a header in its csv file imports
    string_file.writerow(['id', 'tweet', 'lat', 'long', 'timestamp'])

    for line in line_generator:
        #print line
        line_object = json.loads(line)
        for i in range(0,1000):
            print i
            #print line_object[i]
            timestamp = line_object[i]['created_at']
            tweet = line_object[i]['text']
            place_object = line_object[i]['place']
            #print place_object
            try:
                location = line_object[i]['place']['name']
                print location
            except:
                print 'no good location data'
                pass

            string_file.writerow([i, tweet.encode('utf-8'), '0', '0', timestamp])

            #print line_object[0]['text']
            #exit(1)

exit(1)
opal_address='192.168.56.100:8080'
cmd = 'opal file --opal http://'+opal_address+' --user administrator --password password -up '+output_csv_file+' /home/administrator'
os.system(cmd)
cmd = 'opal import-csv -o http://'+opal_address+' --user administrator --password password --destination twitter --table tweets --path /home/administrator/tweets.csv --type Book'
os.system(cmd)
