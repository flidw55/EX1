# -*- coding: utf8 -*-
import pandas as pd
from matplotlib import pyplot as plt

url = 'http://www.thsrc.com.tw/tw/TimeTable/DailyTimeTable/20170525'
StartPoint=u'雲林站'
ArrivePoint=u'板橋站'
TablePd=pd.read_html(url)[5]

re1={}
for i in range(len(TablePd.ix[1])):
    re1[i]=TablePd.ix[0][i]
'''  
print re1
print re1[5]
print type(re1[5])
'''
TablePd=TablePd.rename(columns = re1)
TablePd=TablePd.drop(TablePd.index[[0]])

#print(TablePd[StartPoint])


StartTimer=[]
ArriveTimer=[]
for i in range(1,len(TablePd)):
    if TablePd.notnull()[StartPoint][i] and TablePd.notnull()[ArrivePoint][i] :
        StartTimer.append(TablePd[StartPoint][i])
        ArriveTimer.append(TablePd[ArrivePoint][i])

xs = [i for i, _ in enumerate(StartTimer)]
ys = [i for i, _ in enumerate(ArriveTimer)]
plt.plot(xs, ys, 'bx')
plt.xticks([i  for i, _ in enumerate(StartTimer)],StartTimer)
plt.yticks([i  for i, _ in enumerate(ArriveTimer)],ArriveTimer)
plt.title("Nike")
plt.xlabel("%s" %StartPoint)
plt.ylabel("%s" %ArrivePoint)
plt.show()
