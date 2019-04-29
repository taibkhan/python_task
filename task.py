from pymongo import MongoClient
import pprint
try:
    #connecting with mongodb
    conn= MongoClient()
    print('connected successfuly')
except:
    print('could not connect to mongodb')
    
db= conn['employee-database']
employees= db.employees
#function to insert data in mongodb
def insert():
    a=input('enter the name: ')
    
    results= employees.count_documents({
        'name': a
    })
    if(results>0):
        raise Exception('username already exist')
    b=input('enter the address: ')
    employee= {
            'name': a,
            'address' : b
        }
    result= employees.insert_one(employee)
    if result.acknowledged:
        print('user added successfuly')

    print('database:')
    employess= employees.find()
    for emp in employess:
        pprint.pprint(emp)
# function to update data of a particular employee
def update():
    c=input('enter the name of the employee whose detail needs to be updated: ')
  #  b=input('enter the address: ')
    results= employees.count_documents({
        'name': c
    })
    if(results==0):
        raise Exception('username does not exist')
    a=input('enter the name: ')
    b=input('enter the address: ')
    result = employees.update_one( 
        {"name":c}, 
        { 
                "$set":{ 
                        "name":a,
                        "address":b
                        }
                  
                } 
        )  
   
   
    print('database:')
    employess= employees.find()
    for emp in employess:
        pprint.pprint(emp)

# function to delete a particular document from the data base
def delete():
    c=input('enter the name of the employee to be deleted: ')
    results= employees.count_documents({
        'name': c
    })
    if(results==0):
        raise Exception('username does not exist')
    result = employees.delete_one({"name":c}) 
    print('database:')
    employess= employees.find()
    for emp in employess:
        pprint.pprint(emp)

#choice for the users to select for appropriate functionality
print('enter 1 to insert data')
print('enter 2 to update data')
print('enter 3 to delete data')
print('enter 4 to exit')
a=input('enter your choice: ')
if(a=='1'):
    insert()
elif(a=='2'):
    update()
elif(a=='3'):
    delete()
elif(a=='4'):
    print('exited successfuly')
