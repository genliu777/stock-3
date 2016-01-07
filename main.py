#coding=utf8
import time
from PIL import Image
from sinajs import sinastock

def SHIndexMon():
    while True:
        detail = data.Getsh()
        print detail.indexname,detail.currentindex,detail.indexincrease,detail.indexchangerate
        if abs(detail.indexincrease) > 5 and abs(detail.indexincrease) < 7:
            time.sleep(890)
            print 'boom!'
        if abs(detail.indexincrease) > 7:
            print 'boom!boom!boom!'
            print 'game over!'
            break
        time.sleep(10)
        

if __name__ == '__main__':
    data = sinastock()
    #detail = data.GetDataByStockCode('sh601006')
    #detail = data.GetDailyKLineByStockCode('sh601006')
    #detail = data.Getsh()
    SHIndexMon()
