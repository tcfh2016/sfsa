import tkinter as tk
import akshare as ak

def query():
    stock = stock_entry.get()
    if stock.isnumeric():
        stock_individual_info_em_df = ak.stock_individual_info_em(symbol="000001")
        print(stock_individual_info_em_df)
        label_info['text'] = stock_individual_info_em_df

        for i in range(len(stock_individual_info_em_df)):
            for j in range(2):
                e = tk.Entry(master=label_info, relief=tk.GROOVE)
                e.grid(row=i, column=j, sticky="nsew")
                e.insert(tk.END, f"{stock_individual_info_em_df.iloc[i][j]}")

    else:
        stock_zh_ah_name_df = ak.stock_zh_ah_name()
        print(stock_zh_ah_name_df)

window = tk.Tk()
window.title("Stock Financial Sheet Analyzer")
window.rowconfigure([0], minsize=100, weight=1)
window.rowconfigure([1], minsize=300, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

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

info_frame = tk.Frame(master=window)
info_frame.grid(row=1, column=0, sticky="n")

label = tk.Label(master=info_frame, text="股票信息")
label.grid(row=0, column=0, sticky="n")
label_info = tk.Label(master=info_frame, text="")
label_info.grid(row=1, column=0)

window.mainloop()