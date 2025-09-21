# DevaOpps 🔥

DevaOpps is a machine learning–powered project designed for **data classification and feature extraction**.  
It provides utilities to preprocess input data, train a model, and classify new samples using a saved pipeline.  

---

## 🚀 Features
- **Feature extraction**: Convert raw inputs into structured features.
- **Data conversion**: Transform datasets into JSON-ready formats.
- **Training pipeline**: Train and save classification models with reproducible feature sets.
- **Inference utilities**: Classify new data using trained models.
- **Pre-configured scripts**: Quick start with ready-made scripts and configs.

---

## 📂 Project Structure
```
DevaOpps-main/
├── .gitignore
├── README.md                # Project documentation
├── DataFolder/              # (User-specific data storage)
├── InputData/               # Raw input data
├── source/                  # Main source code
│   ├── classify.py          # Script to classify new data
│   ├── config.json          # Configuration file for preprocessing/training
│   ├── convert_to_json.py   # Convert raw input into JSON
│   ├── extract_features.py  # Feature engineering pipeline
│   ├── requirements.txt     # Python dependencies
│   ├── startScript.sh       # Shell script for quick startup
│   ├── train_model.py       # Training entry point
│   ├── utils.py             # Helper utilities
│   ├── ceva.zip             # Archived resources
│   └── model/               # Saved ML artifacts
│       ├── feature_columns.pkl
└       └── trained_model.pkl
```

---

## ⚙️ Installation

1. Clone or download the project:
   ```bash
   git clone https://github.com/your-username/DevaOpps.git
   cd DevaOpps-main/source
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🧑‍💻 Usage

### 1. Convert Data
Convert raw inputs into JSON format for later processing:
```bash
python convert_to_json.py --input ../InputData/raw.csv --output ../DataFolder/data.json
```

### 2. Extract Features
Extract features from converted data:
```bash
python extract_features.py --config config.json
```

### 3. Train Model
Train and save the model with extracted features:
```bash
python train_model.py --config config.json
```

### 4. Classify New Data
Run inference on new samples using the trained model:
```bash
python classify.py --input ../InputData/test.csv
```

### 5. Quick Start (one command)
Use the provided shell script to run the pipeline:
```bash
bash startScript.sh
```

---

## 🎯 Project Goal
The goal of **DevaOpps** is to create a reproducible and modular machine learning pipeline that:
- Makes data preprocessing easier.
- Provides consistent feature extraction.
- Enables training and deploying classification models rapidly.
- Allows reusability for different datasets and experiments.

---

## 🛣️ Roadmap
- Add support for more model architectures (e.g., Random Forest, XGBoost).
- Improve config system for experiment tracking.
- Implement web-based interface for data upload & prediction.
- Add automated testing and CI/CD pipelines.

---

## 📜 License
This project is distributed under the MIT License.  
Feel free to use and modify it for your own projects.
