import yfinance as yf
import pandas as pd


def load_wti_data(
    ticker="CL=F",
    period="5y",
    auto_adjust=False
):
    
    df = yf.download(
        ticker,
        period=period,
        auto_adjust=auto_adjust
    )

    return df