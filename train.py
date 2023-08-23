def train_model(model, train_data, epochs=50, batch_size=1):
    # Train the model
    model.fit(train_data, epochs=epochs, batch_size=batch_size, verbose=2)
    return model