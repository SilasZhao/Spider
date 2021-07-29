import requests
import json
import time

url = "https://report.amap.com/ajax/cityHourly.do?cityCode={}&dataType=4"

#cityCode 可以从excel中找到
Beijing = "110000"
Shanghai = "310000"
Guangzhou="440100"
Shenzhen="440300"
Chengdu="510100"
Hangzhou = "330100"
Wuhan="420100"

#所有城市的列表
cityList = list([["Beijing","110000"],
                ["Shanghai", "310000"],
                ["Guangzhou", "440100"],
                ["Shenzhen", "440300"],
                ["Chengdu", "510100"],
                ["Hangzhou" , "330100"],
                ["Wuhan","420100"]])

def getList(url,cityCode):
    try:
        response = requests.get(url.format(cityCode))
        response.raise_for_status()
    except requests.RequestException as e:
        print(e)
    else:
        return json.loads(response.text)

#在8-9点时没有数据
def getNumber(targetTime,responseList):
    for i in responseList:
        #每个list的list[0]/1000就是其时间的时间戳
        timeStamp = int((i[0] / 1000))
        hour = time.localtime(timeStamp).tm_hour
        if hour == targetTime:
            #返回车速
            return str(i[1])

if __name__=='__main__':
    code = []
    for i in cityList:
        speed = {i[0]: getNumber(8,getList(url,i[1]))}
        code.append(speed)
    print(json.dumps(code))



    

