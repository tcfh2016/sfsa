import numpy as np

class Irr(object):
    def __init__(self, capital, periods, rate, penalty):
        self._capital = capital
        self._periods = periods
        self._rate = rate
        self._penalty = penalty

    def calc_irr(self):
        capital_per_period = self._capital / self._periods
        fee_per_period = self._capital * self._rate
        payment_per_period = -(capital_per_period + fee_per_period)

        for i in range(self._periods):
            rest_pay = self._capital - i*capital_per_period + self._penalty
            cash_flow = [self._capital] + [payment_per_period] * i + [-rest_pay]
            print("After {0} months, already paid {1}, need to pay {2:.2f}, IRR={3:.2%}"
                  .format(i, i*payment_per_period, -rest_pay, np.irr(cash_flow)*12))

    def run(self):
        print("start running irr...")
        self.calc_irr()
        #np.irr()
