# Include all necessary external functions and classes
import os
class Container:
    #i should later on implement spread i.e the difference when buying and selling
    def __init__(self, curr_asset_price, wallet, init_wallet_amt, wallet_loc, exchange_fee=0.06):
        print('in init')
        self.exchange_fee = exchange_fee
        self.curr_asset_price = curr_asset_price
        self.wallet = wallet(init_wallet_amt, wallet_loc)
        # self.asset_price = None
        # self.asset_value = None

    def asset(self, operation, write_val=None):
        # This holds the asset bought and can read or write
        print('in asset')
        asset = None
        if operation == 'read':
            if os.path.exists('asset.txt'):
                with open('asset.txt', 'r') as file:
                    asset = file.read()
                    # print(asset)
            else:
                with open('asset.txt', 'w') as file:
                    empty = None
                    file.write(str(0))
                with open('asset.txt', 'r') as file:
                    asset = file.read()
                    # print('This is the asset amt: ', asset)
            return float(asset)
        if operation == 'write':
            with open('asset.txt', 'w') as file:
                file.write(str(write_val))
            return asset
        return None

    def validate_order(self, operation, asset_buy_worth=None, trans_currency=None, amt_asset_sell=None,
                       trans_fee_percent=0.6):  # The asset_buy_worth is in the coin worth
        print('in val_order')
        # exchange_fee
        # This checks if there's enough money in wallet to buy asset
        # Or checks if there's enough asset to sell
        if operation == 'buy':
            balance = float(self.wallet.show_balance())
            print('Balance: ', balance)
            # print("Debug: asset_buy_worth =", asset_buy_worth)
            # print("Debug: curr_asset_price =", self.curr_asset_price)
            # print("Debug: trans_fee_percent =", trans_fee_percent)
            #asset_converted = asset_buy_worth * self.curr_asset_price + asset_buy_worth * self.curr_asset_price * trans_fee_percent
            trans_amt = trans_currency + trans_currency * trans_fee_percent
            print('Transaction amount: ', trans_amt)
            if balance > trans_amt:
                return True
            else:
                return False

        if operation == 'sell':
            asset = float(self.asset(operation='read'))
            transaction_asset = amt_asset_sell + amt_asset_sell * trans_fee_percent
            print('Transaction asset: ', transaction_asset)
            print('Available Asset: ', asset)
            if asset > transaction_asset:
                return True
            else:
                return False

        if operation == 'hold':
            return True

        return None

    def exchange_buy(self, asset_buy_worth=0.02, trans_currency=7000):  # might later modify trabs_fee_percent to use self.exchange_fee
        print('in exch buy')
        # This executes the buy order
        trans_fee_percent = self.exchange_fee
        # print(trans_fee_percent)
        '''if self.validate_order('buy', asset_buy_worth=asset_buy_worth, trans_fee_percent=trans_fee_percent):
            trans_amt = asset_buy_worth * self.curr_asset_price + asset_buy_worth * self.curr_asset_price * trans_fee_percent
            self.wallet.debit(trans_amt) #debits the wallet to buy asset
            prev_amt = float(self.asset('read')) #gets the previous asset price before buying
            self.asset('write', write_val=prev_amt + asset_buy_worth) #updates the current asset price after being bought'''
        if self.validate_order('buy', asset_buy_worth=asset_buy_worth, trans_currency=trans_currency, trans_fee_percent=trans_fee_percent):
            trans_amt = trans_currency + trans_currency*trans_fee_percent
            self.wallet.debit(trans_amt)
            prev_amt = float(self.asset('read'))
            asset_bought = trans_currency/self.curr_asset_price
            self.asset('write', write_val=prev_amt + asset_bought)
        else:
            print('canceled buy... insufficient funds')
        return None

    def exchange_sell(self, amt_asset_sell=None):
        print('in exch sell')
        # This executes the sell order
        if amt_asset_sell == None:
            amt_asset_sell = 0.02 * self.asset('read')
        trans_fee_percent = self.exchange_fee
        if self.validate_order('sell', amt_asset_sell=amt_asset_sell, trans_fee_percent=trans_fee_percent):
            init_trans_amt = amt_asset_sell * self.curr_asset_price
            trans_amt = init_trans_amt + init_trans_amt * trans_fee_percent
            self.wallet.credit(init_trans_amt)
            prev_amt = float(self.asset('read'))
            self.asset('write', write_val=prev_amt - amt_asset_sell)
            '''if self.validate_order('sell', amt_asset_sell=amt_asset_sell, trans_fee_percent=trans_fee_percent):
            #calc asset to sell in asset figures
            trans_amt = amt_asset_sell * self.asset_value
            #convert or exchange the asset to normal price + transaction fees
            #trans_fee_in_asset = trans_fee_percent * trans_amt #This holds just the transaction fees in asset(i.e not converted yet)
            trans_fee = (trans_fee_percent * trans_amt * self.curr_asset_price)
            trans_amt = (trans_amt * self.curr_asset_price) + trans_fee
            #remove or debit the asset acct accordingly
            prev_amt = float(self.asset('read'))
            self.asset('write', write_val=prev_amt - trans_amt)
            #credit the wallet acoordingly minus the transaction fees
            self.wallet.credit(trans_amt-trans_fee)'''
        else:
            print('canceled sell... insufficient asset')
        return None

    def exchange_hold(self):
        print('in hold')
        # this does nothing
        return None

    #def reset(): ##This is so that all variables are reset to initial

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


class VirtualExchanger:
    def __init__(self, wallet, deduction_perc):
        self.wallet = wallet
        self.ded_perc = deduction_perc
        self.asset_price = None
        self.asset_value = None

    def buy(self, amount, ticker_price):
        def asset_val(self):
            # This is the particular asset value in the coin currency after buy
            # it shouldnt be used to determine asset value after sell has occurred
            # it shouldnt be run after sell only within buy
            ticker = None
            with open('buy_ticker.txt', 'r') as file:
                ticker = file.read()
            self.asset_value = float(self.asset_price) / float(ticker)
            print('Asset Value : ', self.asset_value)

        self.asset_price = amount - amount * self.ded_perc
        wallet.debit(amount)
        with open('buy_ticker.txt', 'w') as file:
            file.write(str(ticker_price))
        asset_val(self)

    def sell(self, asset_amount, curr_ticker):
        if asset_amount <= self.asset_value:
            self.asset_value = self.asset_value - asset_amount
        else:
            print('overdue so selling all!!')
            asset_amount = self.asset_value
            self.asset_value = 0
        sold = (asset_amount * curr_ticker) - (asset_amount * curr_ticker) * self.ded_perc
        wallet.credit(sold)

    def view_asset_value(self):
        print('The current asset value is: ', self.asset_value)

    def walletBalance(self):
        print(wallet.show_balance())