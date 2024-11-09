from utils import load_config
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from joblib import dump

def main():
    config = load_config()
    data_path = config["train_dir"] / "train_features.csv"
    model_dir = config["model_dir"]
    model_path = model_dir / "trained_model.pkl"
    columns_path = model_dir / "feature_columns.pkl"

    df = pd.read_csv(data_path)
    X = pd.get_dummies(df.drop(columns=["label"]), drop_first=True)
    y = df["label"]

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)
    model = RandomForestClassifier().fit(X_train, y_train)

    model_dir.mkdir(parents=True, exist_ok=True)
    dump(model, model_path)
    dump(X.columns, columns_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    main()
