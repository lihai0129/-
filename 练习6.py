# if语句
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.lower())

# 多条件查询
car = 'subaru'
print("Is car=='subaru'? I predict True.")
print(car=='subaru')

print("\nIs car=='audi'? I predict False.")
print(car=='subaru')

age = 19
if age>=18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

age_1 = 17
if age_1>=18:
    print("You are old enough to")
    print("Have you registered to vote")
else:
    print("Sorry, you are old enough to vote")
    print("Plesse register your")