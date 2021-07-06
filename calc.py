from calc_moving_average import CalcMovingAverage 

for ticker in [ 'BTCUSDT', 'ETHUSDT', 'BNBBTC' ]:
    CalcMovingAverage(ticker).call()