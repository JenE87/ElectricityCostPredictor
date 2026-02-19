import numpy as np
import pandas as pd


def resident_group(resident_count: int) -> str:
    """
    Group resident_count into the same categories used during
    feature engineering (Notebook 03): none, low, medium, high.
    """
    if resident_count == 0:
        return "none"
    elif resident_count <= 50:
        return "low"
    elif resident_count <= 150:
        return "medium"
    else:
        return "high"


def prepare_features(user_inputs: dict, model_features: list) -> pd.DataFrame:
    """
    Convert user inputs from the Streamlit form into a single-row DataFrame
    matching the trained model's features (including engineered/encoded
    features)
    """
    row = {feature: 0 for feature in model_features}

    row["site_area"] = user_inputs["site_area"]
    row["water_consumption"] = user_inputs["water_consumption"]
    row["recycling_rate"] = user_inputs["recycling_rate"]
    row["utilisation_rate"] = user_inputs["utilisation_rate"]
    row["air_quality_index"] = user_inputs["air_quality_index"]
    row["issue_resolution_time"] = user_inputs["issue_resolution_time"]
    row["resident_count"] = user_inputs["resident_count"]

    row["water_consumption_log"] = np.log1p(user_inputs["water_consumption"])

    group = resident_group(user_inputs["resident_count"])
    if group == "low":
        row["resident_group_low"] = 1
    elif group == "medium":
        row["resident_group_medium"] = 1
    elif group == "none":
        row["resident_group_none"] = 1
    # if "high", all cols stay 0

    stype = user_inputs["structure_type"]
    if stype == "Industrial":
        row["structure_type_Industrial"] = 1
    elif stype == "Mixed-use":
        row["structure_type_Mixed-use"] = 1
    elif stype == "Residential":
        row["structure_type_Residential"] = 1
    # if "Commercial", all cols stay 0

    X_live = pd.DataFrame([row])[model_features]
    return X_live


def predict_cost(model, X_live: pd.DataFrame) -> float:
    """Return a single electricity cost prediction as a float."""
    return float(model.predict(X_live)[0])
