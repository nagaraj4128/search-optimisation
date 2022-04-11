import json
import os

foldername = os.listdir("processed-data-sets/")

AllData = {}

for file in foldername:
    file = open("processed-data-sets/"+file)

    json_format = {}

    for i in file:
        feature = i.split(" ", 1)
        json_format[feature[0]] = feature[1].strip("\n")

    # print(json_format)
    if json_format["domain"] in AllData:
        AllData[json_format["domain"]].append(json_format)
    else:
        AllData[json_format["domain"]] = [json_format]

    
for domain,data in AllData.items():
    out_file = open("New processed Data/"+str(domain)+".json", "w")
    # jsonString = json.dumps(data)
    json.dump(data, out_file, indent=4, sort_keys=True)
    out_file.close()
    print(data)
    

# print(AllData["Bottle"])
    