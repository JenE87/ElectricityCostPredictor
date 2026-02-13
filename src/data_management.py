import joblib
import pandas as pd
import streamlit as st


@st.cache_data
def load_electricity_data():
    """Load the cleaned dataset with stnadardised names and with basic error handling."""
    file_path = "outputs/datasets/cleaned/ElectricityCostCleaned.csv"

    try:
        df = pd.read_csv(file_path)
        if df.empty:
            st.error("Dataset is empty. Please rerun Notebook 01 (Data Collection).")
            st.stop()
        return df
    
    except FileNotFoundError:
        st.error(
            f"Dataset file not found at `{file_path}`.\n\n"
            "Please run Notebook 01 (Data Collection) first."
        )
        st.stop()
    
    except Exception as e:
        st.error(f"Unexpected error while loading dataset:\n\n{e}")
        st.stop()


def load_pkl_file(file_path: str):
    """Load a pickle file (model/features) with error handling."""
    try:
        return joblib.load(file_path)
    
    except FileNotFoundError:
        st.error(
            f"File not found at `{file_path}`.\n\n"
            "Please run Notebook 04 (Modelling & Evaluation)."
        )
        st.stop()
    
    except Exception as e:
        st.error(f"Unexpected error while loading file:\n\n{e}")
        st.stop()