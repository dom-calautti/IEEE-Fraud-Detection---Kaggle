IEEE-CIS Fraud Detection Project

Course: LE/EECS 4412 A - Data Mining (Fall 2025-2026)

Dataset: IEEE-CIS Fraud Detection (Kaggle)

------------------------------------------------------------
SETUP
------------------------------------------------------------
1) Clone the repo
   ```
   git clone https://github.com/dom-calautti/IEEE-Fraud-Detection---Kaggle.git
   cd ieee-fraud
   ```
3) Python environment (we standardize on Python 3.11)
   Conda:
   ```
     conda create -n ieeefraud python=3.11 -y
     conda activate ieeefraud
   ```
   or a virtual environment:
   ```
     py -3.11 -m venv .venv
     .\.venv\Scripts ctivate
    ```
5) Install packages
   ```
   pip install -r requirements.txt
   ```
------------------------------------------------------------
DATA
------------------------------------------------------------
We use Kaggle’s competition data. It is **NOT** checked into Git.

1) Create Kaggle API token (Profile -> Create API Token) to get kaggle.json
2) Place kaggle.json:
   Windows: C:\Users\<YOU>\.kaggle\kaggle.json
   Mac/Linux: ~/.kaggle/kaggle.json
3) Download and unzip
   ```
   mkdir -p data/raw
   kaggle competitions download -c ieee-fraud-detection -p data/raw
   cd data/raw
   unzip "*.zip"
   cd ../../
   ```
------------------------------------------------------------
NOTEBOOKS 
------------------------------------------------------------
Start Jupyter Lab:
```
  jupyter lab
```
1. notebooks/eda.ipynb
   - Exploratory plots, fraud rate by hour/day-of-week, amount distributions

2. notebooks/preprocess.ipynb
   - Preprocessing, missingness flags, time-based train/valid split

3. notebooks/baselines.ipynb
   - Baselines (Logistic Regression with class_weight='balanced', XGBoost/LightGBM)
   - Prints ROC-AUC and PR-AUC

------------------------------------------------------------
COLLABORATION WORKFLOW
------------------------------------------------------------
- Branch naming: eda/<name>



