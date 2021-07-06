import pandas
import datetime as dt
from binance.client import Client

class CalcMovingAverage:
    API_KEY  = 'rMtSznZGSwqA4yuazJBlb1iQCLFjHpWr5Enzr4hcVkT248vP7kDXYxPcww9CEC1x'
    API_SECRET = 'i7bVvkw8cR0O2AM5RUoGJNdrJccOX2ljdTkxcYihjDxc9cLA8X0UAhaT9rFgPQbv'

    CANDLE_INTERVAL = '1m'
    CLOSED_VALUE_INDEX = 4 
    CLOSED_TIME_INDEX = 6
    MOVING_AVERAGE_WINDOW = 5

    api_client = Client(API_KEY, API_SECRET)

    def __init__(self, ticker):
        self.ticker = ticker

    def call(self):
        """
        Getting candles from binance, calculating moving averages and displaying results
        """
        data = self.__fetch_candles()
        data['SMA'] = data.iloc[:,1].rolling(window=self.MOVING_AVERAGE_WINDOW).mean()

        self.__display(data)
        return data

    def __fetch_candles(self):
        """ fetching binance candles and return table of closing values and time"""
        try:
            candles = self.api_client.get_klines(symbol=self.ticker,
                                                 interval=self.CANDLE_INTERVAL)

            values = [float(c[self.CLOSED_VALUE_INDEX]) for c in candles]

            timeline = [c[self.CLOSED_TIME_INDEX]/1000 for c in candles]
            timeline = [dt.datetime.fromtimestamp(t).strftime('%H:%M') for t in timeline]

            return pandas.DataFrame({'Time': timeline, 'Close value': values})
        except Exception as e:
            print("Error during fetching candles for {}: {}".format(self.ticker, e))
            return pandas.DataFrame({'Time': [], 'Close value': []})

    def __display(self, table): 
        print('\n Moving average for {} \n'.format(self.ticker))
        print(table.tail(30))