# import json
# my ='{"name" : "Lil", "age" :  "33"}'
# y = json.loads(my)
# print(y["age"])


# import json 
# x ='{ "name" : "saw", "city" : "almata"}'
# y = json.loads(x)
# print(y["city"])

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))