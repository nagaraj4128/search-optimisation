import json

AllData = open("/home/sumit/Desktop/project/AllData.json")

AllData = json.load(AllData)

id_mapping = {}

for id, data in AllData.items():
    for feature, value in data.items():
        if value=="yes":
            value  = feature
        if value =="no":
            continue
        if value in id_mapping:
            id_mapping[value].append(id)
        else:
            id_mapping[value] = [id]


out_file = open("Id_Mapped_Data"+".json", "w")
    # jsonString = json.dumps(data)
json.dump(id_mapping, out_file, indent=4, sort_keys=True)
out_file.close()
