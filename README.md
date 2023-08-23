# StockForecastPythia

This project is a simple stock price predictor using Machine Learning, specifically an LSTM model. The project fetches historical stock data, processes it, trains a model on this data, and then uses this model to predict stock prices. This code was generated using GPT4.

![Alt text](/Figure_1.png)
## Development Status

This project is currently in development. 

## Instructions

1. Fetch Stock Data: Use Python's `yfinance` library to fetch historical stock data from Yahoo Finance API.
2. Data Processing: Clean and process the data for model training.
3. Build Model: Use a simple LSTM model for prediction.
4. Train Model: Split the data into training and testing sets and train the model.
5. Predict & Evaluate: Use the model to predict stock prices and evaluate its performance.

## Setup

To set up the project:

1. Create a virtual environment: `python3 -m venv env`
2. Activate the virtual environment: `source env/bin/activate`
3. Install requirements: `pip install -r requirements.txt`

## File Structure

- `data_fetch.py`: Fetches stock data.
- `data_processing.py`: Handles data cleaning, processing, and normalization.
- `model.py`: Defines the LSTM model for prediction.
- `train.py`: Responsible for splitting the data and training the model.
- `predict_evaluate.py`: Predicts stock prices using the trained model and evaluates its performance.
- `main.py`: The entry point of the project, orchestrating the execution of other files.

## .gitignore

A `.gitignore` file is included to exclude the virtual environment and other unnecessary files from version control.

## Contributions

As this project is in development, contributions are welcome. Please feel free to fork the repository and submit pull requests.

Please note: This project is intended as a demonstration for a Software Engineer position at Sertis AI Asset Management and is not intended for real-world trading.
