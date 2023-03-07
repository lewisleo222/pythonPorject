"""# 中职通0基础课
name="战三法外狂徒"
print(name)
"""

"""# 爬取视频
import you_get
import sys
url=('https://www.bilibili.com/video/BV15b41157i4/?spm_id_from=333.337.search-card.all.click&vd_source=01430aae34dd6345753a098bb6c4ba94')
file='video'
sys.argv = ['you-get','-o',file,url];you_get.main()"""

"""import urllib.parse

import urllib.request
# txt='你好，美女'
txt=input('请输入你要说的话')
text=urllib.parse.quote(txt)
# 智能聊天机器人
# 获取数据 http://api.qingyunke.com/api.php?key=free&appid=0&msg
# 导入工具包

import requests
# 打印 读取 转换 白话 万国码
result=urllib.request.urlopen('{},{}' .format('http://api.qingyunke.com/api.php?key=free&appid=0&msg',text))
print(result.read().decode('utf-8'))"""

"""import  requests
import  json
tex=input('请输入')

url='{},{}' .format('http://api.qingyunke.com/api.php?key=free&appid=0&msg',tex)
req=requests.get(url)
print(req.text)
res=json.loads(req.text)
res["content"]"""




