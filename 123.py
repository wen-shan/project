# x = 10
# print(x)
# def add(a, b):
#     return a + b
# x = 1
# y = 4
#
# result = add(x, y)
# print(result)

# mathScores = [60 , 70 , 10, 20 , 81, 63 ,4]
# print(mathScores[2])
# print(mathScores[1:6])
# print(mathScores[-1])
# print(mathScores[5:])
# print(sum(mathScores))
# print(max(mathScores))
# print(min(mathScores))
# print(sum(mathScores)/len(mathScores))
# mathScores2 = []
# mathScores2.append(60)
# print(mathScores2)
# mathScores2.append(70)
# mathScores2.append(50)
# mathScores2.append(40)
# mathScores2.insert(2 , 30)
# print(mathScores2)
# mathScores2[1] = 55
# print(mathScores2)
# mathScores2.append(70)
# mathScores2.append(40)
# print(mathScores2)
# print(mathScores2.count(40))
# print(mathScores2.index(40))
# print(sorted(mathScores2, reverse = True))
# ls = [[1, 2, 3], [4, 5, 6]]
# print(ls[0][2])

# grades = [[5, 14, 7],[23, 36, 28],[88, 80, 92]]
# print(grades[2])
# print(sum(grades[0])/len(grades[0]))
# print(sum(grades[1])/len(grades[1]))
# print(sum(grades[2])/len(grades[2]))
# grades.append([94, 90, 96])
# print(grades)
# grades[0][1] = 20
# print(grades)

# tuple1 = (1, 2, 3, 4, 5,)
# print(tuple1[2])
# print(tuple1.index(4))
# print(tuple1.count(4))

# gradestuple = ((5, 14, 7),(23, 36, 28),(88, 80, 92))
# print(gradestuple[2])
# print(sum(gradestuple[0])/len(gradestuple[0]))
# print(sum(gradestuple[1])/len(gradestuple[1]))
# print(sum(gradestuple[2])/len(gradestuple[2]))

# family = {
#     'dad':'Hamor',
#     'mom':'Marge',
#     'son':'Bart',
#     'dauguter':'Lisa'
# }
# print('dad' in family)
# print(family.get('dad'))
# family.update({
#     'uncle':'Martin',
#     'aunt':'May'
# })
# print(family)

# gradeDict = {
#     'chinese':[5, 14, 7],
#     'english':[23, 36, 28],
#     'math':[88, 80, 92]
# }
# print(gradeDict.get('math'))
# print(sum(gradeDict.get('chinese'))/len(gradeDict.get('chinese')))
# print(sum(gradeDict['english'])/len(gradeDict['english']))
# print(sum(gradeDict['math'])/len(gradeDict['math']))
# gradeDict.update({'science':[94, 90, 96]})
# print(gradeDict)

# allstudent ={'John','Eva','Jill','Eric','Andy','Albert','Polina','Kristin','Angela'}
# danceclub = {'Andy','Eric','Albert','Polina','Kristin'}
# guiterclub = {'John','Eva','Jill','Eric','Andy'}
# print(danceclub & guiterclub)
# print(guiterclub-danceclub)
# both = guiterclub|danceclub
# print(allstudent-both)

# x = 4**0.5
# print(x)
# import math
# x = math.sqrt(4)
# print(x)

# r = 3
#pi = 3.14
# circle = r**2*pi
# print(circle)
# score = [10, 30, 40, 90, 100, 61]
# avg = (sum(x)/len(x))
# print(avg)
# avg = round(avg)
# print(avg)

# score = 58
# if score >= 60:
#     print("及格了")
# elif 55 <= score < 60:
# #elif 55 <= score and score < 60
#     print("教授拜託調個分")
# elif 50 <=score < 55:
#     print("可惡差點")
# else:
#     print("被當了")

# score = 90
# if score >= 60:
#     print("及格了")
#     if score >= 90:
#         print("你最棒")
#     else:
#         print("還好還好")

# print("Hello","world","!")
# print("Hello\nworld\n!")
# print("123", end=" ")
# print("456")

# x = 42
# print(f"Value of x is {x}")
# print("Value of x is x")

# mathscores = [60, 70, 10, 20, 81, 63, 4]
# print(mathscores[0])
# firstItem = "first item in mathscores is mathscores[0]"
# print(firstItem)
# firstItem = f"first item in mathscores is {mathscores[0]}"
# print(firstItem)

# for i in range(0, 10, 2):
#     print(i)
# mathscores = [60, 70, 10, 20, 81, 63, 4]
# for i in range(len(mathscores)):
#     print(i, mathscores[i])
# mathscores = [60, 70, 10, 20, 81, 63, 4]
# for i in mathscores:
#     print(i)

# family = {
#     'dad':'Hamor',
#     'mom':'Marge',
#     'son':'Bart',
#     'dauguter':'Lisa'
# }
# for member in family.items():
#     print(member)
# for key, value in family.items():
#     print(f"my {key} is {value}")

# mathscores = [60, 70, 10, 20, 81, 63, 4]
# for i in range(len(mathscores)):
# #for score in mathscores:
#     # print(math.sqrt(score)*10)
#     print(i, mathscores[i]**0.5*10)

# for i in range(10):
#     print(i)
# [print(i) for i in range(10)]

# import math
# mathscores = [60, 70, 10, 20, 81, 63, 4]
# [print(math.sqrt(x)*10) for x in mathscores]

# count = 0
# while count < 10:
#     print(count)
#     count +=1
# else:
#     print("loop end")

# mathscores = [60, 70, 10, 20, 81, 63, 4]
# for score in mathscores:
#     if score > 80:
#         break
#     print(score)
# mathscores = [60, 70, 10, 20, 81, 63, 4]
# for score in mathscores:
#     if score > 80:
#         continue
#     print(score)

# import random
# i = random.randint(1,50)
# print(i)
# x = eval(input("How many rows:"))
# print(type(x))

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f'{i}*{j} = {i*j}')
#     print()
#
# count = 0
# while count < 51:
#     print("Hello", end=" ")
#     count +=1
# else:
#     print("我說完了啦")
# num = eval(input("enter a number:"))
# for i in range(1, num+1):
#     if i % 2 == 1:
#         print(i)

# import random
# ls = []
# rows = eval(input("How many rows:"))
# columns = eval(input("How many columns:"))
# for i in range(rows):
#     ls.append([])
#     for j in range(columns):
#         num = random.randint(1,100)
#         ls[i].append(num)
# for row in ls:
#     for value
# import vending_machine.vending_service as machine
flag = True#控制迴圈是否繼續執行
while flag:
    print("\n========================")
    select = eval(input("1. 儲值\n2. 購買\n3. 查詢餘額\n4. 離開\n請選擇:"))

    if select ==1:#儲值
        # value = eval(input("儲值金額:"))
        # while value < 1:
        #     print("===儲值金額需大於零===")
        #     value = eval(input("儲值金額:"))
        # balance += value
        # print(f'儲值後金額為{balance}元')
        machine.deposit()
    elif select ==2:#購買
        machine.buy()
        # print("請選擇商品")
        # for i in range(len(drinks)):
        #     print(f'{i+1}, {drinks[i]["name"]} {drinks[i]["price"]}元')
        #
        # choose = eval(input('請選擇編號'))
        # while choose < 1 or choose > 6:
        #     print("請輸入1-6之間")
        #     choose = eval(input("請選擇:"))
        #
        # buy_drink = drinks[choose-1]
        # if balance < buy_drink['price']:
        #     print('====餘額不足====')
        # else:
        #     balance -= buy_drink['price']
        #     print(f'以購買{buy_drink["name"]} {buy_drink["price"]}元')
        #     print(f'購買後餘額 {balance}元')
        # for item in drinks:
        #     print(f'{item["name"]} {item["price"]}元')

    elif select ==3:#查詢餘額
        print(f"目前餘額為{balance}元")
    elif select ==4:#離開
        print("bye")
        flag = False
        break
    else:
        print("====請輸入1-4之間=====")
        continue

# weight = 100
# weight1 = 80
#
# def add_weight(w1, w2=1):
#     result = w1 + w2
#     result1 = w1 * w2
#     return result, result1
#
#
# x1, x2 = add_weight(weight, weight1)
# print(x1, x2)
#
# y1, y2 = add_weight(w2=weight, w1=weight1)
# print(y1, y2)

x = 10
y = 20
def calculate(num1 , num2):
    return num1 + num2
calculate(x,y)


