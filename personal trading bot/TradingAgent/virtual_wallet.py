import pandas as pd
import numpy as np


class VirtualWallet:
    def __init__(self, init_amount, file_loc):
        self.f_loc = file_loc
        self.i_amt = init_amount

        with open(self.f_loc, 'w') as file:
            file.write(str(self.i_amt))

    def credit(self, amount):
        init_amt = 0.0
        with open(self.f_loc, 'r') as file:
            init_amt = float(file.read())
        init_amt = init_amt + amount
        with open(self.f_loc, 'w') as file:
            file.write(str(init_amt))

    def debit(self, amount):
        init_amt = 0.0
        with open(self.f_loc, 'r') as file:
            init_amt = float(file.read())
        init_amt = init_amt - amount
        with open(self.f_loc, 'w') as file:
            file.write(str(init_amt))

    def show_balance(self):
        balance = None
        with open(self.f_loc, 'r') as file:
            balance = float(file.read())
        # print('Balance: ', balance)
        return balance

    # def reset(): ##This is so that all variables are reset to initial