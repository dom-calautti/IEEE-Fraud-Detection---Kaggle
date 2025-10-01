import pandas as pd
from pathlib import Path
import os

PROJECT_ROOT = Path(__file__).parent.parent
RAW = PROJECT_ROOT / "data" / "raw"
WORKING = PROJECT_ROOT / "data" / "working"

READ_KW = {
    "low_memory": False
}

def load_train_merged() -> pd.DataFrame:
    print(f"Loading from: {RAW / 'train_transaction.csv'}")
    trans = pd.read_csv(RAW / "train_transaction.csv", **READ_KW)
    ident = pd.read_csv(RAW / "train_identity.csv", **READ_KW)
    df = trans.merge(ident, on="TransactionID", how="left")
    return df

def load_test_merged() -> pd.DataFrame:
    trans = pd.read_csv(RAW / "test_transaction.csv", **READ_KW)
    ident = pd.read_csv(RAW / "test_identity.csv", **READ_KW) 
    df = trans.merge(ident, on="TransactionID", how="left")
    return df