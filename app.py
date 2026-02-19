from app_pages.multipage import MultiPage

from app_pages.page_summary import page_summary_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_cost_drivers import page_cost_drivers_body
from app_pages.page_predict_electricity_cost import (
    page_predict_electricity_cost_body)
from app_pages.page_model_performance import page_model_performance_body

app = MultiPage(app_name="Electricity Cost Predictor")

app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Project Hypotheses & Validation", page_project_hypothesis_body)
app.add_page("Electricity Cost Driver Analysis", page_cost_drivers_body)
app.add_page("Electricity Cost Prediction", page_predict_electricity_cost_body)
app.add_page("Model Performance", page_model_performance_body)

app.run()
