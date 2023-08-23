# Predict stock prices
predicted_price = model.predict(test)
predicted_price = scaler.inverse_transform(predicted_price)

# Evaluate model
import math
from sklearn.metrics import mean_squared_error
rmse = math.sqrt(mean_squared_error(test, predicted_price))
print('RMSE: ', rmse)