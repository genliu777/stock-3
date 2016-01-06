#coding=utf8
from PIL import Image
from sinajs import sinastock

if __name__ == '__main__':
    data = sinastock()
    detail = data.GetDataByStockCode('sh601006')
    #print detail.name,detail.currentprice
    data.GetDailyKLineByStockCode('sh601006')
    
