# marks = int(input("enter your marks: "))
# if marks>= 40 and marks<60:
#     print("you get D grade")
# elif marks>=60 and marks<80: 
#     print("you get c grade")
# elif marks>=80 and marks<90: 
#     print("you get b grade")
# else: 
#     print("you get c grade")

# print(marks)

# a = 1
# b = 11 
# c = 59
# if a>b and a>c:
#     print("a is greater")
# elif b>a and b>c:
#     print("b is greater")
# else:

# atm if-else
amount = int(input("Add amount: ")) 
if amount >= 100:
    if amount >= 500:
        notes = amount // 500
        print('total no of 500rs notes are = ', notes)
        amount = amount % 500
    if amount >= 200:
        notes = amount // 200
        print('total no of 200rs notes are = ', notes)
        amount = amount % 200
    if amount >= 100:
        notes = amount // 100
        print('total no of 100rs notes are = ', notes)
else:
    print("Please add values in multiples of 100's")

