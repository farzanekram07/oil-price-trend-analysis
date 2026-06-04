import pandas as pd


def calculate_daily_return(df):
    """
    Calculate daily percentage returns.
    """
    return df["Close"].pct_change()

def rolling_volatility(returns, window=20):
    """
    Rolling standard deviation of returns.
    """
    return returns.rolling(window=window).std()

def moving_average(series, window):
    """
    Calculate moving average.
    """
    return series.rolling(window=window).mean()

def calculate_drawdown(close_price):

    running_peak = close_price.cummax()

    drawdown = (
        close_price - running_peak
    ) / running_peak

    return drawdown

