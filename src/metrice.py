def calculate_daily_return(wti):
	wti['daily_return'] = wti['close'].pct_change()
	return wti