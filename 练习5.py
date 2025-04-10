# 切片
pllayers = ['charles','martina','florence','ali']
print(pllayers[0:3])
print(pllayers[1:4])
print(pllayers[3:])
print(pllayers[:-2])
print(pllayers[::2])
for pllaye in pllayers[:3]:
    print(pllaye)

my_foods = ['pizza','falafel','carrot cake']
id_foods = my_foods[:]
my_foods.append('ice_cteam')
id_foods.append('cannoli')
print(my_foods)
print(id_foods)

print("The first three items in the list are:")
is_items=['The', 'first' ,'three', 'items', 'in ','the' ,'list' ,'are:']
print(is_items[0:3])
print(is_items[2:5])
print(is_items[-3:])

#元组
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
    print(f"holle,{dimension}")
dimensions=(400,50)
for dimension in dimensions:
    print(f"holle,{dimension}")

eat=('bannd','pinguo','lizi')
for eats in eat:
    print(eats)
eat=('bannd','pinguo','bailuobo','xihua')
for eats in eat:
    print(eats)