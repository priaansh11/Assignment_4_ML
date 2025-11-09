# ML Assignment 4 — Machine Learning Pipeline

This project builds a complete **AdaBoost-based ML pipeline** for predicting **Airline Passenger Satisfaction**.  
The pipeline automates data ingestion, validation, preprocessing, model training, and evaluation — all controlled through YAML configuration files.

---

## ✅ Project Structure

### 🔹 Root Files

- **main.py** – Runs the entire ML pipeline sequentially  
- **app.py** – Optional script for predictions / deployment  
- **params.yaml** – Hyperparameters for the AdaBoost model  
- **config.yaml** – File paths and pipeline settings  
- **schema.yaml** – Input dataset schema for validation  
- **requirements.txt** – Python dependencies  
- **README.md** – Project documentation  

---

## 📂 src/ — Core Modules

| Folder/File       | Purpose |
|------------------|---------|
| **components/**  | Code for each pipeline step (ingestion, validation, transformation, training, evaluation) |
| **config/**      | Loads YAML config files dynamically |
| **constants/**   | Common constants such as file paths and schema refs |
| **entity/**      | Data classes for configs and artifacts |
| **pipeline/**    | Wrapper scripts to run specific pipeline stages |
| **utils/**       | Helper functions for saving models, reading YAML, etc. |

---

## 📁 artifacts/ — Output Files

Created automatically after running the pipeline:

- Train/test datasets  
- Processed transformed data  
- Trained AdaBoost model (`model.joblib`)  
- Evaluation metrics (`metrics.json`)  
- Logging information  

---

## 🧪 research/

Contains experimental Jupyter notebooks used during development and testing before finalizing the pipeline.

---

## 📝 logs/

Pipeline logs are stored here.

