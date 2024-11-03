import pandas as pd
import numpy as np
import config
from tensorflow import keras
from keras import layers
from keras import utils
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Get feature data in the csv extracted from dataset
csv = pd.read_csv(config.csv_path) 
features = csv.iloc[:, 1:len(csv.columns)-1]

# Normalize the data
mean = features.mean()
std = features.std()
features = ((features - mean) / std)

# Get labels and format them for the model
labels = csv['label']
num_classes = 10
labels = utils.to_categorical(np.asarray(labels.factorize()[0]), num_classes=num_classes)

# Split the data into train and test datasets
X_train, X_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.2, random_state=42)

# Create model
model = keras.Sequential([
    layers.Dense(256, input_shape=[15], activation="relu"),
    #layers.Dropout(0.1),
    layers.Dense(128, activation="relu"),
    #layers.Dropout(0.1),
    layers.Dense(64, activation="relu"),
    #layers.Dropout(0.1),
    layers.Dense(32, activation="relu"),
    #layers.Dropout(0.1),
    layers.Dense(10, activation='softmax')
])
model.compile(loss="categorical_crossentropy", optimizer= "adam", metrics=['accuracy'])

# Train model
model.fit(X_train, y_train, epochs=100)

# Print model statistics
test_loss, test_acc = model.evaluate(X_test,  y_test, verbose=2)
print('\nTest accuracy:', test_acc)
y_test_arg = np.argmax(y_test,axis=1)
y_pred = np.argmax(model.predict(X_test),axis=1)
print(classification_report(y_test_arg, y_pred))

# Save the model
model.save(config.model_path)