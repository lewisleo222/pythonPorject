

## 1. 从aip中导入相应自然语言处理模块 AipNlp
from aip import AipSpeech

## 2.拷贝粘贴你的 APPID、AK、SK等3个常量,并以此初始化对象
APP_ID = '17181021'
API_KEY = '16YjmjjrwUt4x3NHmuXKsxZg'
SECRET_KEY = '2SkFkmGMttTbz5sQWVX7NMAZW8itH8mN'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

## 3.定义数据
text = "庆祝无锡职业技术学院60周年校庆"

## 4.直接调用情感倾向分析接口，并输出结果
result  = client.synthesis(text)

## 4.直接调用情感倾向分析接口，作个性化定制
result  = client.synthesis(text, 'zh', 1, {
    'vol': 5,
})

# 5 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)

# 6 直接播放
import os
os.system('auido.mp3')
#from playsound import playsound
#
## 6 语音播放
#playsound('D:/Data/ MyVoice.mp3')
