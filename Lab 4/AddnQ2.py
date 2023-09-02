import json

print("First lets make a JSON object!")
inputString = input("Enter the data of your JSON object: ")
jsonObj = json.loads(inputString)
print("The JSON object is:",jsonObj)
print(type(jsonObj))

print("Now lets convert JSON object to string!")
jsonString = json.dumps(jsonObj)
print("String is: ",jsonString)
print(type(jsonString))

