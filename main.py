from data_fetch import get_data
from data_processing import process_data
from model import build_model
from train import train_model
from predict_evaluate import predict_and_evaluate
from plot_predictions import plot_predictions

import subprocess

def main():
    try:
        # Fetch data
        data = get_data('AAPL','2020-01-01','2022-01-01')

        # Process data
        train_data, train_labels, test_data, test_labels, scaler = process_data(data)

        # Build model
        model = build_model()

        # Train model
        model = train_model(model, train_data, train_labels)

        # Predict and evaluate
        predict_and_evaluate(model, test_data, test_labels, scaler)

        model = train_model(model, train_data, train_labels)
        predicted_price = model.predict(test_data)
        predict_and_evaluate(model, test_data, test_labels, scaler)
        plot_predictions(test_labels, predicted_price, scaler)


    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()