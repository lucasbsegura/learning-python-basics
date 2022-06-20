import json

json_string = '{"name":"lucas"}'
print(json.loads(json_string))

json_string2 = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string2)