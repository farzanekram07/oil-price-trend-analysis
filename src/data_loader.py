import yfinance as yf

def load_oil_data():
	return yf.download("CL=F, period = 5y")
