favor_language = " Python is good "
favor_longer = " mi too "
print(f"{favor_language.strip()}\n\t{favor_longer.strip()}")  # 删除两端的空白符 \t:加制表符 \n:换行
print(favor_language.lstrip())  # 删除左边的空白符
print(favor_language.rstrip())  # 删除右边的空白符

names=['lcy','twh','lcy','twh','lcy','thons']  # 列表
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[-3])
print(names[-2])
print(names[-1])
print(f"Holleh! {names[0]} I like you")

works=['would','like','honda','notorcycle']
print(f"I\t{works[0]}\t{works[1]}\tto\town\ta\t{works[-2].title()}\t{works[-1]}.")

motorcyckless=['honda','yamaha','suzuki']
print(motorcyckless)
motorcyckless[0]='hesdb' # 修改列表中的值
print(motorcyckless)

motorcyckless.append('datsor') # 用.append语句 在列表末尾追加值
print(motorcyckless)

motorcyckless.insert(1,'holleh!')  # 用.insert语句 在列表中插入元素
print(motorcyckless)

del motorcyckless[1]  # 用del语句 列表中删除元素 删除时要知道 列表值的位置
print(motorcyckless)

pyp_motorcyckless=motorcyckless.pop()  # 用pop语句 删除列表中最后一个元素  但也可以删除任何一个元素
print(motorcyckless)
fli_motorcyckless=motorcyckless.pop(1)
print(f"The first motorcyle Iowen {fli_motorcyckless}")  # 如果要从列表中删除一个元素，且不再以任何方式使用他 用del 如果删除后还要使用 就用pop

motoisto=['baicai','honglbo','xigua']
print(motoisto)
motoisto.remove('honglbo')  # 如果只知道元素值  可以用.remove python会根据值来删除元素 用.renove 删除的元素 后面还可以继续用
print(motoisto)

shenri=['小明','李华','张三','李四']
print(f"你好，希望你{shenri[0]}先生\n能来我的生日派对")
print(f"你好，希望你{shenri[1]}先生\n能来我的生日派对")
print(f"你好，希望你{shenri[2]}先生\n能来我的生日派对")
print(f"你好，希望你{shenri[3]}先生\n能来我的生日派对")

print("张三 不能来生日派对")
shenri[-2]='莉莉'
print(shenri)
print(f"你好，希望你{shenri[0]} {shenri[1]} {shenri[2]} {shenri[-1]}先生\n能来我的生日派对")
shenri.insert(3,'李明华')
shenri.insert(0,'小雨')
shenri.append('逍遥')
print(shenri)

shenri.pop(1)
shenri.pop(2)
shenri.pop(-1)
print(shenri)