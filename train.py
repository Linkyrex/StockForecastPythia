def train_model(model, train_data, train_labels, epochs=50, batch_size=1):
    model.fit(train_data, train_labels, epochs=epochs, batch_size=batch_size, verbose=2)
    return model