import numpy as np
import matplotlib.pyplot as plt
import report.analyzer as analyzer


class CashflowStatementAnalyzer(analyzer.Analyzer):
    def __init__(self, file_name):
        analyzer.Analyzer.__init__(self, file_name)
        self.read_data()

        self.cashflow_df = np.NaN

    def prepare(self):
        pass

    def analyze(self):
        pass
