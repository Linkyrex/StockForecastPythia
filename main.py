from data_fetch import get_data
from data_processing import process_data
from model import build_model
from train import train_model
from predict_evaluate import predict_and_evaluate

def main():
    try:
        # Fetch data
        data = get_data('AAPL','2020-01-01','2022-01-01')

        # Process data
        data = process_data(data)

        # Build model
        model = build_model()

        # Train model
        model = train_model(model, data)

        # Predict and evaluate
        predict_and_evaluate(model, data)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()