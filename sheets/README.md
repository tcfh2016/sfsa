## Finacial Sheet Analyzing Design

Different functionalities are applied to the analysis of different sheets: balance
sheet, income statement and cash flow statement, there are some common operations
among them, such as reading and processing data from csv files, so `inheritance`
is used here.

- Abstract class `Sheet` is base class to complete the data reading, the data source now is from `Akshare`, by calling `stock_financial_report_sina()` to return the history report data.
    - you can have yearly overview with diagram for three financial sheet by executing the sheet.py file only.
- Derives classes `ZcfzbAnalyzer`, `LrbAnalyzer` and `XjllbAnalyzer` take responsible for balance sheet, income statement and cash flow statement separately.
    - you can also have seasonly overview with diagram to run them separately.
- Diagram plot method for seasonly dimension is provided in `sheet.py`. 
