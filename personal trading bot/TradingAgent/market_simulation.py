
import pandas as pd
import numpy as np

class MarketSimul:
    def __init__(self, wallet):
        self.counter = 0
        self.table_count = 0
        self.data = self.generate_table()
        self.simulate_output(self.data)

        self.prev_table_count = 0

        self.wallet = wallet
        self.initial_wallet_balance = wallet.show_balance()
        pass
    def generate_table(self):

        #####################################################################
        # Convert date
        '''def to_strftime(self, df):
            date = datetime.strptime(df, '%b %d, %Y')
            return date.strftime("%Y-%m-%d")'''

        # df_btc['Date'] = df_btc['Date'].apply(lambda x: to_strftime(x))
        # df_btc = df_btc.sort_values('Date').reset_index(drop=True)

        def yest():
            df_btc['yest_close'] = 0.0
            for i in range(len(df_btc)):
                if i > 0:
                    df_btc.at[i, 'yest_close'] = df_btc['Close'][i - 1]

        def tomo():
            df_btc['tomo_price'] = 0.0
            for i in range(len(df_btc) - 1):
                df_btc.at[i, 'tomo_price'] = df_btc['Close'][i + 1]

        def sma10():
            df_btc['sma10'] = 0.0
            for i in range(len(df_btc)):
                if i > 8:
                    df_btc.at[i, 'sma10'] = (df_btc['Close'][i] + df_btc['Close'][i - 1] + df_btc['Close'][i - 2] +
                                             df_btc['Close'][i - 3] + df_btc['Close'][i - 4] + df_btc['Close'][i - 5] +
                                             df_btc['Close'][i - 6] + df_btc['Close'][i - 7] + df_btc['Close'][i - 8] +
                                             df_btc['Close'][i - 9]) / 10

        def sma5():
            df_btc['sma5'] = 0.0
            for i in range(len(df_btc)):
                if i > 3:
                    df_btc.at[i, 'sma5'] = (df_btc['Close'][i] + df_btc['Close'][i - 1] + df_btc['Close'][i - 2] +
                                            df_btc['Close'][i - 3] + df_btc['Close'][i - 4]) / 5

        def sma4():
            df_btc['sma4'] = 0.0
            for i in range(len(df_btc)):
                if i > 2:
                    df_btc.at[i, 'sma4'] = (df_btc['Close'][i] + df_btc['Close'][i - 1] + df_btc['Close'][i - 2] +
                                            df_btc['Close'][i - 3]) / 4

        def sma3():
            df_btc['sma3'] = 0.0
            for i in range(len(df_btc)):
                if i > 1:
                    df_btc.at[i, 'sma3'] = (df_btc['Close'][i] + df_btc['Close'][i - 1] + df_btc['Close'][i - 2]) / 3

        def sma2():
            df_btc['sma2'] = 0.0
            for i in range(len(df_btc)):
                if i > 0:
                    df_btc.at[i, 'sma2'] = (df_btc['Close'][i] + df_btc['Close'][i - 1]) / 2

        def ema5():
            prevEma = None
            df_btc['ema5_today'] = 0
            for i in range(len(df_btc)):
                if i > 3:
                    if prevEma == None:
                        prevEma = (df_btc['Close'][i] + df_btc['Close'][i - 1] + df_btc['Close'][i - 2] +
                                   df_btc['Close'][i - 3] + df_btc['Close'][i - 4]) / 5
                    ema = df_btc['Close'][i] * (2 / (1 + 5)) + prevEma * (1 - (2 / (1 + 5)))
                    df_btc.at[i, 'ema5_today'] = ema
                    # if ema > df_btc['Close'][i]:
                    #    df_btc.at[i, 'ema5_today'] = 1
                    prevEma = ema

        def ema5against():
            prevEma = None
            df_btc['ema5_against_prevEma'] = 0
            for i in range(len(df_btc)):
                if i > 3:
                    if prevEma == None:
                        prevEma = (df_btc['Close'][i] + df_btc['Close'][i - 1] + df_btc['Close'][i - 2] +
                                   df_btc['Close'][i - 3] + df_btc['Close'][i - 4]) / 5
                    ema = df_btc['Close'][i] * (2 / (1 + 5)) + prevEma * (1 - (2 / (1 + 5)))
                    if ema > prevEma:
                        df_btc.at[i, 'ema5_against_prevEma'] = 1
                    prevEma = ema

        def ema10():
            prevEma = None
            df_btc['ema10_today'] = 0
            for i in range(len(df_btc)):
                if i > 8:
                    if prevEma == None:
                        prevEma = (df_btc['Close'][i] + df_btc['Close'][i - 1] + df_btc['Close'][i - 2] +
                                   df_btc['Close'][i - 3] + df_btc['Close'][i - 4] + df_btc['Close'][i - 5] +
                                   df_btc['Close'][i - 6] + df_btc['Close'][i - 7] + df_btc['Close'][i - 8] +
                                   df_btc['Close'][i - 9]) / 10
                    ema = df_btc['Close'][i] * (2 / (1 + 10)) + prevEma * (1 - (2 / (1 + 10)))
                    df_btc.at[i, 'ema10_today'] = ema
                    # if ema > df_btc['Close'][i]:
                    #    df_btc.at[i, 'ema5_today'] = 1
                    prevEma = ema

        def ema10against():
            prevEma = None
            df_btc['ema10_against_prevEma'] = 0
            for i in range(len(df_btc)):
                if i > 8:
                    if prevEma == None:
                        prevEma = (df_btc['Close'][i] + df_btc['Close'][i - 1] + df_btc['Close'][i - 2] +
                                   df_btc['Close'][i - 3] + df_btc['Close'][i - 4] + df_btc['Close'][i - 5] +
                                   df_btc['Close'][i - 6] + df_btc['Close'][i - 7] + df_btc['Close'][i - 8] +
                                   df_btc['Close'][i - 9]) / 10
                    ema = df_btc['Close'][i] * (2 / (1 + 5)) + prevEma * (1 - (2 / (1 + 5)))
                    if ema > prevEma:
                        df_btc.at[i, 'ema10_against_prevEma'] = 1
                    prevEma = ema

        def db4_yest():
            df_btc['db4yest_close'] = 0.0
            for i in range(len(df_btc)):
                if i > 1:
                    df_btc.at[i, 'db4yest_close'] = df_btc['Close'][i - 2]

        def two_db4_yest():
            df_btc['two_db4yest_close'] = 0.0
            for i in range(len(df_btc)):
                if i > 2:
                    df_btc.at[i, 'two_db4yest_close'] = df_btc['Close'][i - 3]

        def three_db4_yest():
            df_btc['three_db4yest_close'] = 0.0
            for i in range(len(df_btc)):
                if i > 3:
                    df_btc.at[i, 'three_db4yest_close'] = df_btc['Close'][i - 4]

        def today_yest():
            df_btc['today_yest'] = 0
            for i in range(len(df_btc)):
                if i > 0:
                    if df_btc['Close'][i] > df_btc['Close'][i - 1]:
                        df_btc.at[i, 'today_yest'] = 1

        def sma10_against_yest():
            df_btc['sma10_against_yest'] = 0
            for i in range(len(df_btc)):
                if df_btc['sma10'][i] > df_btc['Close'][i]:
                    df_btc.at[i, 'sma10_against_yest'] = 1

        def sma5_against_yest():
            df_btc['sma5_against_yest'] = 0
            for i in range(len(df_btc)):
                if df_btc['sma5'][i] > df_btc['Close'][i]:
                    df_btc.at[i, 'sma5_against_yest'] = 1

        def sma4_against_yest():
            df_btc['sma4_against_yest'] = 0
            for i in range(len(df_btc)):
                if df_btc['sma4'][i] > df_btc['Close'][i]:
                    df_btc.at[i, 'sma4_against_yest'] = 1

        def sma2_against_yest():
            df_btc['sma2_against_yest'] = 0
            for i in range(len(df_btc)):
                if df_btc['sma2'][i] > df_btc['Close'][i]:
                    df_btc.at[i, 'sma2_against_yest'] = 1

        def ema5_against_yest():
            df_btc['ema5_against_yest'] = 0
            for i in range(len(df_btc)):
                if df_btc['ema5_today'][i] > df_btc['Close'][i]:
                    df_btc.at[i, 'ema5_against_yest'] = 1

        def ema10_against_yest():
            df_btc['ema10_against_yest'] = 0
            for i in range(len(df_btc)):
                if df_btc['ema10_today'][i] > df_btc['Close'][i]:
                    df_btc.at[i, 'ema10_against_yest'] = 1

        def db4_yest():
            df_btc['db4yest_close'] = 0.0
            for i in range(len(df_btc)):
                if i > 1:
                    df_btc.at[i, 'db4yest_close'] = df_btc['Close'][i - 2]

        def two_db4_yest():
            df_btc['two_db4yest_close'] = 0.0
            for i in range(len(df_btc)):
                if i > 2:
                    df_btc.at[i, 'two_db4yest_close'] = df_btc['Close'][i - 3]

        def three_db4_yest():
            df_btc['three_db4yest_close'] = 0.0
            for i in range(len(df_btc)):
                if i > 3:
                    df_btc.at[i, 'three_db4yest_close'] = df_btc['Close'][i - 4]

        def today_yest():
            df_btc['today_yest'] = 0
            for i in range(len(df_btc)):
                if i > 0:
                    if df_btc['Close'][i] > df_btc['Close'][i - 1]:
                        df_btc.at[i, 'today_yest'] = 1

        def today_db4_yest():
            df_btc['today_db4_yest'] = 0
            for i in range(len(df_btc)):
                if i > 1:
                    if df_btc['Close'][i] > df_btc['Close'][i - 2]:
                        df_btc.at[i, 'today_db4_yest'] = 1

        def sma10_against_yest():
            df_btc['sma10_against_yest'] = 0
            for i in range(len(df_btc)):
                if df_btc['sma10'][i] > df_btc['Close'][i]:
                    df_btc.at[i, 'sma10_against_yest'] = 1

        def sma5_against_yest():
            df_btc['sma5_against_yest'] = 0
            for i in range(len(df_btc)):
                if df_btc['sma5'][i] > df_btc['Close'][i]:
                    df_btc.at[i, 'sma5_against_yest'] = 1

        def sma4_against_yest():
            df_btc['sma4_against_yest'] = 0
            for i in range(len(df_btc)):
                if df_btc['sma4'][i] > df_btc['Close'][i]:
                    df_btc.at[i, 'sma4_against_yest'] = 1

        def sma3_against_yest():
            df_btc['sma3_against_yest'] = 0
            for i in range(len(df_btc)):
                if df_btc['sma3'][i] > df_btc['Close'][i]:
                    df_btc.at[i, 'sma3_against_yest'] = 1

        def sma2_against_yest():
            df_btc['sma2_against_yest'] = 0
            for i in range(len(df_btc)):
                if df_btc['sma2'][i] > df_btc['Close'][i]:
                    df_btc.at[i, 'sma2_against_yest'] = 1

        def ema5_against_yest():
            df_btc['ema5_against_yest'] = 0
            for i in range(len(df_btc)):
                if df_btc['ema5_today'][i] > df_btc['Close'][i]:
                    df_btc.at[i, 'ema5_against_yest'] = 1

        def ema10_against_yest():
            df_btc['ema10_against_yest'] = 0
            for i in range(len(df_btc)):
                if df_btc['ema10_today'][i] > df_btc['Close'][i]:
                    df_btc.at[i, 'ema10_against_yest'] = 1


        def db4yest_against_yest():
            df_btc['db4_against_yest'] = 0
            for i in range(len(df_btc)):
                if df_btc['db4yest_close'][i] > df_btc['yest_close'][i]:
                    df_btc.at[i, 'db4_against_yest'] = 1

        def two_db4yest_against_yest():
            df_btc['two_db4_against_yest'] = 0
            for i in range(len(df_btc)):
                if df_btc['two_db4yest_close'][i] > df_btc['yest_close'][i]:
                    df_btc.at[i, 'two_db4_against_yest'] = 1

        def three_db4yest_against_yest():
            df_btc['three_db4_against_yest'] = 0
            for i in range(len(df_btc)):
                if df_btc['three_db4yest_close'][i] > df_btc['yest_close'][i]:
                    df_btc.at[i, 'three_db4_against_yest'] = 1

        def tomo_against_yest():
            df_btc['tomo_against_yest'] = 0
            for i in range(len(df_btc)):
                if df_btc['tomo_price'][i] > df_btc['Close'][i]:
                    df_btc.at[i, 'tomo_against_yest'] = 1
        ######################################################################


        #a table would be created using the functions below
        df_btc = pd.read_csv(r'BTC-USD.csv')
        #df_btc = self.to_strftime(self, df)
        df_btc = df_btc.sort_values('Date').reset_index(drop=True)
        yest()
        tomo()
        sma2()
        sma3()
        sma4()
        sma5()
        sma10()

        ema5()
        ema5against()
        ema10()
        ema10against()
        db4_yest()
        two_db4_yest()
        three_db4_yest()
        today_yest()
        today_db4_yest()
        sma10_against_yest()
        sma5_against_yest()
        sma4_against_yest()
        sma3_against_yest()
        sma2_against_yest()
        ema5_against_yest()
        ema10_against_yest()

        db4yest_against_yest()
        two_db4yest_against_yest()
        three_db4yest_against_yest()
        tomo_against_yest()
        #print(df_btc)

        #what is left now is finding a way to add to the table the candle width or length by suing the formula: (H-L)/2, and to do that for 1 week i.e 7 days
        return df_btc

    def simulate_output(self, data):
        reward = self.generate_reward()  ##possible dislocation #This is responsible for generating reward after every count as well as considering acct balance
        if self.counter == 30:
            reward = self.generate_reward()  ##possible dislocation
            self.counter = 0
            self.table_count += 1
            self.initial_wallet_balance = self.wallet.show_balance()
        #reward = self.generate_reward()  ##possible dislocation #This is responsible for generating reward after every count as well as considering acct balance
        tables = self.partition_to_tables(data)
        #print('Tables')
        #print(tables[9])
        #print('-----------')
        output = np.array(tables[self.table_count].iloc[self.counter])
        self.counter += 1
        #print(output)
        return output, reward

    def partition_to_tables(self, df):
        chunks = [df[i:i+30].reset_index(drop=True) for i in range(0, len(df), 30)]

        #store the chunks as df in a list
        df_list = []
        for chunk in chunks:
            df_list.append(chunk)
        return df_list

    def generate_reward(self):
        if self.counter < 30:
            return -1
        else:
            if self.wallet.show_balance() - self.initial_wallet_balance > 80000.0:
                return 100
            else:
                return -50

    def binarydifference(self, first, second):
        pass
    def difference(self, first, second):


        pass



    def sma5aa(self): #do for 288 times
        #calculates using 1day table to create 5sma table
        #import 1day table of btc
        #add to the table 5sma_open, 5sma_high, 5sma_low, 5sma_close
        #del the predecessing columns and leave only the sma's
        #the new table should be the return
        pass
    def sma10aa(self): #do for 288 times
        # calculates using 10min table to create 5min sma table
        pass
    def sma15aa(self): #do for 288 times
        pass
    def sma1hr(self): #do for 288 times
        pass
    def sma5hr(self): #do for 288 times
        pass
    def sma1hr(self): #do for 288 times
        pass
    def ema5(self): #do for 288 times
        pass
    def ema10(self): #do for 288 times
        pass
    def ema15(self): #do for 288 times
        pass
    def ema1hr(self): #do for 288 times
        pass
    def ema5hr(self): #do for 288 times
        pass
    def ema15hr(self): #do for 288 times
        pass
    def wma5(self): #do for 288 times
        pass
    def wma10(self): #do for 288 times
        pass
    def wma15(self): #do for 288 times
        pass
    def wma1hr(self): #do for 288 times
        pass
    def wma5hr(self): #do for 288 times
        pass
    def wma15hr(self): #do for 288 times
        pass

    def priceVolTrend(self, first, second):
        #To check for how to calculate vol trend
        pass