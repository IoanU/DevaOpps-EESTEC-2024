import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from joblib import dump
from pathlib import Path

def main():
    data_path = Path("/usr/src/app/InputData/train/train_features.csv")
    model_dir = Path("/usr/src/app/source/model")
    model_path = model_dir / "trained_model.pkl"
    columns_path = model_dir / "feature_columns.pkl"

    df = pd.read_csv(data_path)

    for col in df.columns:
        if df[col].apply(lambda x: isinstance(x, list)).any():
            df = df.explode(col)

    X = pd.get_dummies(df.drop(columns=["label"]), drop_first=True)
    y = df["label"]

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier().fit(X_train, y_train)

    model_dir.mkdir(parents=True, exist_ok=True)
    dump(model, model_path)
    dump(X.columns, columns_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    main()
