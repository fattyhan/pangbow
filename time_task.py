from threading import Thread
import time
import cn2an
import speech as sp

def do_work(t,w):
    sp.speak('好的，胖宝准备好了，'+str(t)+'秒后提醒您。')
    time.sleep(t)
    sp.speak('小主，胖宝提醒您该'+w+'啦。')

def start_task(t,w):
    thread = Thread(target=do_work, kwargs={'t': 2,'w': w})
    thread.start()
    sp.speak('好的，胖宝准备好了，'+t+'秒后提醒您。')
def init_task(w):
    time_int = 0
    if('秒后') in w or ('秒钟') in w:
        time_text = w[0:w.find('秒')]
        time_int = cn2an.cn2an(time_text, "smart")
    if('分钟') in w:
        time_text = w[0:w.find('分')]
        time_int = cn2an.cn2an(time_text, "smart")
        time_int = time_int*60
    if ('小时') in w:
        time_text = w[0:w.find('小时')]
        time_int = cn2an.cn2an(time_text, "smart")
        time_int = time_int*3600

    task_info = w[w.find('我')+1:]
    do_work(time_int,task_info)
init_task('五秒钟后叫我喝水')