import tkinter as tk
import akshare as ak
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_eva():    
    indicator_dfs = []
    for ind in ['总市值', '市盈率(TTM)', '市净率']:
        df = ak.stock_zh_valuation_baidu(symbol='603259', indicator=ind, period='全部')
        df = df.set_index('date').rename(columns={'value':ind})
        indicator_dfs.append(df)
    df = pd.concat(indicator_dfs, axis=1)
    print(df.sample(5))

    plt.rcParams['font.family']=['STFangsong']
    figure = plt.figure(figsize=(8, 4), dpi=100)
    canvas = FigureCanvasTkAgg(figure, window)
    canvas.get_tk_widget().grid(row=0, column=1, rowspan=2)

    ax1 = figure.add_subplot(1, 1, 1)
    plt.plot(df.index, df['总市值'], label='总市值')
    plt.legend(loc=0, fontsize="x-large")

    ax2 = ax1.twinx()
    plt.plot(df.index, df['市盈率(TTM)'], label='市盈率(TTM)')
    plt.plot(df.index, df['市净率'], label='市净率')
    plt.legend(loc=8)

def query():
    stock = stock_entry.get()
    if stock.isnumeric():
        stock_individual_info_em_df = ak.stock_individual_info_em(symbol="000001")
        print(stock_individual_info_em_df)
        label_info['text'] = stock_individual_info_em_df

        for i in range(len(stock_individual_info_em_df)):
            for j in range(2):
                e = tk.Entry(master=label_info, relief=tk.GROOVE)
                e.grid(row=i, column=j, sticky="ew")
                e.insert(tk.END, f"{stock_individual_info_em_df.iloc[i, j]}")

        plot_eva()
    else:
        stock_zh_ah_name_df = ak.stock_zh_ah_name()
        print(stock_zh_ah_name_df)

window = tk.Tk()
window.title("Stock Financial Sheet Analyzer")
window.rowconfigure([0], minsize=100, weight=1)
window.rowconfigure([1], minsize=300, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# 左侧列：按钮区
option_frame = tk.Frame(master=window)
option_frame.grid(row=0, column=0, sticky="n")

stock_entry = tk.Entry(master=option_frame, width=15)
stock_entry.grid(row=0, column=0, sticky="e")
info_button = tk.Button(master=option_frame, text="估值信息", width=15, command=query)
info_button.grid(row=0, column=2, sticky="w")
zcfzb_button = tk.Button(master=option_frame, text="资产负债表分析", width=15)
zcfzb_button.grid(row=1, column=0, sticky="w")
lrb_button = tk.Button(master=option_frame, text="利润表分析", width=15)
lrb_button.grid(row=1, column=1, sticky="w")
xjllb_button = tk.Button(master=option_frame, text="现金流量表分析", width=15)
xjllb_button.grid(row=1, column=2, sticky="w")

# 左侧列：信息区
info_frame = tk.Frame(master=window)
info_frame.grid(row=1, column=0, sticky="n")

label = tk.Label(master=info_frame, text="股票信息")
label.grid(row=0, column=0, sticky="n")
label_info = tk.Label(master=info_frame, text="")
label_info.grid(row=1, column=0)

# 分割线
separator = ttk.Separator(master=window, orient='vertical')
separator.grid(row=0, column=1, rowspan=2, sticky="nswe")

# 右侧列：估值区

window.mainloop()