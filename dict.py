d1={
    "name":"gopi",
    "age":21,
    "marks":[99,100,98],
    "working":False,
}
print(d1["name"],d1.get("age"))

# only keys
print([x for x in d1.keys()])

# only values
print([x for x in d1.values()])

#adding and updating the values

d1["name"]="Loka"
d1.update({"age":30})

print(d1)

# delete
# d1.pop("name")
# d1.popitem()

# del d1["marks"]
# d1.clear()
# print(d1)

#Loop dictionaries
for k,v in d1.items():
    print(k,v)