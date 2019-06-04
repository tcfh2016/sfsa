import matplotlib.pyplot as plt
from jqdatasdk import *
plt.rcParams['font.family']=['SimHei']
auth('13958111292','julianchenyi1')

# 000001.XSHG 	上证指数
indexs_2009 = get_index_stocks('000001.XSHG', date='2009-05-15')
print ('2009-05-15 上证样本股数量：%d' % len(indexs_2009))

indexs_2019 = get_index_stocks('000001.XSHG', date='2019-05-15')
print ('2019-05-15 上证样本股数量：%d' % len(indexs_2019))

sz_index_trend = get_price('000001.XSHG', '2009-05-15', '2019-05-15', 'daily', 'close')
sz_index_trend.columns = ['上证指数']

sz_index_trend.plot(subplots=False, grid=True, legend=True)
plt.show()
