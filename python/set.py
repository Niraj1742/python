# creating set
name={"sai","mai","tina"}
# print(name)
# print(len(name))
# print(type(name))
# for printing the hole set we have to do loop
'''
for x in name:
    print(x)
'''
# checking if the item is present in list
# if "sai" in name:
#     print("sai is in the print")

# add element in set
"""
name.add("riya")
print(name)
"""

# add other sequence in the set from list ,tuple
"""
name_list=["riya","kia"]
name.update(name_list)
print(name)


name.remove("sai")
print(name)
# if the name not present in set for removing
# name.remove("nir")
name.discard("nir") # this function will not throw a error if value is not present

print(name)
"""

# joining to set
s1={"a","b","c","d"}
s2={"m","l","k","j"}
# print(s1,s2)
"""# pro max joining
s3=s1.union(s2)
print(s3)
"""
# simple joining
"""
s1.update(s2)
print(s1)
"""
# keep only duplicate value while joining
# if one word persent in other word like ``a``
# s1.intersection_update(s2)

#keep all value same without showing duplicate
# s1.symmetric_difference_update(s2)