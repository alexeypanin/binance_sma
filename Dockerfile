FROM python:3.7-slim-stretch

ADD calc.py /
ADD calc_moving_average.py /
ADD test_calc_moving_average.py /

RUN pip install pandas
RUN pip install python-binance

CMD [ "python", "./calc.py" ]

