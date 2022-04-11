import json
from operator import imod

from sortedcontainers import SortedList

mm_feature_to_id ={} 
mm_id_to_productList ={} 

ms = SortedList()

k=5 #max size of sortedList

while(1):
    print()
    print("Enter search query: ",end=" ")
    search_query = input().strip()
    
    if search_query in mm_feature_to_id:

        id = mm_feature_to_id[search_query]
        frequecy = mm_id_to_productList[id][1]

        print(mm_id_to_productList[id][0]) #

        start = ms.bisect_left((frequecy,id))
        del ms[start:start+1]
        ms.add((frequecy+1, id))
        mm_id_to_productList[id][1]+=1

    else:
        #generate path
        directory_path="./Trie"
        for ch in search_query:
            directory_path+='/'
            directory_path+=str(ord(ch))
        directory_path+='/'
        directory_path+="file/file.json"
        with open(directory_path, "r") as jsonFile: #secondary memory
             prod_data = json.load(jsonFile)

        id=prod_data["id"]
        prod_data["data"][1]+=1 #increment in frequency
        ms.add((prod_data["data"][1], id))
        mm_id_to_productList[id] = [prod_data["data"][0],prod_data["data"][1], search_query]
        mm_feature_to_id[search_query] = id
    if len(ms)>k:
        start = ms.bisect_left((0,0))
        new_id = ms[start][1]
        new_feature = mm_id_to_productList[new_id][2]
        directory_path="./Trie"
        print(new_feature)
        for ch in new_feature:
            directory_path+='/'
            directory_path+=str(ord(ch))
        directory_path+='/'
        directory_path+="file/file.json"
        obj = {"id": new_id, "data": mm_id_to_productList[new_id][0:2] }
        with open(directory_path, "w") as outfile:
            json.dump(obj, outfile)
        mm_feature_to_id.pop(new_feature)
        mm_id_to_productList.pop(new_id)
        del ms[start:start+1]
    print()
    print(mm_feature_to_id)
    print(mm_id_to_productList)
    print(ms)