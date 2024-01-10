#creating a dictionary
"""
phone ={
    "sai" :123456 ,
    "ayush" :2344333,
    "ritu" :432111 ,
}

print(phone)
#checking type of dictionary
print(type(phone))
#checking the length of dictionary
print(len(phone))
#assecc the key value
print(phone["sai"]) 
print(phone.get("ayush"))
print(phone.keys())

# update value of dictionary
phone["niraj"] =1234567890
print(phone["niraj"])
 
 #add element
phone["rahul"] =98765432
print(phone)

# add more dictionary
more_phone= {
    "kia" : 432123,
    "rahul" :654321,
    "jay" : 43123,
}
phone.update(more_phone)

# remove element in a dictionary
phone.pop("kia")
print(phone)
# phone.popitem() this will remove last add item
# phone.clear() this will empty the dictionary

# priting value from dict

for x in phone:
    print(phone[x])

# print key and value together we will us
for x in phone.items():
    print(x)
# print key and value need diffrently we will us
for x,y in phone.items():
    print(x,y)
"""
# nested dictionary
phone = {
    "Area1":{
        "a":1,
        "b":2,
        "c":3
    },
    "Area2":{
        "x":1,
        "y":2,
        "z":3
    }
}
print(phone)
# Particular element
print(phone["Area1"]["b"])
print(phone["Area2"]["y"])