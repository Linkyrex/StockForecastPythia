# Select 'Close' price for prediction
data = data[['Close']]

# Handle missing data
data = data.dropna()

# Normalize the data
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))
data = scaler.fit_transform(data)