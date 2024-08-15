import numpy as np
import matplotlib.pyplot as plt

import sheet

class XjllbAnalyzer():
    def __init__(self, raw_xjllb, raw_lrb):                
        self._cashflow_df = sheet.convert_to_numeric(raw_xjllb)
        self._income_df = sheet.convert_to_numeric(raw_lrb)

        self._df = self._cashflow_df[[
            '销售商品、提供劳务收到的现金',
            '经营活动产生的现金流量净额',
            '投资活动产生的现金流量净额',
            '筹资活动产生的现金流量净额',
            '现金及现金等价物净增加额']]
        self._df['净利润'] = self._income_df['净利润']

    @property
    def numberic_df(self):
        return self._cashflow_df
    
    def plot(self):
        plt.rcParams['axes.unicode_minus'] = False
        plt.rcParams['font.sans-serif'] = ['SimHei']
        df = self._cashflow_df.copy()

        net_items = self._df[[
            '经营活动产生的现金流量净额',
            '投资活动产生的现金流量净额',
            '筹资活动产生的现金流量净额',
            '现金及现金等价物净增加额']]
        print(net_items)
        sheet.plot(net_items)

        net_income_items = self._df[[
            '经营活动产生的现金流量净额',
            '净利润']]
        print(net_income_items)
        sheet.plot(net_income_items)

    def analyze(self):        
        self.plot()

if __name__ == "__main__":
    #code = '002304' # 洋河股份
    code = '300760' # 迈瑞医疗
    s = sheet.Sheet(code)
    xjllb = XjllbAnalyzer(s.xjllb, s.lrb)
    xjllb.analyze()