import requests,json

def daily_report():
    url = 'https://restapi.amap.com/v3/weather/weatherInfo?key=7e1879041e4f9d61c892de9908ebd378&city=110112&extensions=base&output=JSON'
    response = requests.get(url=url,timeout=15)
    response.encoding = response.apparent_encoding
    r_text = str(response.content.decode('utf-8'))
    r_json = json.loads(r_text.replace('\n','\\n'))
    w_info = r_json['lives'][0]['city']+'当前天气'+r_json['lives'][0]['weather']+',温度'+r_json['lives'][0]['temperature_float']+'摄氏度，风向'+r_json['lives'][0]['winddirection']+'风力'+r_json['lives'][0]['windpower']+'级,湿度'+r_json['lives'][0]['humidity_float']
    print(w_info+'。以上就是今天的天气信息啦')

def daily_casts_report():
    url = 'https://restapi.amap.com/v3/weather/weatherInfo?key=7e1879041e4f9d61c892de9908ebd378&city=110112&extensions=all&output=JSON'
    response = requests.get(url=url,timeout=15)
    response.encoding = response.apparent_encoding
    r_text = str(response.content.decode('utf-8'))
    r_json = json.loads(r_text.replace('\n','\\n'))['forecasts'][0]
    w_info = r_json['city']+'今天白天'+r_json['casts'][0]['dayweather']+'，今日晚间'+r_json['casts'][0]['nightweather']+',最高温度'+r_json['casts'][0]['daytemp']+'摄氏度，最低温度'+r_json['casts'][0]['nighttemp']+'摄氏度。风向'+r_json['casts'][0]['daywind']+',风力'+r_json['casts'][0]['daypower']+'级。'
    if '晴' in r_json['casts'][0]['dayweather']:
    	w_info = w_info+'今天是个好天气不如出去走走吧，'
    else:
        w_info = w_info+'今天天气不是很好喔，早点回家喔，'
    if int(r_json['casts'][0]['daytemp']) >= 28:
    	w_info = w_info + '记得防晒喔'
    if int(r_json['casts'][0]['daytemp']) < 20:
        w_info = w_info + '记得加衣服喔'
    return w_info+'。以上就是今天的天气信息啦'
#daily_casts_report()
