# 定义字典
my_dict={"王力宏":99,"周杰伦":77,"林俊杰":77}
# 定义空字典
my_dict1={}
my_dict2=dict()
print(f"字典1的内容是:{my_dict},类型：{type(my_dict)}")
print(f"字典2的内容是:{my_dict1},类型：{type(my_dict1)}")
print(f"字典3的内容是:{my_dict2},类型：{type(my_dict2)}")
# 定义重复的key字典
my_dict4={"王力宏":99,"王力宏":78,"周杰伦":77,"林俊杰":77}
print(f"重复key的字典的内容是:{my_dict4}")
# 从字典中基于key获取value
my_dict={"王力宏":99,"周杰伦":77,"林俊杰":77}
score=my_dict["王力宏"]
print(f"王力宏的考试分数是：{score}")
# 定义嵌套字典
stu_score_dict={
    "王力宏":{
        "语文":77,
        "数学":66,
        "英语":33
    },"周杰伦":{
        "语文":88,
        "数学":86,
        "英语":55
    },"林俊杰":{
        "语文":99,
        "数学":96,
        "英语":66
    }

}
print(f"学生的考试信息是：{stu_score_dict}")
# 从嵌套字典中获取数据
# 看一下周杰伦的语文信息
score=stu_score_dict["周杰伦"]["语文"]
print(f"周杰伦的语文分数是:{score}")

