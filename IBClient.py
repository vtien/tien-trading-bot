from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from TradingBot import *

class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

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

    def historicalData(self, reqId, bar):
        print(f'Time: {bar.date} Close: {bar.close}')

    def historicalDataEnd(self, reqId: int, start: str, end: str):
        return super().historicalDataEnd(reqId, start, end)
    
    def historicalDataUpdate(self, reqId: int, bar):
        return super().historicalDataUpdate(reqId, bar)


if __name__ == "__main__":

    app = IBapi()
    app.connect('127.0.0.1', 7496, 123)
    app.run()

'''
#Uncomment this section if unable to connect
#and to prevent errors on a reconnect
import time
time.sleep(2)
app.disconnect()
'''