from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def process_data(data, test_size=0.2):
    data = data[['Close']]
    data = data.dropna()

    scaler = MinMaxScaler(feature_range=(0, 1))
    data = scaler.fit_transform(data)

    train_size = int(len(data) * (1 - test_size))
    train_data = data[:train_size]
    test_data = data[train_size:]

    train_labels = train_data[1:]
    test_labels = test_data[1:]
    train_data = train_data[:-1]
    test_data = test_data[:-1]

    return train_data, train_labels, test_data, test_labels, scaler