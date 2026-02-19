
import pandas as pd
import sys

def main(pred_path, test_nodes_path):
    preds = pd.read_csv(pred_path)
    test_nodes = pd.read_csv(test_nodes_path)

    if "id" not in preds.columns or "ml_target" not in preds.columns:
        raise ValueError("predictions.csv must contain id and y_pred")

    if preds["id"].duplicated().any():
        raise ValueError("Duplicate IDs found")

    if preds["ml_target"].isna().any():
        raise ValueError("NaN predictions found")

    if ((preds["ml_target"] < 0) | (preds["ml_target"] > 1)).any():
        raise ValueError("Predictions must be in [0,1]")

    if set(preds["id"]) != set(test_nodes["id"]):
        raise ValueError("Prediction IDs do not match test nodes")

    print("VALID SUBMISSION")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
