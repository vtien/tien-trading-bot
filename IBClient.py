from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from TradingBot import *

class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.data = []

    def error(self, reqId, code, msg):
        '''Logging Error'''
        print(f"Error {reqId}, code: {code}, message: {msg}")        

    def tickPrice(self, reqId, tickType, price, attrib):
        if tickType == 2 and reqId == 1:
            print('The current ask price is: ', price)

    def realtimeBar(self, reqId, time: int, open_: float, high: float, low: float, close: float, volume: int, wap: float, count: int):
        # return super().realtimeBar(reqId, time, open_, high, low, close, volume, wap, count)
        super().realtimeBar(reqId, time, open_, high, low, close, volume, wap, count)
        try:
            bot = TradingBot()
            bot._stream_bar_data(reqId, time, open_, high, low, close, volume, wap, count)
        except Exception as e:
            print(e)

    def historicalData(self, reqId, bar) -> None:
        print(f'Time: {bar.date} Close: {bar.close} Volume: {bar.volume}')
        self.data.append({"time": bar.date, "close": bar.close, "volume": bar.volume})

    def historicalDataEnd(self, reqId: int, start: str, end: str):
        return super().historicalDataEnd(reqId, start, end)
    
    def historicalDataUpdate(self, reqId: int, bar):
        return super().historicalDataUpdate(reqId, bar)