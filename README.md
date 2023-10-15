## 简介

`financial-sheet-analyzer`是一个 `python`练习项目，它提供了对于财务报表的一些初步的数据分析，主要包括以下几个部分的功能：

1. 交易分析：提取按月的最大值、最小值，并绘图，同时将其保存在.csv文件中。
2. 财报分析：
  - 对于单只股票的数据，对资产负债表进行共同分析，利润表进行趋势分析，并绘图。
  - 对于单只股票的数据，提供对于多只股票的对比。

## 提示

- `...\financial-sheet-analyzer\src` 作为工作目录，所以需要切换到该目录下执行`start.py`
- 使用该脚本之前必须先准备好原始数据表:对于交易分析，将交易数据放到`.\data\trade`目录下，对于财报分析，原始数据放到`.\data\report`。

*后续可以考虑支持在线爬取数据。*

## 使用说明

1）交易分析

当前仅支持单只股票的交易分析，执行如下命令开始分析：

```
python start.py -s 002352 --option trade
```

指定交易数据的时间范围：

```
python start.py -s 002352 -o trade --startdate 201501 --enddate 201808
```

2）财报分析 —— 单只股票

- 资产负债表

```
python start.py -o balance -s 000898
```

执行以上命令可以看到两幅图：资产和负债的共同分析图，以及当前资产状况：


![](./src/report/doc/balance_asset_liability.png)

![](./src/report/doc/current_asset.png)


- 利润表

```
python start.py -s 002352 -o income
```

执行以上命令进行利润表的分析，针对利润表没有使用共同分析，而是包括了“营收趋势”和“费用趋势”:


![](./src/report/doc/income_analysis.png)


- 现金流量表

```
python start.py -s 002352 -o income
```

现金流量表的分析包括：现金净流入趋势

![](./src/report/doc/cash_flow_analysis.png)

现金流和资产负债表的对比

![](./src/report/doc/cash_flow_analysis_balance_items.png)


2）财报分析 —— 多只股票


在对多只股票进行对比分析的时候，默认以最近一个会计年度的报表数据进行对比。目前支持针对多只股票的资产负债表项目和利润表项目进行对比，绘制图形从绝对值和百分比两个角度进行展现。

- 资产负债表对比

```
python start.py -s 002352 600233 -o balance
```

![](muti_stock_asset.png)

- 利润表对比

```
python start.py -s 002352 600233 -o income
```

![](muti_stock_income.png)


## CHANGE LOG

- 231010：网易163的股票数据源不再可用，准备切换到AKSHARE。