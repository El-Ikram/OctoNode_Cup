# competition/evaluate.py

import pandas as pd
import sys
from metrics import macro_f1


def main(pred_path, label_path):
    # Load files
    preds = pd.read_csv(pred_path)
    labels = pd.read_csv(label_path)

    # Validate required columns
    required_pred_cols = {"id", "y_pred"}
    required_label_cols = {"id", "y_true"}

    if not required_pred_cols.issubset(preds.columns):
        raise ValueError("Prediction file must contain columns: id, y_pred")

    if not required_label_cols.issubset(labels.columns):
        raise ValueError("Label file must contain columns: id, y_true")

    # Check duplicate IDs
    if preds["id"].duplicated().any():
        raise ValueError("Duplicate IDs found in submission")

    if labels["id"].duplicated().any():
        raise ValueError("Duplicate IDs found in labels")

    # Sort
    preds = preds.sort_values("id").reset_index(drop=True)
    labels = labels.sort_values("id").reset_index(drop=True)

    # Check exact match of IDs
    if not preds["id"].equals(labels["id"]):
        raise ValueError("Submission IDs do not match test IDs exactly")

    # Compute score
    score = macro_f1(labels["y_true"], preds["y_pred"])

    print(f"SCORE={score:.8f}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
