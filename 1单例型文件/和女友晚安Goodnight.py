#��Ҫ����Դ������У�����Ҫ�Ķ������ط�

from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests


#bot = Bot()
bot = Bot(console_qr=2,cache_path="botoo.pkl")   ��������#����Ķ�ά���������ص���ʽ��ӡ���������������win���������У��滻Ϊ  bot=Bot()


def get_news1():
����#��ȡ��ɽ�ʰ�ÿ��һ�䣬Ӣ�ĺͷ���
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    contents = r.json()['content']
    translation= r.json()['translation']
    return contents,translation

def send_news():
    try:
        my_friend = bot.friends().search(u'ͽ�־�����')[0]    #�����ѵ�΢�����ƣ����Ǳ�ע��Ҳ����΢���ʺš�
        my_friend.send(get_news1()[0])
        my_friend.send(get_news1()[1][5:])
        my_friend.send(u"���԰ְֵ����鼦����")
        t = Timer(86400, send_news)���� ������������������������#ÿ86400�루1�죩������1�Σ�����linux�Ķ�ʱ��������Ϊÿ�ε�½����Ҫɨ���ά���½�����鷳��һ���£�������һֱ���Ű�
        t.start()
    except:
        my_friend = bot.friends().search('����')[0]       ����#���΢�����ƣ�����΢���ʺš�
        my_friend.send(u"������Ϣ����ʧ����")
        

    
if __name__ == "__main__":
    send_news()