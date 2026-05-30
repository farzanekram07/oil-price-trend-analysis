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