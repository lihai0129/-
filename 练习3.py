name=['a1','b2','d3','x4','f5']
print(name)
name.sort()  # 按字母顺序排序 字母由a-z排序
print(name)
name.sort(reverse=True)  # 按字母顺序排序 字母由z-a排序
print(name)

name_noe=['a2','z9','c54','d2']
print(name_noe)
print(sorted(name_noe))  # 按字母排序 但是临时排序 后面可以恢复过来
print(name_noe)
name_noe.reverse()  # 反转列表元素的排列顺序
print(name_noe)
print(len(name_noe))  # 确定列表的长度 列表内有多少元素 就输出多少

# 习题总结
didian=['gangzhou1','beijing','shanghai','changsha','shanxi']
print(didian)
print(sorted(didian))  # 临时正向排序  变换位置 后面可以修改回来
print(sorted(didian , reverse=True))  #临时反向排序 后面可以修改回来
print(didian)
didian.reverse()  # 将列表中的元素位置倒叙过来
print(didian)
didian.reverse()  # 将列表中的元素倒叙过来
print(didian)
didian.sort()  # 将列表中的元素 安照字母排序 不可更改
print(didian)
didian.sort(reverse=True)  # 将列表中的元素按照字母顺序排序  后倒叙过来
print(didian)

magicians=['allice','david','carolina','bacive']
for magician in magicians:
    print(magician)
    print(f"{magician}'s name is good  is wording")

    

