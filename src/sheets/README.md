## Report Analyzing Functionalities Design

Different functionalities are applied to the analysis of different sheets: balance
sheet, income statement and cash flow statement, there are some common operations
among them, such as reading and processing data from csv files, so `inheritance`
is used here.

- Abstract class `analyzer` is base class to complete the data reading and cleaning
from .csv files.
- Derives classes `balance` and `income` take responsible for balance sheet analysis
and income statement analysis separatly.
- Class `balance` and `income` are composed into `ReportAnalyzer` which can do
complex calculation and comparison with data in other classes.

income 营业总收入显示有问题。