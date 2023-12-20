emp={
     'id':101,
     'name':'Hishok',
     'sal':750000,
     'loc':['Marathahalli','bangalore']
    }

#Read operations
print(emp['loc'][1])
print(emp.get('loc')[1])

#Update operation

emp['email']  = "hishok@gmail.com"

print(emp)