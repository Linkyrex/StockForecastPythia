import math
from sklearn.metrics import mean_squared_error

def predict_and_evaluate(model, test_data, test_labels, scaler):
    predicted_price = model.predict(test_data)
    predicted_price = scaler.inverse_transform(predicted_price)

    test_labels = scaler.inverse_transform(test_labels)

    rmse = math.sqrt(mean_squared_error(test_labels, predicted_price))
    print('RMSE: ', rmse)