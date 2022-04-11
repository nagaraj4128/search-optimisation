from operator import imod


import json
file = open("/home/sumit/Desktop/project/Id_Mapped_Data.json")

productid_mapped_data = json.load(file)

feature_to_id = {}
id_to_productList = {}

id =0
for i, j in productid_mapped_data.items():
    feature_to_id[i] = id 
    id_to_productList[id] = [j,0]
    id+=1
    

out_file = open("feature_to_id"+".json", "w")
json.dump(feature_to_id, out_file, indent=4, sort_keys=True)
out_file.close()


out_file = open("id_to_productList"+".json", "w")
json.dump(id_to_productList, out_file, indent=4, sort_keys=True)
out_file.close()