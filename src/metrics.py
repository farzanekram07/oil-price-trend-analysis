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

# Forecast Metrics Module
# This module provides functions to evaluate forecasting models using 
# common metrics like MAE and RMSE.
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error
)

import numpy as np


def evaluate_forecast(
    y_true,
    y_pred
):
    mae = mean_absolute_error(
        y_true,
        y_pred
    )

    rmse = np.sqrt(
        mean_squared_error(
            y_true,
            y_pred
        )
    )

    return {
        "MAE": mae,
        "RMSE": rmse
    }



# ARIMA Metrics Module
# This module provides functions to evaluate ARIMA model forecasts using
# metrics like AIC and BIC.
from statsmodels.tsa.arima.model import ARIMA


def fit_arima(
    train,
    order=(1,1,1)
):

    model = ARIMA(
        train,
        order=order
    )

    return model.fit()