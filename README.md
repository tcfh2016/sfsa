`stock-toolbox` is not one specified software，and no specified design purpose for
this project, it is a learning practice for stock analyzing.

This project is pure `python` and support the following basic functionalities:

- Trade Analysis
  - Pick up minimum price/maximum print from given trade records (by month)
  - Store the result to .csv file
  - Plotting

- Financial Statement Analysis
  - For single stock
    - common-size analysis, assert estimation from balance sheet and store result
      in .csv file
    - profit estimation from income statement and store result in .csv file
    - Plotting    
  - For multiply stocks

Some reminders:

- The script is developed under `Windows` and only `A stocks` as objects.
- Remember change to `...\stock-toolbox\src` which is used for working directory.
- Raw data is needed before running analysis script:
  - for trade analysis, copy raw data file into `.\data\trade`
  - for report analysis, copy raw data file into `.\data\report`

# 1 Trade Analysis

目前仅支持单只股票的交易记录分析，如果在命令中传入了多只股票编码，默认处理第一只股票。

- 得出基于月份的最低、最高价

```
python start.py -s 002352 --option trade
```

- 指定交易时间段

```
python start.py -s 002352 -o trade --startdate 201501 --enddate 201808
```

# 2 Report Analysis

## 2.1 Single Stock

### Balance Sheet

当前仅支持同型分析（比率分析），输出结果：

  - 资产部分同型分析（图示）
  - 负债部分同型分析（图示）
  - 资产评估csv文件

```
python start.py -o balance -s 002352
```

### Income Statement

当前仅支持同型分析（比率分析），输出结果：

  - 利润表同型分析（图示）  
  - 资产评估csv文件

```
python start.py -s 002352 -o income
```

## 2.2 Multiply Stock

在对多只股票进行对比分析的时候，默认以最近一个会计年度的报表数据进行对比。目前支持针对多
只股票的资产负债表项目和利润表项目进行对比，绘制图形从绝对值和百分比两个角度进行展现。

### 资产负债表对比

```
python start.py -s 002352 600233 -o balance
```

![](muti_stock_asset.png)

### 利润表对比

```
python start.py -s 002352 600233 -o income
```

![](muti_stock_income.png)
