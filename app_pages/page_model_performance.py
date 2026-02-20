import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import (
    r2_score, root_mean_squared_error, mean_absolute_error)

from src.data_management import load_pkl_file


def regression_metrics(y_true, y_pred):
    """
    Helper function to compute regression metrics

    Returns:
        tuple: (r2, rmse, mae)
    """
    r2 = r2_score(y_true, y_pred)
    rmse = root_mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    return r2, rmse, mae


def page_model_performance_body():
    """
    Render the Model Performance page.

    This page is for technical / data-practitioner readers.
    It summarises the final model choice and evaluates performance
    on saved train/test splits.
    """

    st.write("### Model Performance")

    st.info(
        "**Business Requirement 2:** Provide a prediction tool that estimates "
        "monthly electricity cost for a given site profile."
    )

    st.write(
        "This page explains how the final model performs and what its main "
        "limitations are."
    )

    st.write("---")

    # Load model and saved train/test splits.
    version = "v1"
    model_path = f"outputs/ml_pipeline/electricity_cost/{version}"

    model = load_pkl_file(f"{model_path}/random_forest_model.pkl")

    X_train = pd.read_csv(f"{model_path}/X_train.csv")
    X_test = pd.read_csv(f"{model_path}/X_test.csv")
    y_train = pd.read_csv(f"{model_path}/y_train.csv").squeeze()
    y_test = pd.read_csv(f"{model_path}/y_test.csv").squeeze()

    st.write("#### Final Model Selection")

    st.success(
        "A **Random Forest Regressor** was selected as the final model "
        "because it achieved strong predictive performance on the test set "
        "and can capture non-linear relationships between site "
        "characteristics and electricity cost."
    )

    st.write("---")

    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    r2_train, rmse_train, mae_train = regression_metrics(y_train, y_train_pred)
    r2_test, rmse_test, mae_test = regression_metrics(y_test, y_test_pred)

    st.write("#### Performance summary (train vs test)")

    st.caption(
        "The **test set** performance is the best indicator of how well the "
        "model generalises to unseen data."
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("R² (Train)", f"{r2_train:,.3f}")
        st.metric("R² (Test)", f"{r2_test:,.3f}")
    with col2:
        st.metric("RMSE (Train)", f"{rmse_train:,.1f}")
        st.metric("RMSE (Test)", f"{rmse_test:,.1f}")
    with col3:
        st.metric("MAE (Train)", f"{mae_train:,.1f}")
        st.metric("MAE (Test)", f"{mae_test:,.1f}")

    st.caption(
        "R² indicates how much variance in electricity cost is explained by "
        "the model (closer to 1 is better). RMSE and MAE are error measures "
        "in USD; lower is better."
    )

    st.write("#### Success criteria (from ML Business Case)")

    # Success thresholds (test set)
    success_r2 = 0.90
    success_rmse = 300
    success_mae = 250

    # Failure thresholds
    fail_r2 = 0.85
    fail_rmse = 400
    gap_threshold = 0.05

    meets_r2 = r2_test >= success_r2
    meets_rmse = rmse_test <= success_rmse
    meets_mae = mae_test <= success_mae
    criteria_pass = meets_r2 and meets_rmse and meets_mae

    train_test_gap = r2_train - r2_test
    gap_ok = train_test_gap <= gap_threshold

    st.caption(
        f"Targets (test set): R² ≥ {success_r2}, RMSE ≤ {success_rmse} USD, "
        f"MAE ≤ {success_mae} USD. Overfitting check: Train-Test R² "
        f"gap ≤ {gap_threshold}. Guardrails are defined for R² and RMSE."
    )

    failure_triggered = (
        (r2_test < fail_r2)
        or (rmse_test > fail_rmse)
        or (not gap_ok)
    )

    if criteria_pass and gap_ok:
        st.success(
            "The final model meets the success criteria on the held-out "
            "test set and shows no concerning train/test gap."
        )
    elif failure_triggered:
        st.warning(
            "The model is below the minimum reliability guardrails "
            "and/or shows a large train/test gap."
        )
    else:
        st.warning(
            "The model is in a borderline range: it does not meet "
            "all target thresholds, but is still above the minimum guardrails."
        )

    st.write("**Criteria checklist (test set):**")

    checklist = pd.DataFrame(
        {
            "Metric": [
                "R² (Test)",
                "RMSE (Test)",
                "MAE (Test)",
                "Train–Test R² gap"
            ],
            "Actual": [
                f"{r2_test:.3f}",
                f"{rmse_test:.2f} USD",
                f"{mae_test:.2f} USD",
                f"{train_test_gap:.3f}"
            ],
            "Target": [
                f"≥ {success_r2}",
                f"≤ {success_rmse} USD",
                f"≤ {success_mae} USD",
                f"≤ {gap_threshold}"
            ],
            "Status": [
                "✅" if meets_r2
                else ("❌" if r2_test < fail_r2 else "⚠️"),
                "✅" if meets_rmse
                else ("❌" if rmse_test > fail_rmse else "⚠️"),
                "✅" if meets_mae
                else "⚠️",
                "✅" if gap_ok
                else "❌",
            ],
        }
    )

    st.dataframe(checklist, hide_index=True, use_container_width=True)

    st.write("")

    with st.expander(
        "Technical Details (features, plots, importance)",
        expanded=False
    ):

        st.write("#### Features used for training")
        st.caption(
            "These are the engineered features used by the trained model "
            "(including one-hot encoded categories and transformed "
            "variables)."
        )

        if st.checkbox("Show feature list"):
            model_features = load_pkl_file(f"{model_path}/model_features.pkl")
            st.write(model_features)

        st.write("---")

        st.write("#### Visual validation (test set)")
        st.caption(
            "These plots help visually assess prediction quality and any "
            "potential bias."
        )

        if st.checkbox("Show actual vs predicted plot"):
            st.caption(
                "Points closer to the diagonal line indicate more accurate "
                "predictions. Larger deviations indicate higher uncertainty."
            )

            fig, axes = plt.subplots(figsize=(6, 6,))
            axes.scatter(y_test, y_test_pred, alpha=0.2, color="tab:blue")
            axes.plot(
                [y_test.min(), y_test.max()],
                [y_test.min(), y_test.max()],
                linestyle="--",
                linewidth=1,
                color="tab:orange"
            )
            axes.set_xlabel("Actual electricity_cost (USD)")
            axes.set_ylabel("Predicted electricity_cost (USD)")
            axes.set_title("Actual vs Predicted (Test Set)")
            st.pyplot(fig)

        if st.checkbox("Show residual distribution"):
            st.caption(
                "Residuals are the difference between actual and predicted "
                "values. A roughly centred distribution suggests limited bias."
            )

            residuals = y_test - y_test_pred
            fig, axes = plt.subplots(figsize=(6, 4))
            axes.hist(residuals, bins=40)
            axes.set_xlabel("Residual (Actual - Predicted)")
            axes.set_ylabel("Frequency")
            axes.set_title("Residual Distribution (Test Set)")
            st.pyplot(fig)

        st.write("---")

        st.write("#### Feature importance (model-based cost drivers)")
        st.caption(
            "Feature importance indicates which variables contributed most to "
            "the model's predictions. It shows relative contribution, not "
            "direction (increase/decrease)."
        )

        if st.checkbox("Show feature importance"):
            feat_imp = pd.read_csv(f"{model_path}/feature_importance.csv")
            st.write("Top 10 features by importance:")
            st.dataframe(feat_imp.head(10))
            st.caption(
                "Higher values indicate greater contribution to predictions "
                "within this model."
            )

            st.image(
                f"{model_path}/feature_importance.png",
                caption="Feature importance (Random Forest)"
            )

    st.write("---")

    st.write("#### Limitations and Interpretation")

    st.info(
        "* Predictions are based on patterns in the historical dataset and "
        "should be treated as estimates.\n"
        "* The model does not include external drivers such as tariffs, "
        "weather, equipment efficiency, or regional energy pricing.\n"
        "* Predictions are most reliable when inputs remain within the ranges "
        "observed in the dataset.\n"
        "* A Random Forest can slightly overfit; the train/test comparison "
        "above is included to monitor generalisation."
    )

    st.success(
        "**Conclusion (BR2):** The Random Forest model demonstrates strong "
        "test performance and is suitable for producing **consistent "
        "electricity cost estimates** to support budgeting and planning "
        "decisions."
    )
