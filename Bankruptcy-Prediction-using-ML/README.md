# 📊 Bankruptcy Prediction using Machine Learning

## 📌 Project Overview

This project aims to predict whether a company is financially healthy or at risk of bankruptcy using machine learning techniques and financial indicators.

---

## 🎯 Problem Statement

The objective of this project is to develop a machine learning model that can predict whether a company is financially healthy or at risk of bankruptcy based on its financial attributes such as profitability, liquidity, leverage, and operational efficiency.

Accurately identifying companies that may face financial distress is crucial, as it helps prevent potential losses caused by unpaid debts and poor investment decisions.

---

## 🎯 Goal & Objectives

- Analyze financial data and identify patterns related to company performance  
- Build and train machine learning models for bankruptcy prediction  
- Evaluate model performance using appropriate metrics  
- Help investors and stakeholders make data-driven financial decisions  
- Provide early warning signals for potential financial risks  

---

## 💼 Business Impact

- Helps investors avoid risky investments  
- Supports financial institutions in credit risk assessment  
- Enables early detection of financially distressed companies  
- Assists analysts in proactive risk monitoring and decision-making  

---

## 📁 Dataset Information

- Dataset contains financial indicators of companies  
- Target column: **Bankrupt**
  - `0` = Financially Healthy
  - `1` = At Risk of Bankruptcy

---

## ⚙️ Project Workflow

1. Project Overview  
2. Import Required Libraries  
3. Load Dataset  
4. Data Understanding  
5. Data Cleaning / Preprocessing  
6. Exploratory Data Analysis (EDA)  
7. Feature Engineering  
8. Train-Test Split  
9. Model Training  
10. Model Evaluation (Before SMOTE)  
11. Model Comparison Table  
12. Model Improvement using SMOTE  
13. Train XGBoost on SMOTE Data  
14. Predictions  
15. Probability Predictions  
16. Final Model Evaluation (After SMOTE)  
17. Before vs After SMOTE Comparison  
18. ROC-AUC Score  
19. ROC Curve  
20. Feature Importance  
21. Create dataset for Power BI Dashboard  
22. Train Demo Model  
23. Save Files for Streamlit  
24. Streamlit App  
25. Project Conclusion  

---

## 🤖 Models Used

- Random Forest Classifier  
- XGBoost Classifier  
- XGBoost with SMOTE (**Final Model**)  

---

## 📊 Evaluation Metrics

The following metrics were used to evaluate the models:

- Accuracy  
- Precision  
- Recall  
- F1-Score  
- Confusion Matrix  
- ROC-AUC Score  

---

## 🔍 Key Insights

- The dataset was highly imbalanced, which required special handling  
- XGBoost performed better than Random Forest  
- Applying SMOTE improved the model’s ability to detect bankrupt companies  
- Important financial features played a major role in model prediction  
- Probability-based output made the prediction more interpretable for business users  

---

## 📈 Dashboard

A Power BI dashboard dataset was created using:

- Actual values  
- Predicted values  
- Prediction probabilities  

The dashboard can include:

- Target Distribution  
- Predicted Distribution  
- Risk Segmentation  
- Probability Distribution  
- Confusion Matrix  
- KPI Cards (Accuracy, ROC-AUC, High Risk %)  

---

## 🚀 Streamlit App

A lightweight Streamlit application was created using the top 5 important features to make prediction easy and interactive.

### Features of the app:
- Accepts user financial input  
- Predicts bankruptcy risk  
- Shows probability score  
- Displays result as:
  - High Risk of Bankruptcy
  - Financially Healthy

---

## 🧪 Sample Run

Example app output:

- **Bankruptcy Risk Score:** 30.23%  
- **Prediction:** Company is Financially Healthy  

---

## 🧠 Project Conclusion

This project successfully demonstrates how machine learning can be used to predict whether a company is financially healthy or at risk of bankruptcy based on financial indicators.

A complete end-to-end pipeline was followed, starting from data understanding, preprocessing, exploratory data analysis, and feature engineering to model building, evaluation, and deployment.

Two machine learning models, Random Forest and XGBoost, were trained and compared. Since the dataset was imbalanced, SMOTE was applied to improve the model’s ability to identify bankrupt companies more effectively. After improvement, the XGBoost model with SMOTE delivered better performance and was selected as the final model.

To make the project more practical and business-friendly, prediction probabilities were also used for risk interpretation. A Power BI dashboard dataset was created for visualization, and a lightweight Streamlit application was developed to allow real-time bankruptcy prediction using the most important financial features.

Overall, this project highlights how machine learning can support investors, analysts, and financial institutions in identifying financially risky companies early and making more informed decisions.

---

## 👨‍💻 Author

**Sagar Wagh**  
Aspiring Data Scientist