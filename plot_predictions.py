import matplotlib.pyplot as plt

def plot_predictions(test_labels, predicted_price, scaler):
    test_labels_orig = scaler.inverse_transform(test_labels)
    predicted_price = scaler.inverse_transform(predicted_price)

    plt.figure(figsize=(10,6))
    plt.plot(test_labels_orig, color='blue', label='Actual Stock Price')
    plt.plot(predicted_price, color='red', label='Predicted Stock Price')
    plt.title('Stock Price Prediction')
    plt.xlabel('Time')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.show()
