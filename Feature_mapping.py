import json
import os

foldername = os.listdir("processed-data-sets/")

AllData = {}

for file in foldername:
    file = open("processed-data-sets/"+file)

    json_format = {}

    for i in file:
        i = i.lower()
        feature = i.split(" ", 1)
        json_format[feature[0]] = feature[1].strip("\n")
        
    AllData[json_format["id"]] = json_format
    
out_file = open("AllData"+".json", "w")
json.dump(AllData, out_file, indent=4, sort_keys=True)
out_file.close()
