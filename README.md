# Electricity Cost Predictor

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

## Business Requirements
The client is a fictional facilities and cost manager working for a construction and property management company, responsible for operational energy expenditure. Electricity cost represent a significant and increasingly volatile operational expense. 

The client currently lacks insight into which factors most strongly influence electricity cost and has no reliable way to estimate future cost for different property site profiles. Without data-driven insights, the client risks inefficient budgeting, unexpected cost overruns, and suboptimal decision-making when managing or planning sites.

The project will be considered successful if:
- Key factors influencing electricity cost are identified through data analysis and clearly communicated using data visualisations.
- A machine learning model is capable of generating reasonable electricity cost predictions based on site characteristics.
- The results are presented in a clear, accessible dashboard suitable for non-technical stakeholders.

**Business requirement 1:** The client requires an understanding of how different site characteristics and operational factors influence electricity cost.

**Business requirement 2:** The client requires a predictive model capable of estimating electricity cost for a given site profile in order to support budgeting and planning decisions.


## Hypotheses and how to validate?
* List here your project hypothesis(es) and how you envision validating it (them)

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
* List your business requirements and a rationale to map them to the Data Visualizations and ML tasks


## ML Business Case
* In the previous bullet, you potentially visualized an ML task to answer a business requirement. You should frame the business case using the method we covered in the course 


## Epics and User Stories
The project was divided into five epics, based on data visualisation and machine learning tasks.

### Epic - Information Gathering and Data Collection
- **User Story** - As a data analyst, I can import the electricity cost dataset from Kaggle so that I can work with a local copy of the data. 
- **User Story** - As a data analyst, I can load and inspect the dataset so that I can understand its structure and contents.

### Epic - Data Visualisation, Cleaning, and Preparation
- **User Story** - As a data analyst, I can explore and visualise the dataset so that I can identify factors influencing electricity cost (*Business Requirement 1*).
- **User Story** - As a data analyst, I can clean the dataset and handle missing or inconsistent values to prepare it for modelling.
- **User Story** - As a data scientist, I can perform feature engineering to improve the dataset for machine learning.

### Epic - Model Training, Optimisation, and Validation
- **User Story** - As a data scientist, I can split the data into training and test sets to prepare it for modelling.
- **User Story** - As a data scientist, I can train a regression model to predict electricity cost based on site characteristics (*Business Requirement 2*).
- **User Story** - As a data scientist, I can evaluate and optimise the model to ensure it produces reliable predictions.

### Epic - Dashboard Planning, Designing, and Development
- **User Story** - As a non-technical user, I can view a project summary explaining the dataset and business requirements.
- **User Story** - As a non-technical user, I can explore visualisations that explain which factors influence electricity cost (*Business Requirement 1*).
- **User Story** - As a non-technical user, I can input site characteristics and receive an estimated electricity cost (*Business Requirement 2*).
- **User Story** - As a technical user, I can view model performance metrics and validation results.

### Epic - Dashboard Deployment and Release
- **User Story** - As a user, I can access the dashboard via a publicly deployed web application.
- **User Story** - As a technical user, I can follow the README instructions to reproduce or redeploy the project.


## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).

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

## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-24](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the dashboard were taken from [Streamlit emojis shortcodes]([https://fontawesome.com/](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/))

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* Thank the people who provided support through this project.

