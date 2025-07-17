def maximumWealth(accounts):
    max_wealth = 0
    for i in range(len(accounts)):
        current_wealth = sum(accounts[i])
        if current_wealth > max_wealth:
            max_wealth = current_wealth
    return max_wealth
