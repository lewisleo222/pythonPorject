# 1.从aip中导入相应文字识别模块aipocr
from aip import AipOcr
# 2.复制粘贴你的AppId,AK,SK等3个常量，并以此初始化对象
APP_ID='30785532'
API_KEY='1YHGb2smo7pTAYEnYhRqId8p'
SECRET_KEY='2I4INkT9wdbqzv4zjwCMwG1DpSlGWcpY'

aipOcr=AipOcr(APP_ID,API_KEY,SECRET_KEY)
filePath=r'C:\Users\k\Desktop\image\book\a35.png'
with open(filePath, 'rb') as fp:
    image = fp.read()

result=aipOcr.basicGeneral(image)

if 'words_result' in result:
    Mywords = result['words_result']
    print(Mywords)
else:
    print('API 请求失败或响应不符合预期')