#basic dictionary
thisdict = {"brand" : "Ford",
            "model" : "Mustang",
            "year": 1964
            }
print(thisdict["brand"])

#retreive number of items in dictionary
print(len(thisdict))

#Add multiple values to a key
del thisdict
thisdict = {"brand" : "Ford",
            "electric": False,
            "year": 1964,
            "colors": ["red","white","blue"]
            }
print(thisdict["colors"])

prices_lookup = {'apple':2.99,'oranges':1.99,'pears':4.99}
prices_lookup["apple"]

#Dictionary inside a dictionary
d = {'k1':123,'k2':[0,1,2],'k3':{'insidekey':100}}
d["k2"]
d["k3"]['insidekey']

#Retreive item inside key and change it
d["k2"][2] = 'TWO'
print(d)

b = {'key1':['a','b','c']}
mylist = b["key1"]
letter = mylist[2]
letter.upper()

#Save change
b["key1"][1] = b["key1"][1].upper()

#Add value to dictionary
b['key2'] = 100

#Add Value to values in dictionary
b["key1"] += "100"

#Add Value to list of values
b["key1"].extend(['d','e'])

#Delete Value in Value
del b["key1"][3]

b.keys()
b.values()
b.items()
