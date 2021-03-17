# Test JSON
# ==== Libraries
import json
from urllib.request import urlopen


json_data = '''
{
    "sheet": [
        {
            "id": 1,
            "name": "test",
            "email": "potatoman@kedi.com"
        },
        {
            "id": 2,
            "name": "test2",
            "email": "test2@mail.com"
        }
    ]
}
'''


# data = json.loads(json_data)

# print(type(data))
# print(data)

# # :: example read
# for user in data['sheet']:
#     print(user['name'])

# # :: example del / write
# for user in data['sheet']:
#     del user['id']

# new_string = json.dumps(data, indent=2)

# print(new_string)


with urlopen("https://developer.deutschebahn.com/store/api-docs/DBOpenData/Fahrplan-Free/v1") as response:
    source = response.read()

data = json.loads(source)

print(json.dumps(data, indent=2))


# :: Write to file
with open('test.json', 'w') as f:
    json.dump(data, f, indent=2)
