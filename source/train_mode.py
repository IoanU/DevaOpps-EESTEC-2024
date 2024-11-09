import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from joblib import dump

def main():
    # Load the extracted features from train_features.csv
    data_path = "./InputData/train/train_features.csv"
    df = pd.read_csv(data_path)

    # Separate features and labels
    X = df.drop(columns=["label"])
    y = df["label"]

    # Split data for validation
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Random Forest model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Validate model
    y_pred = model.predict(X_val)
    accuracy = accuracy_score(y_val, y_pred)
    print(f"Validation Accuracy: {accuracy:.2f}")

    # Save the trained model
    model_path = "./source/model/trained_model.pkl"
    dump(model, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    main()

