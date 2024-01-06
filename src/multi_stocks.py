import akshare as ak
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sheets.sheet as sheet
import sheets.zcfzb as zcfzb
import sheets.lrb as lrb
import sheets.xjllb as xjllb

plt.rcParams['font.sans-serif'] = ['SimHei']


if __name__ == "__main__":
    code_list = {
        '002304':'洋河股份',
        '600519':'贵州茅台',
        '000858':'五粮液',
        '000568':'泸州老窖',
        '600809':'山西汾酒',
        '000596':'古井贡'
    }
    
    # 资产负债表分析
    zc_df, fz_df, yyzsr_df, jlr_df = pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
    for key in code_list:
        sheet_data = sheet.Sheet(key)

        zcfz_df = zcfzb.ZcfzbAnalyzer(sheet_data.zcfzb).numberic_df
        zc_df[code_list[key]] = zcfz_df['资产总计'][0:40]
        fz_df[code_list[key]] = zcfz_df['负债合计'][0:40]

        lrb_df = zcfzb.ZcfzbAnalyzer(sheet_data.lrb).numberic_df
        yyzsr_df[code_list[key]] = lrb_df['营业总收入'][0:40]
        jlr_df[code_list[key]] = lrb_df['净利润'][0:40]
    
    #print(fz_df)
    
    # 资产负债表
    fig, axes = plt.subplots(nrows=2, ncols=1)
    zp = zc_df.plot(ax=axes[0], figsize=(8,6))
    zp.set_ylabel("资产总计")    
    fp = fz_df.plot(ax=axes[1], figsize=(8,6))
    fp.set_ylabel("负债合计")

    # 利润表
    yp = yyzsr_df.plot(figsize=(8,6))
    yp.set_ylabel("营业总收入")
    #jp = jlr_df.plot(ax=axes[1], figsize=(8,6))
    #jp.set_ylabel("净利润")
    