import akshare as ak

"""
1）从巨潮资讯上取数据已经失效
stock_dividents_cninfo()源代码中可以看到分红数据取自：巨潮资讯-个股-历史分红
链接：http://webapi.cninfo.com.cn/#/company?companyid=600009
2）使用东财接口，带有股本信息
"""

class Divident(object):
    def __init__(self, stock):
        self._stock = stock        
        self._fhps = ak.stock_fhps_detail_em(symbol=stock)

    def extract_simple_info(self):
        #print(self._fhps.columns)
        check_fields = [
            '报告期', 
            '业绩披露日期', 
            '现金分红-现金分红比例描述', 
            '现金分红-股息率',
            '每股收益',
            '每股净资产',
            '净利润同比增长',
            '总股本']

        fhps_df = self._fhps[check_fields]
        fhps_df = fhps_df.set_index('报告期').sort_index()        
        fhps_df.plot(figsize=(10,5), subplots=True, secondary_y=['总股本'])        
        print(fhps_df)

if __name__ == "__main__":
    #code = '002304' # 洋河股份
    #code = '600519' # 贵州茅台
    #code = '000858' # 五粮液
    #code = '000568' # 泸州老窖 
    code = '600809' # 山西汾酒
    #code = '000596' # 古井贡

    fhps = Divident(code)
    fhps.extract_simple_info()