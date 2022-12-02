import yfinance as yf
# All my helper functions. Needs to be refactored lmao

# Given the amount someone wants to spend and the stocks available.
# * Stocks should be ranked by purchase priority #
# return the optimal number of stocks to buy
def purchaseAmounts(investment_amount=0, stocks=None):
    if stocks is None:
        stocks = ["SWPPX"]
    if investment_amount == 0:
        return {}
