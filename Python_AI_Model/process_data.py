import os
import librosa
import pandas as pd
import numpy as np
import config

def extract_features(file_path):
    """Extract audio features from a file using librosa"""
    try:
        # Load audio file
        audio, sr = librosa.load(file_path, duration=30)
        
        # Extract features
        mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
        spectral_centroid = librosa.feature.spectral_centroid(y=audio, sr=sr)
        spectral_bandwidth = librosa.feature.spectral_bandwidth(y=audio, sr=sr)
        chroma = librosa.feature.chroma_stft(y=audio, sr=sr)
        rms = librosa.feature.rms(y=audio)
        rolloff = librosa.feature.spectral_rolloff(y=audio, sr=sr)
        zero_cross = librosa.feature.zero_crossing_rate(y=audio)
        onset_env = librosa.onset.onset_strength(y=audio, sr=sr)
        tempo = librosa.feature.tempo(onset_envelope=onset_env, sr=sr)

        # Calculate statistics
        features = []
        for feature in [mfccs, spectral_centroid, spectral_bandwidth, chroma, rms, rolloff, zero_cross]:
            features.extend([
                np.mean(feature),
                np.var(feature),
            ])
        features.append(tempo[0])

        return features
    except Exception as e:
        print(f"Error extracting features from {file_path}: {str(e)}")
        return None

""""Create csv with the extracted features of all songs in dataset"""
if (__name__ == '__main__'): 

    features = []
    labels = []
    file_names = []

    # Process each genre folder
    for genre in os.listdir(config.genre_data_dir):
        genre_path = os.path.join(config.genre_data_dir, genre)
        if os.path.isdir(genre_path):
            print(f"Processing {genre} files...")
            
            # Process each audio file in the genre folder
            for file_name in os.listdir(genre_path):
                if file_name.endswith('.wav'):
                    file_path = os.path.join(genre_path, file_name)
                    extracted_features = extract_features(file_path)
                    
                    if extracted_features:
                        file_names.append(file_name)
                        features.append(extracted_features)
                        labels.append(genre)

    # Create dataframe and save as csv file
    features = np.array(features)
    df = pd.DataFrame({
                'mfcc_mean': features[:, 0],
                'mfcc_var' : features[:, 1],
                'spectral_centroid_mean' : features[:, 2],
                'spectral_centroid_var' : features[:, 3],
                'spectral_bandwidth_mean' : features[:, 4],
                'spectral_bandwidth_var' : features[:, 5],
                'chroma_mean' : features[:, 6],
                'chroma_var' : features[:, 7],
                'rms_mean' : features[:, 8],
                'rms_var' : features[:, 9],
                'rolloff_mean' : features[:, 10],
                'rolloff_var' : features[:, 11],
                'zero_cross_mean' : features[:, 12],
                'zero_cross_var' : features[:, 13],
                'tempo' : features[:, 14],
                'label' : labels}, index=file_names)
    df.to_csv(config.csv_path)

