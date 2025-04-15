import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Create date range for the past year
end_date = datetime.now().date()
start_date = end_date - timedelta(days=365)
dates = pd.date_range(start=start_date, end=end_date, freq='B')  # Business days

# Generate sample data
n_samples = len(dates)
tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'META']
data = []

for ticker in tickers:
    # Generate random price movements
    base_price = np.random.uniform(50, 500)
    daily_returns = np.random.normal(0.0005, 0.015, n_samples)
    prices = [base_price]
    
    for ret in daily_returns:
        prices.append(prices[-1] * (1 + ret))
    prices = prices[1:]  # Remove the initial base price
    
    # Generate volume
    avg_volume = np.random.randint(1000000, 10000000)
    volumes = np.random.normal(avg_volume, avg_volume/5, n_samples).astype(int)
    
    # Create data entries
    for i in range(n_samples):
        data.append({
            'date': dates[i],
            'ticker': ticker,
            'open': round(prices[i] * (1 - np.random.uniform(0, 0.005)), 2),
            'high': round(prices[i] * (1 + np.random.uniform(0, 0.01)), 2),
            'low': round(prices[i] * (1 - np.random.uniform(0, 0.01)), 2),
            'close': round(prices[i], 2),
            'volume': max(0, volumes[i]),
            'pe_ratio': round(np.random.uniform(10, 40), 2),
            'dividend_yield': round(np.random.uniform(0, 0.03), 4),
            'market_cap': round(prices[i] * avg_volume * np.random.uniform(5, 15), 0)
        })

# Create DataFrame
df = pd.DataFrame(data)

# Save as parquet
df.to_parquet('finance.parquet', index=False)

print(f"Created finance.parquet with {len(df)} rows of data")