from collections import defaultdict

#---------------- C = create an empty dictionary
empty = defaultdict(list)
print("Empty dictionary: {}".format(empty))

#---------------- U = add new entry into dict
names = ['Alexys', 'Jacobi', 'Asunte','Natalie','Joann']
ages = [24, 18, 20, 80, 74]

#zip above two list together
d_zip = zip(names, ages)

#convert above to a default dict
d = defaultdict(int, d_zip)

print("\nDictionary after adding new entries: {}".format(d))

#---------------- U = updated an existing entry into dict
key = "Natalie"
d[key] = 42

print("\nDictionary after update {}'s age: {}".format(key, d))

#print where or not a key exists in dictionary or not
for name in ['Bernard', 'Natalie']:
    if name in d.keys():
        print("\nName [{}] exists as a key".format(name))
    else:
        print("\nName [{}] does not exists as a key".format(name))
        #add key to dictionary
        d[name]

print("\nDictionary after adding new entries: {}".format(d))

#---------------- R = access key value pair 
#print all keys
print("\nKeys:", end =" ")
for k in d.keys():
    print(k, end=", ")
print("\n")

#print all values
print("\nValues:", end =" ")
for v in d.values():
    print(v, end=", ")
print("\n")

#print all key-value pairs
print("\nKey-Value Pairs:")
for k,v in d.items():
    print("{}: {}".format(k,v))

#update value of key and access
d['Bernard'] = 41
print("\nToday's Bernard birthday! He is now {} years old.".format(d['Bernard']))

#---------------- D = delete a key-value pair from the dictionary

#option 1: pop (returns key's value)
removed = d.pop("Asunte")

print("\n{} was removed from dictionary: {}".format(removed, d))

#option 2: del (removes key from dictionary)
del d["Bernard"]
print("\nDictionary after [del]: {}".format(d))
