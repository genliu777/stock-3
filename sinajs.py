#coding=utf8
import urllib2
import urllib
from PIL import Image
class sinastock:
    def __init__(self):
        self.name = ''
        self.todayopeningprice = ''
        self.yesterdayclosingprice = -1
        self.currentprice = -1
        self.todayhighestprice = -1
        self.todayminimumprice = -1
        self.numberoftransactions = -1
        self.transactionprice = -1
        
    def GetDataByStockCode(self,StockCode):
        url = 'http://hq.sinajs.cn/list=' + StockCode
        rep = urllib2.Request(url)
        data = urllib2.urlopen(rep,timeout=10).read()
        first = data.find("\"")
        last = data.find("\"",first + 1)
        data = data[first+1:last]
        detail = data.split(",")
        self.name = detail[0]
        self.todayopeningprice = float(detail[1])
        self.yesterdayclosingprice = float(detail[2])
        self.currentprice = float(detail[3])
        self.todayhighestprice = float(detail[4])
        self.todayminimumprice = float(detail[5])
        self.numberoftransactions = float(detail[8])
        self.transactionprice = float(detail[9])
        return self
    
    def GetDailyKLineByStockCode(self,StockCode):
        url = 'http://image.sinajs.cn/newchart/daily/n/' + StockCode +'.gif'
        localpath = 'e:/stock/k/daily' + StockCode + '.gif'
        urllib.urlretrieve(url,localpath)
        image = Image.open(localpath)
        image.show()
        
    def GetTimeLineByStockCode(self,StockCode):
        url = 'http://image.sinajs.cn/newchart/min/n/' + StockCode +'.gif'
        localpath = 'e:/stock/k/min' + StockCode + '.gif'
        urllib.urlretrieve(url,localpath)
        image = Image.open(localpath)
        image.show()
        
    def GetWeeklyKLineByStockCode(self,StockCode):
        url = 'http://image.sinajs.cn/newchart/weekly/n/' + StockCode +'.gif'
        localpath = 'e:/stock/k/weekly' + StockCode + '.gif'
        urllib.urlretrieve(url,localpath)
        image = Image.open(localpath)
        image.show()
        
    def GetMonthlyKLineByStockCode(self,StockCode):
        url = 'http://image.sinajs.cn/newchart/monthly/n/' + StockCode +'.gif'
        localpath = 'e:/stock/k/monthly' + StockCode + '.gif'
        urllib.urlretrieve(url,localpath)
        image = Image.open(localpath)
        image.show()
        
    def Getsh(self):
        url = 'http://hq.sinajs.cn/list=s_sh000001'
        rep = urllib2.Request(url)
        data = urllib2.urlopen(rep,timeout=10).read()
        first = data.find("\"")
        last = data.find("\"",first + 1)
        data = data[first+1:last]
        detail = data.split(",")
        return 

