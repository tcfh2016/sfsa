import akshare as ak
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

# 构建全新的年度数据用于计算
# 1. 将没有3个有效数据（非NaN）的列视作无效列，丢弃 - drop
# 2. 替换NaN为0，为后续数据统一类型做准备
# 3. 将所有值转换为 float格式
def convert_to_numeric(raw_df):
    raw_df = raw_df.set_index('报告日')
    df = raw_df.loc[:, ~raw_df.columns.isin(['数据源', '是否审计', '公告日期', '币种', '类型', '更新日期'])].copy()    
    df.fillna(0, inplace=True)
    
    for col in df:
        df[col] = pd.to_numeric(df[col])
    return df

def plot(values, percent = False):
    fig, axes = plt.subplots(nrows=2, ncols=2, sharey=True)
    df = values.T

    s_1st = df.loc[:, df.columns.str.contains('0331')].T
    plot = s_1st.plot(ax=axes[0, 0], figsize=(8, 6))
    
    s_2nd = df.loc[:, df.columns.str.contains('0630')].T
    plot = s_2nd.plot(ax=axes[0, 1], figsize=(8, 6))

    s_3rd = df.loc[:, df.columns.str.contains('0930')].T
    plot = s_3rd.plot(ax=axes[1, 0], figsize=(8, 6))

    s_4st = df.loc[:, df.columns.str.contains('1231')].T
    plot = s_4st.plot(ax=axes[1, 1], figsize=(8, 6))
    plot.legend(s_4st.columns)

    if percent:
        vals = plot.get_yticks()
        plot.set_yticklabels(['{:,.2%}'.format(x) for x in vals])

class Sheet(object):
    def __init__(self, stock):
        self._stock = stock
        self._date_yearly = ['']
        
        self._zcfzb = ak.stock_financial_report_sina(stock=stock, symbol="资产负债表")
        self._lrb = ak.stock_financial_report_sina(stock=stock, symbol="利润表")
        self._xjllb = ak.stock_financial_report_sina(stock=stock, symbol="现金流量表")
    
    @property
    def zcfzb(self):
        return self._zcfzb

    @property
    def lrb(self):
        return self._lrb
    
    @property
    def xjllb(self):
        return self._xjllb

    def overview(self):
        self.extract_yearly_zcfzb()
        self.extract_yearly_lrb()
        self.extract_yearly_xjllb()

    def extract_yearly_zcfzb(self):
        print(self._zcfzb.columns.values)
        check_fields = [
            '报告日', 
            '资产总计', 
            '负债合计', 
            '所有者权益(或股东权益)合计']

        zcfzb_df = self._zcfzb[check_fields]
        zcfzb_df = zcfzb_df[zcfzb_df['报告日'].str.find('1231') != -1]
        zcfzb_df = zcfzb_df.set_index('报告日').sort_index()
        zcfzb_df = zcfzb_df.apply(lambda x : np.float64(x) / 100000000)
        zcfzb_df.plot(figsize=(10,5))
        print(zcfzb_df)

    def extract_yearly_lrb(self):
        print(self._lrb.columns.values)
        check_fields = [
            '报告日', 
            '营业总收入', 
            '营业总成本',
            '营业利润', 
            '净利润']
        
        lrb_df = self._lrb[check_fields]
        lrb_df = lrb_df[lrb_df['报告日'].str.find('1231') != -1]
        lrb_df = lrb_df.set_index('报告日').sort_index()
        lrb_df = lrb_df.apply(lambda x : np.float64(x) / 100000000)
        lrb_df.plot(figsize=(10,5))
        print(lrb_df)

    def extract_yearly_xjllb(self):
        print(self._xjllb.columns.values)
        check_fields = [
            '报告日', 
            '经营活动产生的现金流量净额', 
            '投资活动产生的现金流量净额', 
            '筹资活动产生的现金流量净额',
            '现金及现金等价物净增加额']

        xjllb_df = self._xjllb[check_fields]
        xjllb_df = xjllb_df[xjllb_df['报告日'].str.find('1231') != -1]
        xjllb_df = xjllb_df.set_index('报告日').sort_index()
        xjllb_df = xjllb_df.apply(lambda x : np.float64(x) / 100000000)
        xjllb_df.plot(figsize=(10,5))
        print(xjllb_df)
        
if __name__ == "__main__":
    #code = '002304' # 洋河股份
    #code = '600519' # 贵州茅台
    #code = '000858' # 五粮液
    #code = '000568' # 泸州老窖 
    #code = '600809' # 山西汾酒
    code = '000596' # 古井贡
    
    sheets = Sheet(code).overview()
    