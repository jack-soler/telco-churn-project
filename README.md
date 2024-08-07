# Telco Customer Churn Prediction Project

## Project Overview
This project aims to predict customer churn for a telecommunications company using machine learning models. The dataset used for this project is the Telco Customer Churn dataset from Kaggle. The project involves data cleaning, model training, and optimization to achieve meaningful predictive power.

## File Structure
```
/telco-churn-project
    /data
        - raw_data.csv
        - cleaned_data.csv
    /notebooks
        - data_cleaning.ipynb
        - model_training.ipynb
        - model_optimization.ipynb
    /scripts
        - data_cleaning.py
        - model_training.py
        - model_optimization.py
    .gitignore
    README.md
    requirements.txt
```

## Requirements
- Python 3.8+
- Libraries: pandas, numpy, scikit-learn, SQLAlchemy, matplotlib, seaborn, Jupyter

Install the required libraries using:
```bash
pip install -r requirements.txt
```

## Data
The dataset used in this project is the Telco Customer Churn dataset from Kaggle. It contains various features related to customer demographics, account information, and services.

## Steps for the Project

### 1. Data Cleaning
- **Script**: `scripts/data_cleaning.py`
- **Notebook**: `notebooks/data_cleaning.ipynb`
- **Description**: This step involves loading the raw data, handling missing values, encoding categorical variables, and normalizing/standardizing the data. The cleaned data is saved to `data/cleaned_data.csv`.

### 2. Model Training
- **Script**: `scripts/model_training.py`
- **Notebook**: `notebooks/model_training.ipynb`
- **Description**: This step involves initializing, training, and evaluating the machine learning model. The data is retrieved from a SQL database or Spark.

### 3. Model Optimization
- **Script**: `scripts/model_optimization.py`
- **Notebook**: `notebooks/model_optimization.ipynb`
- **Description**: This step involves optimizing the model by iteratively changing hyperparameters and documenting the changes and their impact on model performance.

### 4. Evaluation
- **Description**: The final model's performance is evaluated and printed/displayed at the end of the script. The model should achieve at least 75% classification accuracy or 0.80 R-squared.

## GitHub Documentation
- Ensure the repository is free of unnecessary files and folders.
- Use an appropriate `.gitignore` file to exclude files like `.DS_Store`, `__pycache__`, etc.
- The README is customized to provide a polished presentation of the project.

## Group Presentation
- All group members should speak during the presentation.
- Ensure content, transitions, and conclusions flow smoothly within any time restrictions.
- The content should be relevant to the project and maintain audience interest.

## Submission
To submit your project, click Submit, and then provide the URL of your GitHub repository for grading.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Kaggle for the Telco Customer Churn dataset.
- Team Members: Anna Arndt, Soler John, Humayun Muhammad, Derrick Smith, Natalia Perlaza
