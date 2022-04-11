import json
import os

file = open('./feature_to_id.json')

jsonFile = json.load(file)

all =set()

for x, y in jsonFile.items():
    vals = repr(x)
    for i in vals:
        all.add(i)
all.remove(' ')
all = list(all)
print(all)
with open("./id_to_productList.json", "r") as jsonFile:
    data = json.load(jsonFile)
with open("./feature_to_id.json", "r") as jsonFile:
    feature_to_id = json.load(jsonFile)
id_to_feature={}

for key in feature_to_id:
    id_to_feature[feature_to_id[key]]=key

with open("sample.json", "w") as outfile:
    json.dump(data["0"], outfile)
for key in id_to_feature:
    #for every key
    #make the trie path
    #Create json file containing the prod list and frequency
    directory = "file"
    parent_dir = "./Trie"
    key_string=int(key)
    feature_name = id_to_feature[key]
    for ch in feature_name:
       parent_dir+='/'
       parent_dir+=str(ord(ch))
    parent_dir+='/'
    mode = 0o666
    path = os.path.join(parent_dir, directory) 
    try:
        os.makedirs(path, exist_ok = True)
        parent_dir+="file/file.json"
        with open(parent_dir, "w") as outfile:
            obj = {"id":key, "data": data[str(key_string)]}
            json.dump(obj, outfile)
    except OSError as error:
        print(error)
    
