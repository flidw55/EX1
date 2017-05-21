# -*- coding: utf8 -*-
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
from datetime import datetime
url = 'http://www.thsrc.com.tw/tw/TimeTable/DailyTimeTable/20170525'
StartPoint= u'雲林站'
ArrivePoint= u'板橋站'
TablePd=pd.read_html(url)[5]

zhfont=matplotlib.font_manager.FontProperties(fname = 'C:\Windows\Fonts\kaiu.ttf')

re1={}
for i in range(len(TablePd.ix[1])):
    re1[i]=TablePd.ix[0][i]

TablePd=TablePd.rename(columns = re1)
TablePd=TablePd.drop(TablePd.index[[0]])

#print(TablePd[StartPoint])


StartTimer=[]
ArriveTimer=[]
for i in range(1,len(TablePd)):
    if TablePd.notnull()[StartPoint][i] and TablePd.notnull()[ArrivePoint][i] :
        StartTimer.append(datetime.strptime(TablePd[StartPoint][i],'%H:%M'))
        ArriveTimer.append(datetime.strptime(TablePd[ArrivePoint][i],'%H:%M'))

# xs = [i for i, _ in enumerate(StartTimer)]
# ys = [i for i, _ in enumerate(ArriveTimer)]
# plt.plot(xs, ys, 'bx')
# plt.xticks([i  for i, _ in enumerate(StartTimer)],StartTimer)
# plt.yticks([i  for i, _ in enumerate(ArriveTimer)],ArriveTimer)
# plt.title(u"高鐵時間分配圖" ,fontproperties=zhfont)
# plt.xlabel("%s" %StartPoint ,fontproperties=zhfont)
# plt.ylabel("%s" %ArrivePoint ,fontproperties=zhfont)
# plt.show()


plt.title(u"高鐵時間分配圖",fontproperties=zhfont)
plt.xlabel("%s" %StartPoint,fontproperties=zhfont)
plt.ylabel("%s" %ArrivePoint,fontproperties=zhfont)
#plt.axis([datetime.strptime("2017/05/20 06:00",'%Y/%m/%d %H:%M'),datetime.strptime("2017/05/20 12:00",'%Y/%m/%d %H:%M'),datetime.strptime("2017/05/20 06:00",'%Y/%m/%d %H:%M'),datetime.strptime("2017/05/20 12:00",'%Y/%m/%d %H:%M')])
#plt.axis([datetime.strptime("06:00",'%H:%M'),datetime.strptime("12:00",'%H:%M'),datetime.strptime("06:00",'%H:%M'),datetime.strptime("12:00",'%H:%M')])
plt.plot(StartTimer,ArriveTimer, 'bx')
plt.show()