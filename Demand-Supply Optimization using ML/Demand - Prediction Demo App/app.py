# =========================
# STEP 1: IMPORT LIBRARIES
# =========================
import streamlit as st   # UI create
import pandas as pd      # Data handle 
import numpy as np       # Mathematical operations
import joblib            # Saved ML model load 


# =========================
#  STEP 2: PAGE SETUP
# =========================
st.set_page_config(
    page_title="Demand Prediction App",   # Browser tab title
    layout="wide"                        # Full width layout
)

st.title("FMCG Demand Prediction App")
st.markdown("Prediction warehouse demand and optimize supply allocation")


# =========================
#  STEP 3: LOAD MODEL
# =========================
@st.cache_resource  
def load_model():
    try:
        model = joblib.load("model.pkl")        # trained model load
        features = joblib.load("features.pkl")  # feature list load
        return model, features
    except:
        return None, None

model, features = load_model()

# Model  app stop
if model is None:
    st.error("Model or feature file not found.")
    st.stop()


# =========================
#  STEP 4: USER INPUT (SIDEBAR)
# =========================
def get_user_input():
    st.sidebar.header("Input Parameters")

    data = {
        "retail_shop_num": st.sidebar.number_input("Retail Shops", 0, 1000, 50),
        "dist_from_hub": st.sidebar.number_input("Distance from Hub", 0.0, 500.0, 10.0),
        "WH_capacity_size": st.sidebar.number_input("Warehouse Capacity", 0.0, 10000.0, 500.0),
        "distributor_num": st.sidebar.number_input("Distributors", 0, 500, 20),
        "workers_num": st.sidebar.number_input("Workers", 0, 500, 10),
        "transport_issue_l1y": st.sidebar.selectbox("Transport Issue", [0,1]),
        "flood_impacted": st.sidebar.selectbox("Flood Impacted", [0,1]),
        "electric_supply": st.sidebar.selectbox("Electric Supply", [0,1]),
        "temp_reg_mach": st.sidebar.selectbox("Temp Reg Machine", [0,1]),

        #  New Stock 
        "current_stock": st.sidebar.number_input("Current Stock", 0.0, 10000.0, 200.0),

        "govt_check_l3m": st.sidebar.number_input("Govt Checks (last 3 months)", 0, 50, 2)
    }

    return pd.DataFrame([data])

input_data = get_user_input()


# =========================
# STEP 5: INPUT VALIDATION
# =========================
if input_data["retail_shop_num"][0] < 0:
    st.error("Invalid Input")
    st.stop()


# =========================
#  STEP 6: FEATURE ENGINEERING
# =========================
def feature_engineering(df):

    # Data transformation
    df["log_dist_from_hub"] = np.log1p(df["dist_from_hub"])
    df["log_retail_shop"] = np.log1p(df["retail_shop_num"])
    df["log_distributor"] = np.log1p(df["distributor_num"])

    # Efficiency features
    df["worker_efficiency"] = df["workers_num"] / (df["retail_shop_num"] + 1)
    df["capacity_utilization"] = df["WH_capacity_size"] / (df["dist_from_hub"] + 1)

    # Risk & infrastructure
    df["risk_score"] = df["transport_issue_l1y"] + df["flood_impacted"]
    df["infra_score"] = df["electric_supply"] + df["temp_reg_mach"]

    # Market features
    df["market_activity"] = df["retail_shop_num"] + df["distributor_num"]
    df["distance_efficiency"] = df["retail_shop_num"] / (df["dist_from_hub"] + 1)
    df["supply_efficiency"] = df["infra_score"] / (df["risk_score"] + 1)

    return df


# =========================
#  STEP 7: BUSINESS LOGIC
# =========================
def analyze_inventory(warehouse, current_stock, predicted_demand):

    difference = current_stock - predicted_demand

    if difference > 0:
        status = "Overstock"
        action = "Reduce or transfer excess stock"
    elif difference < 0:
        status = "Stock-out"
        action = "Increase supply or request stock"
    else:
        status = "Balanced"
        action = "No action needed"

    return {
        "warehouse": warehouse,
        "current_stock": current_stock,
        "predicted_demand": predicted_demand,
        "status": status,
        "difference": abs(difference),
        "action": action
    }


# =========================
#  STEP 8: PREDICTION + OUTPUT
# =========================
if st.sidebar.button("Predict Demand"):

    try:
        # 🟢 STEP 1: Save current_stock FIRST
        current_stock = input_data["current_stock"][0]

        # 🟢 STEP 2: Feature engineering apply
        input_data = feature_engineering(input_data)

        # 🟢 STEP 3: Model features align
        input_data = input_data.reindex(columns=features, fill_value=0)

        # 🟢 STEP 4: Prediction
        prediction = model.predict(input_data)[0]

        # 🟢 STEP 5: Business logic apply
        result = analyze_inventory("Warehouse A", current_stock, prediction)
        

        # =========================
        #  OUTPUT UI
        # =========================
        st.subheader("Prediction Result")

        #  Inventory Analysis
        st.markdown("### Inventory Analysis")
        st.write("Warehouse:", result["warehouse"])
        st.write("Status:", result["status"])
        st.write("Difference:", result["difference"])
        st.write("Recommended Action:", result["action"])

        #  Demand metrics
        col1, col2 = st.columns(2)

        with col1:
            st.metric("Predicted Demand (tons)", round(prediction, 2))

        with col2:
            if prediction > 300:
                st.success("High Demand Zone - Increase Supply")
            elif prediction > 100:
                st.warning("Moderate Demand")
            else:
                st.error("Low Demand - Reduce Supply")

        #  Business Insight
        st.markdown("### Business Insight")
        st.write(
            "This prediction helps optimize supply allocation. "
            "Increase supply in high-demand zones and reduce overstock in low-demand zones."
        )

        #  Optimization Suggestion
        st.markdown("###  Optimization Suggestion")

        if result["status"] == "Overstock":
            st.info("Transfer excess stock to nearby warehouses with higher demand")

        elif result["status"] == "Stock-out":
            st.warning("Request additional stock from warehouses with surplus inventory")

        else:
            st.success("Stock is balanced. No redistribution needed")

    except Exception as e:
        st.error(f"Error: {e}")