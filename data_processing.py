from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def process_data(data, test_size=0.2):
    # Select 'Close' price for prediction
    data = data[['Close']]

    # Handle missing data
    data = data.dropna()

    # Normalize the data
    scaler = MinMaxScaler(feature_range=(0, 1))
    data = scaler.fit_transform(data)

    # Split data into train and test sets
    train_data, test_data = train_test_split(data, test_size=test_size, shuffle=False)

    return train_data, test_data, scaler