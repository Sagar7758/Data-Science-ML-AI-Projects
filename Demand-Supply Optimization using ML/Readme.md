# 📦 Machine Learning-Based Demand Forecasting & Inventory Optimization System

## 📌 Project Overview

This project predicts warehouse demand using Machine Learning and provides actionable insights for inventory optimization.

It helps businesses:

* Reduce overstock
* Avoid stock-outs
* Improve supply chain efficiency

---

## 🎯 Problem Statement

Warehouses often face:

* High demand → Low supply ❌
* Low demand → Overstock ❌

Result:

* Inventory cost loss
* Inefficient supply chain

---

## 💡 Solution

We built a **Machine Learning-based demand prediction system** that:

* Predicts future demand using historical data
* Compares predicted demand with current stock
* Suggests business actions (increase/reduce supply)

---

## 🧠 Features

* Machine Learning based demand prediction
* Feature engineering (log transformation, efficiency, risk scores)
* Real-time input via Streamlit UI
* Inventory analysis (Overstock / Stock-out / Balanced)
* Business recommendations

---

## 🛠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Joblib
* Streamlit

---

## 📂 Project Structure

```
Demand-Forecasting-Project/
│
├── app.py
├── model.pkl
├── features.pkl
├── requirements.txt
├── README.md
│
├── data/
│   └── dataset.csv
│
├── notebook/
│   └── demand_model.ipynb
│
├── dashboard/
│   └── tableau_dataset.csv
│
├── images/
│
└── ppt/
    └── warehouse-prediction.pptx
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Sagar7758/Data-Science-ML-AI-Projects.git
cd demand-forecasting-project
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Application

```bash
streamlit run app.py
```

---

## 🧪 Sample Inputs

* Retail Shops: 50
* Distance from Hub: 10
* Warehouse Capacity: 500
* Current Stock: 200

---

## 📊 Output

* Predicted Demand
* Inventory Status (Overstock / Stock-out / Balanced)
* Recommended Action

---

## 📈 Business Impact

* Reduces inventory cost
* Improves supply planning
* Enables data-driven decision making

---

## 🚀 Future Improvements

* Add real-time data integration
* Deploy using Streamlit Cloud
* Add advanced models (XGBoost, Random Forest tuning)

---

## 👨‍💻 Author

Sagar Wagh
