from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from jqdatasdk import *
plt.rcParams['font.family']=['SimHei']
auth('**','**')


count=get_query_count()
print(count)

# 计算指数平均市盈率的函数，仅计算市盈率为正的样本股市盈率
def get_pe_of_index(index, date):
    stocks = get_index_stocks(index, date)
    pe_query = query(valuation.pe_ratio).filter(valuation.code.in_(stocks))
    pe_data_df = get_fundamentals(pe_query, date)
    pe_data_list = list(pe_data_df['pe_ratio'])
    #print(pe_data_list)

    positive_pe_sum = 0.0
    cnt = 0
    for pe in pe_data_list:
        if pe > 0.0:
            positive_pe_sum += pe
            cnt += 1

    average_pe = positive_pe_sum / cnt
    #print(average_pe)
    return average_pe

# 获取中证500（ 000905.XSHG）在2009-05-15到2019-05-15期间交易日的收盘价
history_price = get_price('000905.XSHG', '2009-05-15', '2019-05-15', 'daily', 'close')

# 计算2009-05-15到2019-05-15期间的交易日指数成分股的平均市盈率
trade_date = history_price.index
history_pe = []
for d in trade_date:
    average_pe = get_pe_of_index('000905.XSHG', d)
    average_pe = 20
    history_pe.append(average_pe)

print(len(history_pe))
print(len(history_price['close']))

# 将计算出来的平均市盈率添加到收盘价所属的DataFrame
history_price['pe_average'] = history_pe
history_price.columns = ['收盘价', '平均市盈率']
history_price.plot(subplots=False, grid=True, legend=True, secondary_y='平均市盈率')
plt.show()
