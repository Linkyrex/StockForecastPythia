import math
from sklearn.metrics import mean_squared_error

def predict_and_evaluate(model, test_data, scaler):
    # Predict stock prices
    predicted_price = model.predict(test_data)
    predicted_price = scaler.inverse_transform(predicted_price)

    # Evaluate model
    rmse = math.sqrt(mean_squared_error(test_data, predicted_price))
    print('RMSE: ', rmse)