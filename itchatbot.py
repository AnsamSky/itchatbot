# coding=utf-8
import itchat, time,re
from itchat.content import *
import urllib
import json

#通过以下命令可以在登陆的时候使用命令行显示二维码：
#itchat.auto_login(enableCmdQR=True)
# 如部分的linux系统，块字符的宽度为一个字符（正常应为两 字符），故赋值为2
#itchat.auto_login(enableCmdQR=2)
#默认控制台背景色为暗色（黑色），若背景色为浅色（白色），可以将enableCmdQR赋值为负值：
#itchat.auto_login(enableCmdQR=-1)
#通过如下命令登陆，即使程序关闭，一定时间内重新开启也可以不用重新扫码。
#itchat.auto_login(hotReload=True)

itchat.auto_login(hotReload=True,enableCmdQR=True)

#如果你想要给文件传输助手发一条信息，只需要这样：
#itchat.send('Hello, 哈哈哈哈', toUserName='filehelper')




@itchat.msg_register([TEXT])
def text_reply(msg):
    #info = msg['Text'].encode('UTF-8')
    info = msg['Text']
    url = 'http://www.tuling123.com/openapi/api'
    data_msg = {"key": "8019d7394bde451193bf20fa291a715f", "info": info, "loc": "", "userid": ""}
    #data = urllib.urlencode(data)
    data_msg = urllib.parse.urlencode(data_msg).encode(encoding='UTF8')
    url2 = urllib.request.Request(url,data_msg)
    response = urllib.request.urlopen(url2)
    apicontent = response.read()
    #s = json.loads(apicontent,encoding = 'utf-8')
    s = json.loads(apicontent.decode('utf-8'))
    print('s==',s)
    if s['code'] == 100000:
        itchat.send(s['text'], msg['FromUserName'])

itchat.auto_login(hotReload=True, enableCmdQR = 2)
itchat.run(debug = True)
