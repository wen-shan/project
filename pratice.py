# mathscore = [60, 70, 10, 20, 81, 63, 4]
# print(mathscore[2])
# print(mathscore[:5])
# mathscore.append(25)
# print(mathscore)
# mathscore.insert(3,20)
# print(mathscore)
# mathscore.remove(20)
# del mathscore[-1]
# print(mathscore)
# grades = [[5, 14, 7], [23, 36, 28], [88, 80, 92]]
# print(grades[2])
# ave_c = sum(grades[0])/len(grades[0])
# print(ave_c)
# ave_e = sum(grades[1])/len(grades[1])
# print(ave_e)
# ave_m = sum(grades[2])/len(grades[2])
# print(ave_m)
# grades.append([94, 90, 96])
# print(grades)
# grades[0][1] = 20
# print(grades)
# gradesturple = ((5, 14, 7), (23, 36, 28), (88, 80, 92))
# print(gradesturple[2])
# ave_c = sum(gradesturple[0])/len(gradesturple[0])
# print(ave_c)
# ave_e = sum(gradesturple[1])/len(gradesturple[1])
# print(ave_e)
# ave_m = sum(gradesturple[2])/len(gradesturple[2])
# print(ave_m)
# gradesdict = {
#     'chinese':[5, 14, 7],
#     'english':[23, 36, 28],
#     'math':[88, 80, 92]
# }
# print(gradesdict.get('math'))
# ave_c = sum(gradesdict.get('chinese'))/len(gradesdict.get('chinese'))
# print(ave_c)
# ave_e = sum(gradesdict.get('english'))/len(gradesdict.get('english'))
# print(ave_e)
# ave_m = sum(gradesdict.get('math'))/len(gradesdict.get('math'))
# print(ave_m)
# gradesdict['science'] = [94, 90, 96]
# print(gradesdict)
# allstudent = {
#     'John',
#     'Eva',
#     'Jill',
#     'Eric',
#     'Andy',
#     'Albert',
#     'Polina',
#     'Kristin',
#     'Angela'
# }
# dancrclub = {
#     'Andy',
#     'Eric',
#     'Albert',
#     'Polina',
#     'Kristin'
# }
# guitarclub = {
#     'John',
#     'Eva',
#     'Jill',
#     'Eric',
#     'Andy'
# }
# print(dancrclub & guitarclub)
# print(guitarclub - dancrclub)
# both = guitarclub | dancrclub
# print(allstudent-both)
# r = 4
# # pi = 3.14
# # area = (r**2*pi)
# # print(area)
# # ls = [10, 30, 40, 90, 100, 61]
# # ave = sum(ls)/len(ls)
# # print(ave)
# # print(round(ave))
# print('first line. \nsecond line. \nthird line.')
# print('Hello', end = '')
# print('world!', end = '')
# print('Hello', 'world', '!')

# x = 42
# value = f'value of x is {x}'
# print(value)
# value ='value of x is {x}'
# print(value)
# import math
# mathscore = [60, 70, 10, 20, 81, 63, 4]
# len_mathscore = len(mathscore)
# for i in range (len_mathscore):
#     print(i, mathscore[i])
# for item in mathscore:
#     print(item)
# for item in mathscore:
#     print(math.sqrt(item)*10)
# for a in range (0,10):
#     print(a)
# for item in mathscore:
#     print(math.sqrt(item)*10)
# [print(math.sqrt(item)*10) for item in mathscore]
# for score in mathscore:
#     if score >80:
#         continue
#     print(score)
# for i in range (1, 10):
#     for j in range (1,10):
#         print(f'{i}*{j}={i*j}')
# count = 0
# while count < 51:
#     print('hello')
#     count +=1
# else:
#     print('end')
# num = eval(input('enter numbers:'))
# for i in range (1, num+1):
#     if i % 2 ==1:
#         print(i)
# import random
# ls = []
# row = eval(input('how many rows:'))
# column = eval(input('how many columns:'))
# for i in range(row):
#     ls.append([])
#     for j in range(column):
#         num = random.randint(1, 100)
#         ls[i].append(num)
# for x in range(row):
#     for y in range(column):
#         print(f'{ls[x][y]} ' , end='')

flag = True
balance = 0
drinks = [
    {"name":"可樂", "price": 20},
    {"name":"雪碧", "price": 20},
    {"name":"茶裏王", "price": 25},
    {"name":"原萃", "price": 25},
    {"name":"純粹喝", "price": 30},
    {"name":"水", "price": 20}
]
while flag:
    print('\n===========================')
    select = eval(input("1. 儲值\n2. 購買\n3. 查詢餘額\n4. 離開\n請選擇:"))
    if select ==1:
        value = eval(input('儲值金額'))
        while value < 1:
            print('====輸入金額需大於零====')
            value = eval(input("儲值金額:"))
        balance += value
        print(f'儲值後金額為{balance}元')
    elif select ==2:
        print("請選擇商品")
        for i in range(len(drinks)):
            print(f'{i+1}, {drinks[i]["name"]} {drinks[i]["price"]}元')
        choose = eval(input('請選擇編號'))
        while choose < 1 or choose > 6:
            print("請輸入1-6之間")
            choose = eval(input("請選擇:"))
        buy_drink = drinks[choose - 1]
        if balance < buy_drink['price']:
            print('====餘額不足====')
        else:
            print(f'以購買{buy_drink["name"]} {buy_drink["price"]}元')
            balance -= buy_drink['price']
            print(f'購買後餘額 {balance}元')

    elif select ==3:
        print(f'目前餘額為{balance}元')
    elif select ==4:
        print('bye')
        flag = 0
        break
    else:
        print('====請輸入1-4之間====')
        continue

