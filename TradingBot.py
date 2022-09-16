from abc import ABC
from IBClient import IBapi
from ibapi.contract import Contract
import time
import threading
import datetime

class TradingBot(ABC):

    def __init__(self):
        self.app = IBapi()
        self.app.connect('127.0.0.1', 7496, 123) # url, socket port number, client id (just needs to be any unique number)

    def run_loop(self):
        self.app.run()

    def create_contract(self, ticker, secType, exchange, currency):
        """Create contract object"""
        
        contract = Contract()
        contract.symbol = ticker
        contract.secType = secType
        contract.exchange = exchange
        contract.currency = currency
        return contract

    def get_ticker_data(self, ticker: str, secType: str, exchange: str, currency: str):

        #Start the socket in a thread
        api_thread = threading.Thread(target=self.run_loop, daemon=True)
        api_thread.start()
        time.sleep(1) #Sleep interval to allow time for connection to server

        contract = self.create_contract()

        #Request Market Data
        self.app.reqMktData(1, contract, '', False, False, [])

        time.sleep(10) #Sleep interval to allow time for incoming price data
        self.app.disconnect()

    def _stream_bar_data(self, reqId, time: int, open_: float, high: float, low: float, close: float, volume: int, wap: float, count: int):
        print(close)

    def _get_historical_bar_data(self, reqId: int, bar):
        print(bar)

    def get_realtime_bar_data(self, ticker):
        contract = self.create_contract(ticker, "STK", "SMART", "USD")
        # params = self.app.reqRealTimeBars(0, contract, 5, "TRADES", 1, [])
        self.app.reqRealTimeBars(0, contract, 5, "TRADES", 1, [])

    def get_historical_bar_data(self, ticker):

        #Start the socket in a thread
        api_thread = threading.Thread(target=self.run_loop, daemon=True)
        api_thread.start()
        time.sleep(1) #Sleep interval to allow time for connection to server

        contract = self.create_contract(ticker, "CASH", "IDEALPRO", "USD")
        
        queryTime = (datetime.datetime.today() - datetime.timedelta(days=10)).strftime("%Y%m%d %H:%M:%S")
        self.app.reqHistoricalData(4102, contract, queryTime,
        "1 M", "1 day", "MIDPOINT", 1, 1, False, [])

        time.sleep(5)
        self.app.disconnect()

    def calculate_performance():

        return



class RealTradingBot(TradingBot):

    def buy():

        pass

    def sell():

        pass

class TestTradingBot(TradingBot):

    def buy():

        pass

    def sell():

        pass