# Electricity Cost Predictor
[Electricity Cost Predictor](https://electricity-cost-predictor-5d88feda62f8.herokuapp.com/) is a machine learning (ML) project using a publicly available dataset to determine whether a regression pipeline can be built to estimate monthly electricity cost for different site profiles.
This was achieved bny training a supervised regression model using `electricity_cost` as the target variable and site and operational characteristics (such as site are, utilisation rate, water consumption, and resident count) as features.
The project combines exploratory data analysis, feature engineering, and model evaluation within an interactive Streamlit dashboard to support budgeting and planning decisions.

## Table of Contents 
- [Dataset Content](#dataset-content)
- [Project Terms & Jargon](#project-terms-and-jargon)
- [Business Requirements](#business-requirements)
- [Hypotheses](#hypothesis-and-how-to-validate-them)
- [Mapping Business Requirements to Data Visualization and ML Tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ml-tasks)
- [ML Business Case](#ml-business-case)
- [Epics and User Stories](#epics-and-user-stories)
- [Dashboard Design](#dashboard-design)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## Dataset Content
This project uses a publicly available dataset sourced from [Kaggle](https://www.kaggle.com/datasets/shalmamuji/electricity-cost-prediction-dataset) that contains site and operational factors related to electricity cost. Each row represents a site and each column contains a site attribute.

The dataset is anonymised and suitable for public use. It consists of 10,000 rows and 9 columns, including the target variable (`Electricity Cost`).


| Variable              | Meaning                                                                | Units                                          |
|-----------------------|------------------------------------------------------------------------|------------------------------------------------|
| Site Area             | Total area of the site in square meters                                | 501 - 5000                                     |
| Structure Type        | Primary usage type of the site                                         | Residential, Commercial, Mixed-use, Industrial |
| Water Consumption     | Estimated daily water usage in liters                                  | 1000 - 9905                                    |
| Recycling Rate        | Percentage of waste that is recycled at the site                       | 10 - 90                                        |
| Utilisation Rate      | Percentage of the site's capacity that is currently being utilized     | 30 -100                                        |
| Air Quality Index     | Air quality measurement at the site, with low values representing good air quality, and high values poor air quality | 0 -200 |
| Issue Resolution Time | Time taken to resolve operational or maintenance issues at the site in hours | 1 - 72                                   |
| Resident Count        | Number of residents or occupants at the site                           | 0 - 441                                        |
| Electricity Cost      | Monthly electricity cost in USD                                        | 500 - 5852                                     |


## Project Terms & Jargon
- **Electricity cost**: monthly electricity spend (USD)
- **Site profile**: a combination of site attributes used to estimate cost
- **Cost drivers**: variables that tend to increase/decrease costs
- **Prediction**: model estimate based on historical patterns (not guaranteed)


## Business Requirements
The client is a fictional facilities and cost manager working for a construction and property management company, responsible for operational energy expenditure. Electricity cost represent a significant and increasingly volatile operational expense. 

The client currently lacks insight into which factors most strongly influence electricity cost and has no reliable way to estimate future cost for different property site profiles. Without data-driven insights, the client risks inefficient budgeting, unexpected cost overruns, and suboptimal decision-making when managing or planning sites.

The project will be considered successful if:
- Key factors influencing electricity cost are identified through data analysis and clearly communicated using data visualisations.
- A machine learning model is capable of generating reasonable electricity cost predictions based on site characteristics.
- The results are presented in a clear, accessible dashboard suitable for non-technical stakeholders.

**Business requirement 1:** The client requires an understanding of how different site characteristics and operational factors influence electricity cost.

**Business requirement 2:** The client requires a predictive model capable of estimating electricity cost for a given site profile in order to support budgeting and planning decisions.


## Hypotheses and how to validate them
- **Hypothesis 1 - Site characteristics influence electricity cost**
   - Hypothesis: Electricity cost vary significantly depending on site characteristics such as site area, structure type, utilisation rate, and resident count.
   - Validation: This hypothesis will be validated through exploratory data analysis (EDA) and visualisations (e.g. correlation analysis) to identify which variables show strong relationships with electricity cost.
- **Hypothesis 2 - Operational intensity is a strong cost driver**
   - Hypothesis: Sites with higher operational intensity (e.g. higher utilisation rate or resident count) have higher electricity cost than less intensively used sites.
   - Validation: This will be validated by analysing electricity cost across different operational usage levels and visualising trends between operational variables and electricity cost.
- **Hypothesis 3 - A regression model can predict electricity cost with acceptable accuracy**
   - Hypothesis: A supervised machine learning regression model trained on site and operational features can predict electricity cost with reasonable accuracy.
   - Validation: This hypothesis will be validated by training a regression model and evaluating its performance using appropriate metrics such as R² and RMSE on a held-out test set.


## The rationale to map the business requirements to the Data Visualizations and ML tasks
- **Business Requirement 1 (Data Visualization and Correlation Analysis)**
   - BR1 is addressed on dashboard page **Electricity Cost Driver Analysis** (main insights, correlation, cost driver plots) and supported by page **Project Hypotheses & Validation**.
   - We use **EDA** and **visualizations** to show how each feature relates to electricity cost.
   - Techniques include: dataset inspection, distribution plots, and correlation analysis (numeric features).
   - Outcome: clear summary of strongest drivers (e.g., site area, utilisation/occupancy patterns).
- **Business Requirement 2 (Regression & Data Analysis)**
   - BR2 is addressed on dashboard page **Electricity Cost Prediction** (live predictions from user inputs) and **Model Performance** (train/test metrics, plots, feature importance, limitations).
   - We train a **supervised regression model** using the cleaned dataset.
   - We evaluate the model using train/test split performance (R², RMSE, MAE).
   - Outcome: a Streamlit predictor that estimates monthly electricity cost for a user-defined site profile.

[Back to top](#electricity-cost-predictor)

## ML Business Case
### Predict Electricity Cost
**Regression Model**
- We want a machine learning model to predict **monthly electricity cost (USD)** for a site based on its physical and operational characteristics. The target variable, `electricity_cost`, is **continuous numeric data**, so we consider a **regression model**. This is a **supervised learning** task with a single numeric output.
- The ideal outcome is to provide the client (facilities/cost manager) with a consistent and repeatable estimate of monthly electricity cost for different site profiles, to support budgeting and planning decisions.
- **Model success metrics (test set)**:
   - R² score ≥ 0.90
   - RMSE ≤ 300 USD
   - MAE ≤ 250 USD
   - **Result:** The final Random Forest model meets the success criteria on the held-out test set.
- **Model failure criteria**:
   - R² < 0.85 or RMSE > 400 USD, indicating predictions are not reliable enough for planning, or
   - Overfitting indicated by a large train/test gap (e.g., Train R² - Test R² > 0.05).
   - **Note:** If success thresholds are not met, but the model remains above the minimum guardrails, results are considered **borderline** and should be used with caution.
- The model output is defined as a single predicted electricity cost value (USD/month) for a user-provided site profile. Predictions are generated on demand in the Streamlit dashboard (not in batches).
   - Predictions are most reliable when input values fall within the ranges observed in the training dataset.
- Heuristics: Currently, the client has no data-driven approach for estimating electricity cost across varying site profiles and relies on manual judgement and rough comparisons.
- The training data to the model comes from Kaggle.
   - The dataset contains 10,000 observations and 9 attributes (including the target).
   - Target: `electricity_cost`
   - Features: `site_area`, `structure_type`, `water_consumption`, `recycling_rate`, `utilisation_rate`, `air_quality_index`, `issue_resolution_time`, `resident_count`


## Epics and User Stories
The project was divided into five epics, based on data visualisation and machine learning tasks.

### Epic 1 - Information Gathering and Data Collection
- **User Story** - As a data analyst, I can import the electricity cost dataset from Kaggle so that I can work with a local copy of the data. 
- **User Story** - As a data analyst, I can load and inspect the dataset so that I can understand its structure and contents.

### Epic 2 - Data Visualisation, Cleaning, and Preparation
- **User Story** - As a data analyst, I can explore and visualise the dataset so that I can identify factors influencing electricity cost (*Business Requirement 1*).
- **User Story** - As a data analyst, I can clean the dataset and handle missing or inconsistent values to prepare it for modelling.
- **User Story** - As a data scientist, I can perform feature engineering to improve the dataset for machine learning.

### Epic 3 - Model Training, Optimisation, and Validation
- **User Story** - As a data scientist, I can split the data into training and test sets to prepare it for modelling.
- **User Story** - As a data scientist, I can train a regression model to predict electricity cost based on site characteristics (*Business Requirement 2*).
- **User Story** - As a data scientist, I can evaluate and optimise the model to ensure it produces reliable predictions.

### Epic 4 - Dashboard Planning, Designing, and Development
- **User Story** - As a non-technical user, I can view a project summary explaining the dataset and business requirements.
- **User Story** - As a non-technical user, I can explore visualisations that explain which factors influence electricity cost (*Business Requirement 1*).
- **User Story** - As a non-technical user, I can input site characteristics and receive an estimated electricity cost (*Business Requirement 2*).
- **User Story** - As a technical user, I can view model performance metrics and validation results.

### Epic 5 - Dashboard Deployment and Release
- **User Story** - As a user, I can access the dashboard via a publicly deployed web application.
- **User Story** - As a technical user, I can follow the README instructions to reproduce or redeploy the project.


## Dashboard Design
### Page 1: Project Summary
- A brief project introduction
- Dataset summary (source, size, target variable)
- State business requirements
- Key project terminology

### Page 2: Project Hypotheses
- List of project hypotheses
- Describe how each hypothesis was validated using data analysis or machine learning
- Summarise conclusions once analysis is complete

### Page 3: Electricity Cost Driver Analysis
- Display preview of the dataset (shape and first rows)
- Present correlation analysis between features and electricity cost
- Show visualisations of key variables against electricity cost
- Summarise insights on which site and operational factors most influence electricity cost

### Page 4: Electricity Cost Prediction
- Provide input widgets for site and operational characteristics
- Allow users to generate electricity cost predictions for unseen site profiles
- Display the predicted electricity cost output in a clear and interpretable format

### Page 5: Model Performance and Technical Details
- Overview of the machine learning pipeline
- Features used to train the model
- Model performance metrics (e.g. R², RMSE)
- Feature importance

[Back to top](#electricity-cost-predictor)

## Testing
### Manual Testing
| Feature / Page      | Action            | Expected Result      | Pass/Fail |
|---------------------|-------------------|----------------------|-----------|
| Dashboard - Heroku Deployment | Open live URL | App loads successfully in browser | Pass |
| Dashboard - Sidebar Navigation | Click each page in the sidebar | Correct page loads, no errors | Pass |
| Dashboard - Project Summary | Open Page | Text displays, link to README works, dataset metrics + key inputs show correctly | Pass |
| Dashboard - Project Hypotheses  | Open page and expand | Hypotheses text displays, checkbox reveals method summary | Pass |
| Dashboard - Electricity Cost Driver Analysis  | Open page, expander and toggle sections | Text displays, plots render and table preview shows expected columns | Pass |
| Dashboard - Electricity Cost Prediction | Open page, enter valid values and run prediction | Prediction appears and updates (incl. estimated cost, cost category, interpretation) based on inputs | Pass |
| Dashboard - Model Performance | Open page and expand "Technical Details" | Text displays, metrics display and optional plots/feature importance render | Pass |
| Data - Raw dataset loads | Start app / open Electricity Cost Driver Analysis page  | Raw csv loads and preview displays | Pass |
| Data - Cleaned dataset loads | Open pages using cleaned data  | Cleaned csv loads without erros or missing columns | Pass |
| Data - Model artefacts exist | Open Model Performance page | Model and X/y splits load successfully | Pass |
| Data - Feature importance file | Open Model Performance page and toggle "Show feature importance" | Table and png display | Pass |

### Validation Testing
All Python files in `app_pages/`, `src/` and `app.py` were validated using the [CI Python Linter](https://pep8ci.herokuapp.com/) with no remaining errors, as per PEP8 guidelines.

Minor warnings were identified and corrected, including:
- Ensuring top-level functions and class definitions are surrounded by 2 blank lines
- Breaking up long lines to comply with the 79-character limit
- Removing trailing whitespace and unnecessary blank lines
- Adding missing whitespace around operators and commas 
- Fixing indentation inconsistencies
- Removing unused imports

### Fixed Bugs
- **Missing `structure_type` column in dataset preview** (Electricity Cost Driver Analysis page)
   Fix: Used the raw dataset for the preview and standardised headers (snake_case + typo corrections) to ensure `structure_type` is available for display.
- **Raw dataset column typos and spacing caused empty/missing preview columns**
   Fix: Standardised column names and corrected known typos (e.g., `air qality index` → `air_quality_index`, `issue reolution time` → `issue_resolution_time`) in the raw dataset loading function.
- **Streamlit version did not support `border=True` in `st.metric()`**
   Fix: Replaced `border=True` with `st.container()` layout to keep clean visual structure.
- **Heroku build log warning about `runtime.txt` deprecation**
   Fix: Removed `runtime.txt` to align with current Heroku recommendations and avoid future deployment issues.
- **Long pages with too much scrolling**
   Fix: Use expanders with the setting `expanded=False` on the Model Performance and Electricity Cost Driver Analysis pages instead of expanded sections and separators, to improve UX and prevent excessive scrolling.

### Unfixed Bugs
No known unfixed bugs at the time of submission.

[Back to top](#electricity-cost-predictor)

## Deployment
### Heroku
- The App live link is: [Electricity Cost Predictor](https://electricity-cost-predictor-5d88feda62f8.herokuapp.com/)

The project was deployed to Heroku using the following steps:

1. Ensure you have a `setup.sh` file in your working directory with the following code:
   ```
   mkdir -p ~/.streamlit/
   echo "\
   [server]\n\
   headless = true\n\
   port = $PORT\n\
   enableCORS = false\n\
   \n\
   " > ~/.streamlit/config.toml
   ```
2. In the `.python-version` file ensure that it contains a [Heroku-24](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack supported version of Python (e.g., `3.12`)
3. Ensure you have a Procfile in the working directory with the following code:
   `web: sh setup.sh && streamlit run app.py`
4. Log in to [Heroku](https://id.heroku.com/login) or create an account
5. On the dashboard in the top-right corner first click **New** and then **Create new app**
6. Choose a unique **App name**
7. Choose your local **Location** (e.g., `Europe`)
8. Click **Create app**
9. In the **Deploy tab**, under **deployment method** select **GitHub** as the deployment method.
10. Enter your repository name and click **Search**. Once found, click **Connect**.
11. Select the branch you want to deploy (e.g., `main`), then under **Manual Deploy** click **Deploy Branch**. 
12. Once your app has been successfully deployed, you can access it by clicking the **View** button at the bottom of the Manual Deploy section or the **Open App** at the top of the page.

**Note:**
The deployment process should happen smoothly if all deployment files are fully functional.
If the deployment fails, check the build log for details of where troubleshooting is required.
For example, if the slug size is too large then add large files not required for the app to the `.slugignore` file.

## Forking and Cloning
Should you wish to fork or clone this repository, please follow the instructions below:

### Forking
1. On the main repository page, click the **Fork** button in the top-right corner.
2. Choose the desired **Owner** for the fork from the dropdown menu.
3. *(Optional)* Change the **repository name** if you want to distinguish it from the original.
4. *(Optional)* Add a **description** in the designated field.
5. Ensure **Copy the `main` branch only** is checked.
6. Click the **Create fork** button to finish forking the repository.

### Cloning
1. On the main repository page above the list of files, click the **<> Code** button.
2. Copy the URL (`https://github.com/...`) provided under Local > HTTPS.
3. Open a terminal in your IDE and navigate to the directory in which you want to create the cloned repository.
4. In your IDE terminal type `git clone` and paste the URL copied earlier (`git clone https://github.com/USERNAME/REPONAME`)
5. Press **Enter** to create your local cloned repository.

### Installing Requirements
The `requirements.txt` file only contains the packages required for dashboard deployment. 
The `all-requirements.txt` file includes all the development and analysis dependencies used in the notebook. 

To install all the dependencies required for full local development and execution of the notebooks, run the following command in your terminal:
`pip install -r all-requirements.txt`

[Back to top](#electricity-cost-predictor)

## Main Data Analysis and Machine Learning Libraries
- **Pandas**
   Used for loading csv files, inspecting data, and preparing train/test splits (e.g., `pd.read_csv()`, `.value_counts()`, selecting columns).
- **Numpy**
   Used for numeric operations and transformations during preprocessing (e.g., `np.log1p()` for skew reduction).
- **Matplotlib**
   Used for visualisations in the Streamlit dashboard (e.g., correlation bar chart, scatter plot for actual vs predicted, residual histogram).
- **Seaborn**
   Used for higher-level statistical plots during EDA (e.g., boxplots comparing distributions).
- **scikit-learn**
   Used for training and evaluating regression models (Linear Regression baseline and Random Forest Regressor), plus regression metrics such as R², RMSE, MAE.
- **joblib**
   Used to save and reload trained model artefacts and reusable objects (e.g., `random_forest_model.pkl`, `model_features.pkl`)
- **Streamlit**
   Used to build and deploy the interactive dashboard application. It enables rapid development of data-driven web apps and was used to structure multi-page navigation, display visalisations, render model outputs, and collect user input for electricity cost prediction.
- **Ydata-profiling**
   Used during EDA to generate an automated profiling report that supported feature understanding and preprocessing decisions.


## Credits 
### Code
- Code Institute LMS course materials, walkthroughs, custom classes and functions with focus on the predictive analytics and machine learning module
- [Python.org](https://www.python.org/)
- [Medium - Member Articles](https://medium.com/)
- [datacamp](https://www.datacamp.com/de)
- [Stack Overflow](https://stackoverflow.com/questions)
- [W3 schools](https://www.w3schools.com/)
- [Geeksforgeeks - Machine Learning](https://www.geeksforgeeks.org/machine-learning/machine-learning/)
- [freecodecamp](https://www.freecodecamp.org/news/)
- Sololearn (App)
- Programming Hub (App)

### Content & Media
- All content was written by the project developer, with usage of [ChatGPT](chatgpt.com) and [DeepL](https://www.deepl.com) for spelling, wording and correct grammar.
- The icons in the dashboard were taken from [Streamlit emojis shortcodes](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/)


## Acknowledgements (optional)
* Thank the people who provided support through this project.

[Back to top](#electricity-cost-predictor)
