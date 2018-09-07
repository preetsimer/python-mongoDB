import pymongo
client=pymongo.MongoClient()
database=client['Students']
collection=database['students1']
for i in range(0,10):
    name=input("Enter students name: ")
    marks=int(input("Enter marks: "))
    collection.insert_one({'Name':name, 'Marks':marks})
print("Data Entry successful")    
data=collection.find({'Marks':{'$gt':80}})
for document in data:
    print(document)
print("Program Executed!!!")
