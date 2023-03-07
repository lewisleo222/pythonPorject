#pip install requests
#pip install lxml
#发送请求
import  requests
from lxml import  etree
resp=requests.get("https://www.fang.com/")
#解析数据
resp.encoding='gbk'
e=etree.HTML(resp.text)
names =[n.strip() for n in e.xpath('//div[@class="nlcd_name"]/a/text')]
addreses=e.xpath('//div[@class="nlcd_name"]/a/title')
prices=[ d.xpath('string(.)').strip() for d in e.xpath('//div[@class="nlcd_name"]')]
comments=e.xpath('//span[@class="value_num"]/text()')
#处理数据
for n,a,p,c in zip(names,addreses,prices,comments):
    print(f'{n}=={a}=={p}=={c}')

