#union() where duplicates are excluded,contain all items in both sides
#example1
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(y, z)

print(result)

#example2
x={'Bharath','Kannan','Harish','Aakash'}
y={'Hishok','Kannan','Hari','Bharath'}
enames = x.union(y)
print(enames)
