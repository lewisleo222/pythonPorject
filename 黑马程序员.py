"""
# 钱包余额
monry=50
# 显示钱包中还有多少余额

print("钱包的余额:",monry)
# 花费10元
monry=monry-10
# 显示花费10元还剩多少余额
print("买了10元的冰淇淋之后还剩",monry,"元")
# 花费5元
monry=monry-5
# 买了可乐还剩多少余额
print("买了5元的可乐之后还剩",monry,"元")




"""
import sys

"""#查看对象类型信息
print(type("黑马程序员"))

print(type(666))
print(type(13.14))
#查看变量储存数据使用的类型
name = "黑马程序员"
print("name_type=type(name)")
# 转换x数据类型
num_str=str(11)
print("type(num_str)")
# 将数字类型转换为字符串
num_str =str(11)
print(type(num_str),num_str)
float_str=str(13.14)
print(type(float_str),float_str)
#将字符串转换为数字
num_str=int("11")
print(type(num_str),num_str)
num=float(13.14)
print(type(num),num)
# 不能将汉字字符串转换成数字类型（int) 必须要求转换内容必须是数字
num1=int("黑马程序员")
print(type(num1),num1)
"""

"""#整数转浮点数
float_int=float(11)
print(type(float_int),float_int)
#浮点数转换成整数
int_float=int(13.14)
print(type(int_float),int_float)"""

"""张三=str("法外狂徒")
print(张三)
# 规则1：只能使用下划线、中文、英文
# 规则2 大小写敏感
# 规则3 不能使用关键字
# 1.什么是标识符（变量、类、方法）
# 2.标识符的命名规则（中文、英文、下划线）
# 3.变量的命名规范？ 见名知意、下划线命名法 英文字母全小写"""

"""# 算术运算符
print("1+1=",1+1)
print("2*5=",2*5)
print("2-0=",2-0)
print("10/5=",10/5)
print("85%10=",85%10)
print("98//5=",98//5)
print("7**8=",7**8)
# 赋值运算符
number=1+2*36
# 符合赋值运算符
num=1
print("num=",num)
num+=1
print("num+=",num)
num-=1
print("num-=",num)
num*=8
print("num*=",num)
num/=8
print("num/=",num)
num%=9
print("num%=",num)
num//=7
print("num//=",num)

"""

"""print(name2)
# 在字符串内包含单引号包含双引号
print("'黑马程序员'")
# 双引号包含单引号、
print('"黑马程序员"')
# 使用反斜杠转义
print("\"")"""

"""#字符串字面量的拼接
name="123123"
print("我的mysql密码是："+name)
# 字符串无法和数字类型拼接
class_num=57
avg_slary=16798
message="计算机学院id为%s的学生,毕业月薪为%s"%(class_num,avg_slary)
print(message)
# 通过%s将数字和字符串进行拼接
class_num1=57
class_num2=8584
message1="计算机学院id为%s的学生，毕业月薪为%s"%(class_num1,class_num2)
print(message1)
name2="创智博客"
set_year=2006
stock_price=19.19
message2="%s创建于%d,现在的股价为：%f"%(name2,set_year,stock_price)
print(message2)"""

"""num1=11
num2=11.345
print("数字11宽度限制5，结果是：%5d"%num1)
print("数字11.345宽度限制7，小数精度2，结果是%7.2f"%num2)
print("数字11.345宽度限制7，小数精度2，结果是%.2f"%num2)"""

"""# 字符串格式化方法2 f"{}" (format) 格式化单词
name="法外狂徒张三"
position="b站知名律师"
print(f"我的名字是：{name},我的职位是：{position}")
"""
"""# 表达式的格式化
print("1*1的结果是：%d"%(1*1))
print("1*2的结果是：{1*2}")
print("字符串在python中的类型名为：%s"%type("字符串"))"""


"""# 练习
name="无锡百优品有限责任公司"
stock_price=float(88.8)

stock_code="ZSCDF878RT"
stock_price_daily_groth_factor=float(1.2)
growth_days=int(3)
num=stock_price*stock_price_daily_groth_factor**growth_days
print("公司：{},股票代码：{},当前股价：{:.2f}".format(name,stock_code,stock_price))
print("每日增长系数是：%.2f,经过%d天的增长后，股价达到了：%.2f"%(stock_price_daily_groth_factor,growth_days,num))
"""
"""# 数据输入
print("请告诉我你是谁？")
name=input()
print("我知道了，你是：%s"% name)
# 输入数字类型
num=input("请告诉我你的密码")
num=int(num)
print("你的银行卡类型是：",type(num))"""

"""# 小练习
user_name="张三"
user_type="尿不湿"
print("您好！%s,今天你的%s丢在了我的车上！"%(user_name,user_type))
"""

# 比较运算符
# ==(等于）
# !=(不等于）
# >(大于）
# <(小于）
# >=(大于等于）
# <=(小于等于）
# 定义变量存储布尔类型的数据
"""bool_1=True
bool_2=False
print(f"bool_1变量的内容是：{bool_1},类型是：{type(bool_1)}")
print(f"bool_2变量的内容是：{bool_2},类型是：{type(bool_2)}")
# 比较运算符的使用
# ==,!=,>,<,>=,<=
# 演示进行内容的相等比较
num1=10
num2=15
print(f"10==10的结果是：{num1==num2}")
print(f"10==10的结果是：{num1!=num2}")"""
# 定义变量
"""age=30

if age>=13:
    print("明天我就去表白")
    print("即将步入大学生活")
print("时间过得真快呀")"""



"""print(f"欢迎来到黑马儿童游乐园,儿童免费，成人收费")

age=input("请输入你的年龄：")

if age<=str(12):
    print("您是儿童，欢迎您免费来游玩本游乐园 有过山车喔！")
else:
    print("您已成年，游玩需补票10元。")
    print("祝您游玩愉快")"""

"""print("欢迎来到黑马动物园")
height=input("请输入您的身高：（cm)")
height=float(height)
if height>120:
    print("您的身高超出120cm,游玩需要购票10元。")
else:
    print("您的身高未超出120cm,可以免费游玩，")
print("祝您游玩愉快！")"""

"""# 多条件判断语句
print("欢迎来到黑马动物园。")
height=int(input("请输入你的身高(cm):"))
vip_level=int(input("请输入你的vip级别（1~5）:"))
if height<120:
    print("您的身高小于120cm,可以免费游玩。")
elif vip_level >3:
    print("您的vip级别大于3，可以免费游玩！")
else:
    print("不好意思，所有条件都不满足,需要购票10元。")
print("祝您游玩愉快!")"""

"""if int(input("请输入你的身高（cm):"))<120:
    print("身高小于120cm,可以免费。")
elif int(input("请输入你的vip等级（1-5）:")) >3:
    print("今天是1号免费日，可以免费")
else:
    print("不好意思，条件都不满足，需要买票10元")"""

"""num=int(123)
if input("请输入第一次猜想的数字:")==num: #条件1
    print("您猜对了！")
elif input("不对，再猜一次：")==num:    #条件2
    print("您猜对了！")
elif input("不对，再猜最后一次：")==num: #条件3
    print("您猜对了！")
else:                                 #所有条件不满足的情况下：
    print("Sorry,全部猜错啦，我想的是：123")"""

"""# 多语句嵌套条件语句
print("欢迎来到黑马动物园。")
if int(input("输入伱的身高："))>120:
    print("你的身高大于120cm，不可以免费")
    print("不过如果你的vip等级高于3，可以免费游玩")

    if int(input("请告诉您的vip级别："))>3:
        print("恭喜你，你的vip级别大于3，可以免费游玩。")
    else:
        print("Sorry,您需要补票，10元。")
else:
    print("欢迎您小朋友，可以免费游玩。")"""

"""age=20
year=3
level=1
if age>=18:
    print("你是成年人：")
    if age<30:
        print("你的年龄达标了")
        if year>2:
            print("恭喜您，年龄和级别达标，可以领取礼物。")
        elif level >3:
            print("恭喜您，年龄和级别达标，可以领取礼物。")
        else:
            print("不好意思，尽管年龄达标，但是入职时间和级别都不达标。")

    else:
        print("不好意思，年龄太大了。")

else:
    print("不好意思，小朋友不可以领取")"""

"""import random
num=random.randint(1,10)
guess=int(input("请输入你猜想的数字："))
if guess==num:
    print("恭喜您猜对了！")
    sys.exit(0)
else:
    if guess < num:
        print("您猜的数字小了")
    elif guess > num:
        print("您猜的数字大了")
guess1 = int(input("您输错了哦，请输入你猜想的数字："))
if guess1 == num:
        print("恭喜您猜对了!")
        sys.exit(0)
else:
    if guess1 < num:
      print("您猜的数字小了")
    elif guess1 > num:
      print("您猜的数字大了")
guess2 = int(input("不好意思，您还有最后一次机会哦！"))
if guess2 == num:
    print("恭喜您猜对了!")
    sys.exit(0)
else:
    if guess2 < num:
      print("您猜的数字小了")
    elif guess2 > num:
      print("您猜的数字大了")
    else:
        print("非常遗憾，这三次机会都没有猜对！")
"""






""" if guess1==num:
        print("恭喜您猜对了！")
    elif guess1<num:
        print("您猜的数字小了！")
    elif guess1>num:
        print("您猜的数字大了！")
    else:
        print("不好意思，非常遗憾地通知你还有最后一次机会！")
        if guess2==num:
            print("恭喜您猜对了！")
            if guess2 < num:
                print("你猜的数字小了！")
            elif guess2 > num:
                print("你猜的数字大了!")
        else:
            print("")"""

# 循环语句

"""i=0
while i<100:
    print("小美，我喜欢你")
    i+=1"""
"""# 方法一
print(sum(list(range(1,101))))
# 方法二
sum2=0

for i in range(1,101):

sum2+=i

print(sum2)
# 方法三
def fsum1(n):

i=0 #初始化变量

s=0

while i<n+1: #条件判断

s+=i #循环体

i+=1 #改变变量

print(s)

fsum1(100)
# 方法四
def fsum2(n):

if n==1:

return 1

else:

return n+fsum2(n-1)

print(fsum2(100))
"""

"""# 求1-100的和
sum = 0
i = 1
while i<=100:
    sum += i
    i += 1
print(f"1-100的累计和是：{sum}")"""

"""# 获取范围内在1-100的随机数字
import random
num=random.randint(1,100)
# 定义一个变量，记录总共猜测了多少次
count=0
#  通过一个布尔类型的变量，做循环是否继续的标记
flag =True
while flag:
    guess_num=int(input("请输入你猜测数字："))
    count += 1
    if guess_num ==num:
        print("猜中了")
        # 设置为False就是终止循环的条件
        flag=False
    else:
        if guess_num > num:
            print("你猜的大了")
        else:
            print("你猜的小了")
print(f"你总共猜测了{count}次")
"""
# 演示while循环的嵌套使用
# 外层：表白100的控制
# 内层：每天的表白都送10只玫瑰花的控制

"""i=1
while i<100:
    print(f"今天是第{i}天,准备表白......")

    # 内层循环的控制变量
    j=1
    while j<=10:
        print(f"送给小美第{j}只玫瑰花")
        j+=1

    print("小美，我喜欢你")
    i += 1

print(f"坚持到第{i}天，表白成功")"""

"""# 定义外层循环的控制变量
i=1
while i<=9:
    # 定义内层循环的控制变量
    j=1
    while j<=i:
        # 内层循环的print语句
        print(f"{j}*{i}={j*i}\t",end='')
        j+=1
    i +=1
    print() # print 空内容,就是输出一个换行"""

"""name="itheima"
for x in name: # 将name的内容，挨个取出
    print(x)"""



"""import re

str_ = "23sD2ffe12e"
# [a-zA-Z]是匹配内容，str_是待匹配的对象
str_ = re.findall('[a-zA-Z]',str_)
print(len(str_))"""

"""name="itheima is a brand of itcast"

for a in name:
    len=name.count('a')
    print(f"itheima is a brand of itcast中共含有：{len}个字母a")"""

"""name="itheima is a brand of itcast"
count=0
for a in name:
    if a=='a':
        count+=1
    else:
        count+=0
    print(f"itheima is a brand of itcast中共含有：{count}个字母a")"""

"""# range语法1 range(num)
for x in range(10):
    print(x)
# range 语法2 range(num1,num2)"""

"""for x in range(5,10):
    # 从5开始，到10结束，不包含10本身的数字序列
    print(x)

# 语法3 range(num1,num2,step)
for x in range(5,10,2):
    # 从5开始，到10结束（不包含10本身）的一个数字序列，数字之间的间隔为2
    print(x)"""

"""# 定义一个数字变量num,内容随意并使用range()语句，获取从1到num的序列，使用for循环遍历它。在遍历的过程中，统计有多少偶数出现
num="187448948854"
count=0
for x in range(1,100):
    if x%2==0:
        count+=1
    else:
        count+=0
    print(f"1到100（不含100本身）范围内，有{count}个偶数")"""

"""# 限定
i=0
for i in range(5):
    print(i)

print(i)"""

"""# for循环嵌套语句
i=0
for i in range(1,101):
    print(f"今天是向小美表白的第{i}天，坚持。")
    for j in range(1,11):
        print(f"送给小美的第{j}朵玫瑰花")
    print(f"小美，我喜欢你(第{i}天的表白结束)")
print(f"第{i}天，表白成功")"""

# # 定义外层循环的控制变量
# i=1
# while i<=9:
#     # 定义内层循环的控制变量
#     j=1
#     while j<=i:
#         # 内层循环的print语句
#         print(f"{j}*{i}={j*i}\t",end='')
#         j+=1
#     i +=1
#     print() # print 空内容,就是输出一个换行

"""# for循环打印九九乘法表
i=0
for i in range(1,10):
    j=1
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}\t",end='')
        j+=1
    i +=1
    print()"""

# # 演示循环中断语句 continue
# for i in range(1,6):
#     print("语句1")
#     continue #本次循环结束
#     print("语句2")

# # 演示continue的嵌套应用
# for i in range(1,6):
#     print("语句1")
#     for j in range(1,6):
#         print("语句2")
#         continue
#         print("语句3")
#
#     print("语句4")
# # 演示break用法
# for i in range(1,6):
#     print("语句1")
#     for j in range(1,6):
#         print("语句2")
#         break
#         print("语句3")
#
#     print("语句4")
# 自己做的公司发工资练习，有瑕疵

# i=0
#
# remaining_sum=10000
# for i in range(1,21):
#     # print(f"员工{i},绩效分{num}",end='')
#         import random
#         num=random.randint(1,10)
#         if num<5:
#           print(f"员工{i},绩效分{num},低于5，不发工资，下一位。")
#           continue
#
#         if num >5:
#             remaining_sum -= 1000
#             print(f"向员工{i}发放工资1000元，账户余额还剩余{remaining_sum}")
#             if remaining_sum == 0:
#              break

"""# 定义账户余额变量
money=10000
# for循环对员工发放工资
for i in range(1,21):
    import random
    num=random.randint(1,10)
    if num <5 :
        print(f"员工{i}绩效分{num}，不满足，不发工资，下一位")
        # continue跳过发放
        continue
    # 要判断余额不足
    if money>=1000:
        money-=1000
        print(f"员工{i},满足条件发放工资1000,公司账户余额:{money}")
    else:
        print(f"余额不足，当前余额：{money}元，不足以发工资，不发了，下个月再来")
        break"""

# balance = 4213
# annualInterestRate = 0.2
# monthlyPaymentRate =0.04
# monthInterestRate = annualInterestRate / 12
# monthlyPayment = (monthlyPaymentRate*balance)
# newBalance= (balance-monthlyPayment) * (1 + monthInterestRate)
# month = 0
# while month < 12:
#     month += 1
#     newBalance=(balance-monthlyPayment)*(1 + monthInterestRate)
#     balance = newBalance
#     monthlyPayment = (monthlyPaymentRate*newBalance)
#
#     print ("Month: " + str(month))
#     print ("Minimum monthly payment: " + str(round(monthlyPayment,2)))
#     print ("Remaining balance: " + str(round(newBalance, 2)))

# 需求，统计字符串的长度，不使用内置函数len()
# str1="itheima"
# str2="itcast"
# str3="python"
# # 定义一个计数的变量
# count=0
# for i in str1:
#     count+=1
# print(f"字符串{str1}的长度是：{count}")
#
# count=0
# for i in str2:
#     count+=1
# print(f"字符串{str2}的长度是：{count}")
#
# count=0
# for i in str3:
#     count+=1
# print(f"字符串{str3}的长度是：{count}")
#
# # 可以使用函数，来优化这个过程
# def my_len(data):
#     count=0
#     for i in data:
#         count+=1
#     print(f"字符串{data}的长度是{count}")
# my_len(str1)

# # 函数的定义：
# def 函数名(传入参数):
#     函数体
#     return 返回值

# # 定义一个函数，输出相关信息
# def say_hi():
#     print("Hi 我是牛马程序员,学python来牛马")
#
# say_hi()

# def check_nucleic_acid():
#     print("欢迎来到牛马程序员！")
#     print("请出示您的健康码以及72小时核酸证明！")
# check_nucleic_acid()

# 定义2数相加函数，通过参数接收被计算的2个数字
# def add(x,y):
#
#     result=x+y
#     # 打印结果
#     print(f"{x}+{y}的结果是：{result}")
# # 传入实参，进行函数调用
# add(4,5)

# 定义一个查验温度的函数
# def temperature(a):
#     # 变量a转换为数字类型
#     a=float(a)
#     # 判断体温是否异常
#     if a <=37.5:
#         print(f"欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明,并配合测量体温!体温测量中，您的体温是：{a}度，体温正常请进！")
#     else:
#         print(f"欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！体温测量中，您的体温是：{a},需要隔离！")
# # 调用函数temperature()
# temperature(38.7)

# # 定义一个函数，完成2数相加功能
# def add(a,b):
#     result=a+b
#     # 通过返回值，将相加的结果返回给调用者
#     return result
# # 函数的返回值，可以通过变量去接收
# r=add(2,6)
# print(r)

# 无return语句的函数返回值
# def say_hi1():
#     print("你好呀")
# result=say_hi1()
# print(f"无返回值函数，返回的内容是：{result}")
# print(f"无返回值函数，返回的内容类型是：{type(result)}")
#
# # 主动返回None的函数
# def say_hi2():
#     print("你好呀")
#     return None
#
# result=say_hi2()
# print(f"无返回值函数，返回的内容是：{result}")
# print(f"无返回值函数，返回的内容类型是：{type(result)}")
#
# result=say_hi2()
# print(f"无返回值类型，返回的内容是：{result}")
# print(f"无返回值函数，返回的内容类型是：{type(result)}")

# none用于if判断
# def check_age(age):
#     if age>18:
#         return "success"
#     else:
#         return None
# result =check_age(16)
# if not result:
#     #进入if表示result是None值，也就是False
#     print("未成年，不可以进入")
# # None用于声明无初始内容的变量
# name=None

# 定义函数，进行文档说明
# def add(x,y):
#     """
#     add函数可以接收2个参数，进行2数相加的功能
#     :param x:其中一个参数x，输入值即可
#     :param y:其中一个参数y，输入值即可
#     :return:返回add（)函数的结果
#     """
#     result=x+y
#     print(f"2数相加的结果是：{result}")
#     return result
# add(5,6)

# 定义函数func_b
# def func_b():
#     print("------2------")
# # 定义函数func_a,并在内部调用func_b
# def func_a():
#     print("-----1------")
#     # 嵌套调用func_b
#     func_b()
#     print("-----3------")
# # 调用函数func_a
# result=func_a()
# print(result)

# # 演示局部变量
# def test_a():
#     num=100
#     print(num)
#
# test_a()
# # 出了函数体，局部变量就无法使用了
# print(num)

# 演示全局变量
# num=200
# def test_a():
#     print(f"test_a:{num}")
# def test_b():
#     print(f"test_b:{num}")
# test_a()
# test_b()
# print(num)

# 在函数内修改全局变量
# num=200
# def test_a():
#     print(f"test_a:{num}")
# def test_b():
#     global num
#     num=500 # 局部变量
#     print(f"test_b:{num}")
#
# test_a()
# test_b()
# print(num)

# 定义银行卡余额变量
# money=5000000
# # 定义客户姓名变量
# name=input("请输入您的姓名：")
# # 定义查询余额函数
# def research(show_header):
#     if show_header:
#       print("------查询余额------")
#     print(f"{name},您的银行卡余额为：{money}")
# # 定义存款函数
# def deposit(num):
#     global money
#     money+=num
#     print("------存款------")
#
#     print(f"{name}.您的存款金额为：{num}")
#     # 调用reasearch()函数查询余额
#     research(False)
# # 定义取款金额函数为withdraw()
# def withdraw(num):
#     global money
#     money-=num
#     print("------取款------")
#
#     print(f"{name},您的取款金额为：{num}元成功。")
#     # 调用reasearch()函数查询余额
#     research(False)
#
# # 定义主菜单函数
# def main():
#     print("-------主菜单---------")
#     print(f"{name},您好，欢迎来到黑马银行ATM，请选择操作:")
#     print("查询余额\t[输入1]")
#     print("存款\t\t[输入2]")
#     print("取款\t\t[输入3]")
#     print("退出\t\t[输入4]")
#     return input("请输入您的选择：")
#
# # 设置无线循环，确保程序不退出
# while True:
#     keyword_input=main()
#     if keyword_input=="1":
#         research(True)
#         continue #通过continue继续下一次循环,一进来就是回到了主菜单
#     elif keyword_input=="2":
#         num=int(input("您想要存多少钱？请输入："))
#         deposit(num)
#         continue
#     elif keyword_input == "3":
#         num = int(input("您想要取多少钱？请输入："))
#         withdraw(num)
#         continue
#     else:
#         print("程序退出啦")
#         break

# # 定义一个列表List
# my_list=["itheima",'itcast',"python"]
# print(my_list)
# print(type(my_list))
# 定义一个嵌套的列表
# my_list=[[1,2,3],[4,5,6]]
# print(my_list)
# print(type(my_list))
# 语法： 列表[下标索引]
# name_list=['Tom','Lily','Rose']
# print(name_list[0])  # 结果：Tom
# print(name_list[1])  # 结果：Lily
# print(name_list[2])  # 结果：Rose
# 通过下标索引取出对应位置的数据
# my_list=["Tom","Lily",'Rose']
#列表[下标索引】，从前向后从0开始，每次+1，从后向前，每次-1
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# 错误示范: 通过下标索引获取数据，一定不要超出范围
# print(my_list[3])

# 通过下标索引取出对应位置的数据(倒序取出】
# print(my_list[-1])
# print(my_list[-2])
# print(my_list[-3])
# 取出嵌套列表的元素
# my_list=[[1,2,3],[4,5,6]]
# print(my_list[1][1])
# my_list=["itheima","itcast","python"]
# 1.1 查找某元素在列表内的下标索引
# index=my_list.index("itheima")
# print(f"itheima在列表中的下标索引值是：{index}")
# 1.2如果被查找的元素不存在，会报错
# index=my_list.index("hello")
# print(f"hello在列表中的下标索引值是:{index}")

# 2.修改特定下标索引的值
# my_list[0]="传智教育"
# print(f"列表被修改元素值后，结果是：{my_list}")
# 3.在指定下标位置插入新元素
# my_list.insert(1,"best")
# print(f"列表插入元素后，结果是：{my_list}")
# 4.在列表的尾部追加'''单个'''新元素
# my_list.append("黑马程序员")
# print(f"列表在追加了元素后，结果是：{my_list}")
# 5.在列表的尾部追加'''一批'''新元素
# my_list1=[1,2,3]
# my_list.extend(my_list1)
# print(f"列表在追加了一个新的列表后，结果是：{my_list}")
# 6.1 方法1：del 列表[下标]
# del my_list[2]
# print(f"列表删除元素后结果是：{my_list}")
# 6.2方法2，列表.pop（下标）
# my_list.pop(2)
# element=my_list.pop(2)
# print(f"通过pop方法列表删除元素后结果是：{my_list},取出的元素是{element}")
# 7.删除某元素在列表中第一个匹配项
# my_list=["itheima","itheima","itheima","itheima"]
# my_list.remove("itheima")
# print(f"通过remove方法移除元素后，列表的结果是:{my_list}")
# 8.清空列表
# my_list.clear()
# print(f"列表被清空啦！")
# 9.统计列表内某元素的数量：
# my_list=["itheima","itheima","itheima","itheima","itheima"]
# count=my_list.count("itheima")
# print(f"列表中itheima的数量是：{count}")
# 10.统计列表中全部的元素数量
# my_list=["itheima","itheima","itheima","itheima","itheima"]
# num=len(my_list)
# print(f"列表中的元素数量总共有{num}")
# 1.定义这个列表，并用变量接受它
# student_age=[21,25,21,23,22,20]
# print(f"学生的年龄分别是：{student_age}")
# 2.追加一个数字31，到列表的尾部
# student_age.append(47)
# print(f"追加一位补录的学生之后，学生年龄分别是：{student_age}")
# 3.追加一个新列表[29,33,30]，到列表的尾部
# student_age1=[1,2,3]
# student_age.extend(student_age1)
# print(f"追加一列补录的学生年龄列表，学生年龄分别是：{student_age}")
# 4.取出第一个元素(应是：21）
# student_age=[21,85,34,56]
# print(student_age[0])
# 5.取出最后一个元素（应是：30)
# student_age=[21,85,34,56,30]
# print(student_age[4])
# 6.查找元素31，在列表中的下标位置
# student_age=[21,85,34,56,31]
# index=student_age.index(31)
# print(f"元素31在列表中的下标位置是：{index}")
# def list_while_func():

    # 使用while循环遍历列表的演示函数
    # :return: None

    # my_list=["传智教育","黑马程序员","python"]
    # 循环控制变量通过下标索引来控制，默认0
    # 每一次循环将下标索引变量+1
    # 循环条件：下标索引变量 <列表的元素数量


    #定义一个变量用来标记列表的下标
    # index=0    #初始值为0
    # while index < len(my_list):
        # 通过index变量取出对应下标的元素
        # element=my_list[index]
        # print(f"列表的元素：{element}")
        # 至关重要 将循环变量(index) 每一次循环都+1
        # index +=1


# def list_for_func():
#
#     使用for循环遍历列表的演示函数
#     :return: None
#
#     my_list=[1,2,3,4,5]
#     for 临时变量 in 数据容量：
#     for element in my_list:
#         print(f"列表的元素有：{element}")
# list_while_func()
# list_for_func()
# 练习案例：取出列表内的偶数
# def list_while_func1():

    # 使用while循环遍历列表的演示函数
    # :return: None

    # my_list=[1,2,3,4,5,6,7,8,9,10]
    # 循环控制变量通过下标索引来控制，默认0
    # 每一次循环将下标索引变量+1
    # 循环条件：下标索引变量 <列表的元素数量

    # 定义一个变量用来标记列表的下标
    # index = 0  # 初始值为0
    # my_list1=[] #创建一串新列表
#     while index < len(my_list):
#        if my_list[index]%2==0:
#            my_list1.append(my_list[index])
#        index+=1
#     print(f"通过while循环，从列表：{my_list}中取出偶数，组成新列表{my_list1}")
# def list_for_func1():

    # 使用for循环遍历列表的演示函数
    # :return: None




    # my_list = [1, 2, 3, 4, 5,6,7,8,9,10]
    # my_list2=[]
    # for 临时变量 in 数据容量：
#     for element in my_list:
#         if element%2==0:
#             my_list2.append(element)
#     print(f"通过for循环，从列表：{my_list}，取出的偶数遍历为{my_list2}")
#
# list_while_func1()
# list_for_func1()

# 定义元组
# t1=(1,"Hello",True)
# t2=()
# t3=tuple()
# print(f"t1的类型是:{type(t1)},内容是:{t1}")
# print(f"t2的类型是:{type(t2)},内容是:{t2}")
# print(f"t3的类型是:{type(t3)},内容是:{t3}")
# 定义单个元素的元素
# t4=("hello",)
# print(f"t4的类型是：{type(t4)},t4的内容是：{t4}")
# 元组的嵌套
# t5=((1,2,3),(4,5,6))
# print(f"t5的类型是：{type(t5)},内容是{t5}")
# 元组的嵌套
# num=t5[1][2]
# print(f"从嵌套元组中取出的数据是:{num}")
# 元组的操作，index查找方法
# t6=("创智教育","黑马程序员","Python")
# index=t6.index("黑马程序员")
# print(f"在元组t6中查找黑马程序员,的下标是：{index}")
# 元组的操作:count统计方法
# t7=("创智教育","黑马程序员","黑马程序员","黑马程序员","python")
# num=t7.count("黑马程序员")
# print(f"在元组t7中统计黑马程序员的数量有：{num}")
# 元组的操作：len函数统计元组数量
# t8=("创智教育","黑马程序员","黑马程序员","黑马程序员","python")
# num=len(t8)
# print(f"t8元组中的元素有：{num}个")
# 元组的遍历
# index=0
# while index < len(t8):
#     print(f"元组的元素有：{t8[index]}")
    # 至关重要
    # index +=1

# 元组的遍历；for
# for element in t8:
#     print(f"元组的元素有:{element}")

# 修改元组内容
# t8[0]="itcast"
# 定义一个元组
# t9=(1,2,["itcast","itheima"])
# print(f"t9的内容是：{t9}")
# t9[2][0]="黑马程序员"
# t9[2][1]="传智教育"
# print(f"t9的内容是：{t9}")

# 定义一个元组
# t10=('周杰伦',11,['football','music'])
# position=t10.index(11)
# print(f"查询年龄所在的下标位置：{position}")
# research=t10[0]
# print(f"查询该名学生的姓名:{research}")
# t11=('周杰伦',11,['football','music'])
# del t11[2][0]
# print(f"删除学生中的football:{t11}")
# t11[2].insert(0,'coding')
# print(f"增加爱好：coding到爱好List内{t11}")

# 定义一个字符串
# my_str="itheima and itcast"
# 通过下标索引取值
# value=my_str[2]
# value2=my_str[-16]
# print(f"从字符串{my_str}取下标为2的元素的值是:{value},取下标为-16的元素，值是：{value2}")
# 字符串不支持修改

# index方法
# value=my_str.index("and")
# print(f"在字符串{my_str}中查找and,其起始下标是：{value}")
# replace方法
# new_my_str=my_str.replace("it","程序")
# print(f"将字符串{my_str},进行替换后得到：{new_my_str}")
# split方法
# my_str="hello python iteheima itcast"
# my_str_list=my_str.split("hello python iteheima itcast")
# print(f"将字符串{my_str}进行split切分后得到:{my_str_list},类型是{type(my_str_list)}")

# strip方法
# my_str="   itheima and itcast   "
# new_my_str=my_str.strip()
# print(f"字符串{my_str}被strip后，结果：{new_my_str}")
# my_str="12itheima and itcast21"
# new_my_str=my_str.strip("12")
# print(f"字符串{my_str}被strip('12')后，结果是：{new_my_str}")

# 统计字符串中某字符串的出现次数
# my_str="itheima and itcast"
# count=my_str.count("it")
# print(f"字符串{my_str}中it出现的次数是：{count}")
# 统计字符串的长度,len()
# num=len(my_str)
# print(f"字符串{my_str}的长度是{num}")
# 字符串的遍历
# while循环
# my_str="黑马程序员"
# index=0
# while index < len(my_str):
#     print(my_str[index])
#     index+=1
# for循环
# my_str="黑马程序员"
# for i in my_str:
#     print(i)
# 定义一个字符串
# my_str1="itheima itcast boxuegu"
# num=my_str1.count("it")
# print(f"字符串内有{num}个'it'字符")
# 将字符串内的空格，全部替换为字符:"|"
# new_my_str1=my_str1.replace(" ","|")
# print(f"将字符串内的空格转换为|,结果显示为:{new_my_str1}")
# 用split切割
# new_my_str1_list=new_my_str1.split("|")
# print(f"字符串{new_my_str1}按照|进行字符串切割，得到列表:{new_my_str1_list}")

# my_list=[0,1,2,3,4,5,6]
# result=my_list[1:4:1]  #步长默认是1，所以可以省略不写
# print(f"结果1:{result}")
# 对tuple进行切片,从头开始,到最后结束,步长1
# my_tuple=(0,1,2,3,4,5,6)
# result1=my_tuple[:]
# print(f"结果2:{result1}")
# 对str切片,从头开始,到最后结束,步长2
# my_str="0123456789"
# result2=my_str[::2]
# print(f"结果3:{result2}")
# 对str进行切片,从头开始,到最后结束,步长-1
# my_str="0123456789"
# result3=my_str[::-1]    # 等于将序列反转了
# print(f"结果4:{result3}")
# 对列表进行切片,从3开始,到1结束,步长-1
# my_list=[0,1,2,3,4,5,6]
# result4=my_list[3:1:-1]
# print(f"结果5:{result4}")
# 对元组进行切片,从头开始,到尾结束,步长-2
# my_tuple=(0,1,2,3,4,5,6)
# result6=my_tuple[:-2]
# print(f"结果6:{result6}")

# 练习
# my_str1="万过薪月,员序程马黑来,nohtyP学"
# result7=my_str1[5:10]
# print(f"结果7:{result7}")
# 将切片取出的字符串进行倒序
# result8=result7[::-1]
# print(f"结果8:{result8}")

# 定义集合
my_set={"传智教育","黑马程序员","itheima","传智教育","黑马程序员","itheima","传智教育","黑马程序员","itheima"}
my_set_empty=set()      # 定义空集合
print(f"my_set的内容是:{my_set}，类型是:{type(my_set)}")
print(f"my_set_empty的内容是:{my_set_empty}，类型是:{type(my_set_empty)}")
# 添加新元素
my_set.add("Python")
my_set.add("传智教育")
print(f"my_set添加元素后结果是:{my_set}")
# 移除元素
my_set.remove("黑马程序员")
print(f"my_set移除元素后结果是:{my_set}")
# 随机取出一个元素
my_set={"传智教育","黑马程序员","itheima"}
element=my_set.pop()
print(f"集合被取出元素是:{element},取出元素后:{my_set}")
# 清空集合
my_set.clear()
print(f"集合被清空啦,结果是:{my_set}")
# 取2个集合的差集
set1={1,2,3}
set2={1,5,6}
set3=set1.difference(set2)
print(f"取出差集后的结果是:{set3}")
print(f"取差集后,原有set1的内容是:{set1}")
print(f"取差集后,原有set2的内容是:{set2}")
# 消除2个集合的差集
set1={1,2,3}
set2={1,5,6}
set1.difference_update(set2)
print(f"消除差集后,集合1结果:{set1}")
print(f"消除差集后,集合2结果:{set2}")
# 2个集合合并为1个
set1={1,2,3}
set2={1,5,6}
set3=set1.union(set2)
print(f"2集合合并结果:{set3}")
print(f"合并后集合1:{set1}")
print(f"合并后集合2:{set2}")
# 统计集合元素len()
set1={1,2,3,4,5}
num=len(set1)
print(f"集合内的元素数量有:{num}")
# 集合的遍历
# 集合不支持下标索引,不能用while循环
# 可以用for循环
set1={1,2,3,4,5}
for element in set1:
    print(f"集合的元素有:{element}")

# 练习
my_list=['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best']
print(f"有列表：{my_list}")
my_set_empty1=set()
for element1 in my_list:
    
    my_set_empty1.add(element1)
print(f"存入集合后结果：{my_set_empty1}")
