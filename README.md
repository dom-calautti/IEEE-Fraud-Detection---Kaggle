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
2) Download the Dataset and place in /data/raw
   
3) Run Jupyter notebook
   ```
     jupyter notebook
   ```
4) Run all cells in model_comparison.ipynb
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
