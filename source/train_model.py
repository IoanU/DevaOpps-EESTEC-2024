import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from joblib import dump
import os

def main():
    data_path = "/home/matei/Repositories/DevaOpps/InputData/train/train_features.csv"
    model_dir = "/home/matei/Repositories/DevaOpps/source/model"
    model_path = os.path.join(model_dir, "trained_model.pkl")
    columns_path = os.path.join(model_dir, "feature_columns.pkl")

    df = pd.read_csv(data_path)

    # Separate features and labels
    X = df.drop(columns=["label"])
    y = df["label"]

    # One-hot encode categorical columns and save columns
    X_encoded = pd.get_dummies(X, drop_first=True)
    X_train, X_val, y_train, y_val = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Save the model and column names
    os.makedirs(model_dir, exist_ok=True)
    dump(model, model_path)
    dump(X_encoded.columns, columns_path)
    print(f"Model saved to {model_path}")
    print(f"Feature columns saved to {columns_path}")

if __name__ == "__main__":
    main()
