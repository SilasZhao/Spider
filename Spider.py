import requests
import json
import time

url1 = "https://report.amap.com/ajax/cityHourly.do?cityCode="
url2 = "&dataType=4"
#cityCode 可以从excel中找到
Beijing = "110000"
Shanghai = "310000"
Guangzhou="440100"
Shenzhen="440300"
Chengdu="510100"
Hangzhou = "330100"
Wuhan="420100"

#所有城市的列表
cityList = list([Beijing,
            Shanghai,
            Guangzhou,
            Shenzhen,
            Chengdu,
            Hangzhou,
            Wuhan])

def getList(url1,url2,cityCode):
    response = requests.get(url1+cityCode+url2)
    return json.loads(response.text)

#在8-9点时没有数据
def getNumber(targetTime,responseList):
    for i in responseList:
        #每个list的list[0]/1000就是其时间的时间戳
        timeStamp = int((i[0] / 1000))
        hour = time.localtime(timeStamp).tm_hour
        if hour == targetTime:
            #返回最后一位
            return str(i[1])[-1]

if __name__=='__main__':
    code = ""
    for i in cityList:
        code += getNumber(8,getList(url1,url2,i))
    print(code)



    

