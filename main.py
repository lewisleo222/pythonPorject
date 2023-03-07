# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""设计第一个python小游戏"""
temp= input("不妨猜一下小甲鱼现在的心里想的是哪个数字捏？")
guess=int(temp)
if guess==8:
    print("你是小甲鱼心里的蛔虫么？")
    print("猜中了也没奖励，哼哼")
else:
    print("猜错啦，小甲鱼现在心里想的是8！")
    print("游戏结束，不玩啦！")
