import simplejson as json
import os

if os.path.isfile("./age.json") and os.stat("./age.json").st_size !=0:
    old_file=open("./age.json","r+")
    data=json.loads(old_file.read())
    print("the current data is ", data["age"], "adding another year")
    data["age"]=data["age"]+1
    print("new year is", data["age"])

else:
    old_file=open("./age.json","w+")
    data={"name":"santosh","age":25}
    print("the default age is ", data["age"])

old_file.seek(0)
old_file.write(json.dumps(data))
