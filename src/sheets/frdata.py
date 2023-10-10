import akshare as ak
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

class FinancialReport(object):
    def __init__(self, stock):
        self._stock = stock
        self._date_yearly = ['']
        
        self._zcfzb = ak.stock_financial_report_sina(stock=stock, symbol="资产负债表")
        self._lrb = ak.stock_financial_report_sina(stock=stock, symbol="利润表")
        self._xjllb = ak.stock_financial_report_sina(stock=stock, symbol="现金流量表")
    
    def extract_yearly_zcfzb(self):
        #print(self._zcfzb.columns)
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
        #print(self._lrb.columns)
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
        #print(self._xjllb.columns)
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

    finalcial_report = FinancialReport(code)
    finalcial_report.extract_yearly_zcfzb()
    finalcial_report.extract_yearly_lrb()
    finalcial_report.extract_yearly_xjllb()