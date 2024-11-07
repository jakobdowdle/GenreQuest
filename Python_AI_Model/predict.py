import os
import keras
import numpy as np
import pandas as pd
import config
from process_data import extract_features

# Load the model
model = keras.models.load_model(config.model_path)

# Path to the song you want to predict, and extract features
song_path = os.path.join(config.CURRENT_DIRECTORY, 'Data/genres_data/pop/pop.00079.wav')
features = extract_features(song_path)

# Read the csv to get the mean and standard deviation to normalize the feature data
csv = pd.read_csv(config.csv_path)
allfeatures = csv.iloc[:, 1:len(csv.columns)-1]
mean = allfeatures.mean()
std = allfeatures.std()
features = ((features - mean) / std)

# Properly reashape array to input into model and make prediction
features = np.array(features).reshape(1, -1)
predictions = model.predict(features)
predictions = np.squeeze(predictions)

# Format and print prediction percentages and final genre prediction
predictions_percentages = [f"{num:.2%}" for num in predictions]
genres = os.listdir(config.genre_data_dir)
genre_predictions = dict(zip(genres, predictions_percentages))
print("\n")
print(genre_predictions)
print("The predicted genre is: " + genres[np.argmax(predictions)])