#TODO This is where and how the agent interacts with the exchange and wallet
from container_exchange import Container
from virtual_wallet import VirtualWallet

wallet = VirtualWallet(10000.0, 'wallet.txt')
container = Container(0.06, 10000.0, wallet, 10000.0, 'wallet.txt')
#init env which is the states grouped together into various grouped states each as 30 days

def interact(env, wallet, exchange, agent, num_episodes=2000, window=100, reward=-1):
    env.start()
    for i_episode in range(num_episodes):
        episode = env.step()
        container.reset() #to be implemented #This is so that all variables are reset and ready for next episode
        wallet.reset() #to be implemented ##This is so that all variables and amounts are reset and ready for next episode
        for state, n_state, in episode: #n_state here means next_state
            action = agent.select_action(state)
            # 0 is buy, 1 is hold and 2 is sell
            if action == 0:
                container.exchange_buy(0.05)
            if action == 1:
                container.exchange_hold()
            if action == 2:
                container.exchange_sell(0.3)
            if wallet.show_balance() > 19800.0:
                reward = 10
            if wallet.show_balance() < 19800.0 and wallet.show_balance() > 10990.0:
                reward = 0
            if wallet.show_balance() < 10990.0:
                reward = -1
            done = True if i_episode == num_episodes else False
            agent.step(state, action, n_state, reward, done)