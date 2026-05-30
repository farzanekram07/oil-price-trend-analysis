import matplotlib.pyplot as plt


def plot_close_price(df):

    plt.figure(figsize=(12,5))

    plt.plot(df.index,
             df["Close"])

    plt.title(
        "WTI Closing Price"
    )

    plt.show()