''' Specify real or test and the trading strategy at the command line (make sure this is easy to deploy
on AWS in this manner) '''

from TradingBot import *

def main():

    test_bot = TradingBot()
    # test_bot.get_realtime_bar_data("AAPL")
    test_bot.get_historical_bar_data("AAPL")

if __name__ == "__main__":

    main()