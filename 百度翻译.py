"""

[课    题]：Python 爬虫项目--百度翻译JS解密

[难度指数]: ☆☆☆☆(满级难度十颗星)

[讲    师]: 青灯教育--益达

[授课时间]: 19:35

[使用环境]: Anaconda (python3.9) 解释器 识别我们写的代码

[开发工具]: pycharm 编辑器

[使用模块]: requests >>> pip install requests   <第三方模块>
           execjs >>> pip install pyexecjs     <第三方模块>
           Node.js 插件
           JavaScript 解释器  前端语言




[软件没安装?]
找到给你发上课链接的老师领取
Anaconda / python3.9 / pycharm(专业破解版/社区版) 安装包以及安装视频教程


[听不懂? 没基础?]
屏幕右上角是助教[玲玲老师]的微信 可扫码添加 添加以后可以找到[玲玲老师]领取:
I. 本节课源码 (没基础的同学主要学习编程的思路逻辑, 不建议一起敲代码)
II.领取0基础的视频教程一套 (基础编程 and 爬虫基础)


推出了三个班级
① 训练营 2天 特定的课题 群 一周解答服务 录播 5年 9.9  VIP的体验
挖掘数据价值
② 兴趣班 3-4个月 爬虫/数据分析 (基础+爬虫/数据分析+高级开发) 做兼职 一年 录播终身有效 提供兼职外包平台 外包指导
就业的选择比较少  3880 一次性 免息分期 3 6 9 12 300左右 就业选择会少一些


③ 就业班 7个月 (基础+爬虫+数据分析+全栈开发) 就业 2年 录播也是终身有效  提供兼职外包平台 外包指导 就业指导 推荐就业
8k-15K  8080  一次性 免息分期 18期 400左右 就业选择性非常多 爬虫工程师 数据分析师 web开发工程师 人工智能 自动化办公

腾讯课堂 每周3节课 晚上8点-到晚上10点 每周6-8个小时的学习时间即可


"""

import requests
import execjs  # 编译JS代码
# pip install pyexecjs2 -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com



while True:
    key_word = input('请输入你要翻译的内容(输入0退出)：')
    if key_word == '0':
        break
    with open('百度翻译.js', mode='r', encoding='utf-8') as f:
        js_code = f.read()
    compile_result = execjs.compile(js_code)
    sign = compile_result.call('e', key_word)

    url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
    headers = {
        'Cookie': 'PSTM=1675841670; BAIDUID=B22016C28DCE3B165E81E18E0645BFA5:FG=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BIDUPSID=B22016C28DCE3B16DDCCC40F26BDA3DE; delPer=0; PSINO=3; BDRCVFR[krBU_nwdDgR]=mk3SLVN4HKm; BA_HECTOR=8g00012l010h0lak040kahnn1hupqa11l; ZFY=GOKJbP1uTHNJj3iNq5TJKtQKlZMwXCs3RftSdSVsf4w:C; BAIDUID_BFESS=B22016C28DCE3B165E81E18E0645BFA5:FG=1; BDRCVFR[S4-',
        'Host': 'fanyi.baidu.com',
        'Origin': 'https://fanyi.baidu.com',
        'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }

    data = {
        'from': 'zh',
        'to': 'en',
        'query': key_word,
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': sign,
        'token': 'ff0dd9077e8dd121d1aa29f684670b58',
        'domain': 'common',
    }
    response = requests.post(url=url, data=data, headers=headers)
    result = response.json()['trans_result']['data'][0]['dst']
    print(result)