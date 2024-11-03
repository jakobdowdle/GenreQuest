import os

CURRENT_DIRECTORY = os.getcwd()
genre_data_dir = os.path.join(CURRENT_DIRECTORY, 'data/genres_data')
csv_path = os.path.join(CURRENT_DIRECTORY, 'data/features.csv')
model_path = os.path.join(CURRENT_DIRECTORY, 'data/model.keras')