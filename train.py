# Split data into train and test sets
train_size = int(len(data) * 0.80)
train, test = data[0:train_size, :], data[train_size:len(data), :]

# Train the model
model.fit(train, epochs=50, batch_size=1, verbose=2)