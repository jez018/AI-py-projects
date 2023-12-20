# TODO This is where the initialization and interaction is begun

import container_exchange, virtual_wallet
from container_exchange import Container
from virtual_wallet import VirtualWallet
from agent2 import Agent
import numpy as np

####Test 001
'''
env = Container(10, VirtualWallet, 1000, 'wallet.txt')
env.exchange_buy()
env.exchange_sell()
env.exchange_hold()
env.asset('read')
env.validate_order(operation='buy', asset_buy_worth=100, amt_asset_sell=None)
'''
'''
#### Test 002 run time
#credit the acct with 10K
env = Container(10, VirtualWallet, 10000, 'wallet02.txt')
#buy 4 of assets at 1000 per unit
print('point 1')
env.curr_asset_price = 1000
env.exchange_buy(trans_currency=4000)
#sell 3 of assets at 700 per unit
print('point 2')
env.curr_asset_price = 700
env.exchange_sell(amt_asset_sell=3)
#buy 2 of assets at 920 per unit
print('point 3')
env.curr_asset_price = 920
env.exchange_buy(trans_currency=920)
env.exchange_buy(trans_currency=920)
#sell 3 of assets at 1200 per unit
print('point end')
env.curr_asset_price = 1200
env.exchange_sell(amt_asset_sell=3)

### Test 003 runtime logic
#credit acct with 1K
#buy 1 of assets at 700 per unit
#sell 1 of assets at 900 per unit
#buy 1 of assets at 2000 per unit  # expect insufficient funds here
#buy 2 of assets at 1000 per unit # expect insufficient funds here
#buy 1 of assets at 1100 per unit # expect trade to go through
#sell 1 of assets at 2000 per unit
#buy 2 of assets at 1500 per unit # expect trade to go through
'''
from market_simulation import MarketSimul
from container_exchange import Container, VirtualWallet

v_wallet = VirtualWallet
print('wallet: ', v_wallet)
cont = Container(100, v_wallet, 1000.0, 'wallet3.txt')
print('End of cont test.... And  begining market simul initialization')
env_2 = MarketSimul(cont.wallet)
print('End of market simul init... And begining of Agent init')
agent = Agent(state_size=33) #Instantiating and initializing the AI
print('end of Agent init')
eval_days = 1

'''for i in range(eval_days):
    print(env_2.simulate_output(env_2.data)[0])
    #date, state = np.array(env_2.simulate_output(env_2.data)[0]), np.array(env_2.simulate_output(env_2.data)[1:])
    #print(np.array(env_2.simulate_output(env_2.data)[1:].size))
    #state = state.astype(np.float32)
    #print(state)
    #act = agent.act(state)
    #print(act)
    print('-----------------------------------------------------')'''
for i in range(eval_days):
    state, reward = env_2.simulate_output(env_2.data)
    state = state[1:].astype(float) #putting [1:] removes the date in the data
    print('Agent taking action...')
    act = agent.act(state)
    print('action: ', act)

