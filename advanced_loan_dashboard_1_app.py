import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
import numpy as np
from streamlit_option_menu import option_menu
import plotly.graph_objects as go

# Page configuration
st.set_page_config(page_title="🏦 Loan Eligibility Dashboard", layout="wide", initial_sidebar_state="expanded")



# Custom CSS for Dark Mode
import streamlit as st
import pandas as pd

# CSS Styling for cool look and feel
st.markdown("""
    <style>
    /* Sidebar background */
    section[data-testid="stSidebar"] {
        background-color: #0f172a;
    }

    /* Header and text color */
    .stSidebar h1, .stSidebar h2, .stSidebar h3, .stSidebar h4, .stSidebar h5, .stSidebar h6, .stSidebar label, .stSidebar span, .stSidebar p {
        color: #dbeafe !important;
    }

    /* Multiselect, slider background and hover effects */
    .stMultiSelect, .stSlider {
        background-color: #1e293b !important;
        border-radius: 10px;
        padding: 5px;
        color: #dbeafe !important;
    }

    /* Slider track and handle */
    .stSlider > div > div {
        background-color: #1e293b !important;
    }

    /* Selected options in multiselect */
    .css-1n76uvr, .css-1r6slb0 {
        background-color: #3b82f6 !important;
        color: white !important;
        border-radius: 5px;
    }

    /* Checkbox and label styling */
    .stCheckbox > div {
        background-color: #1e293b !important;
        border-radius: 6px;
        padding: 5px;
    }
    </style>
""", unsafe_allow_html=True)



# Title and description
st.title("🏦 Real-Time Loan Eligibility Dashboard")


# File uploader
uploaded_file = st.file_uploader("📁 Upload loan_dashboard_data.csv", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Preprocessing
    if 'Total_Income' not in df.columns:
        df['Total_Income'] = df['ApplicantIncome'] + df['CoapplicantIncome']
    if 'EMI' not in df.columns:
        df['EMI'] = df['LoanAmount'] / df['Loan_Amount_Term']

    # Sidebar Filters
    


    with st.sidebar:
        st.header("🔎 Filter Options")

    # Property Area
        area_options = df["Property_Area"].dropna().unique().tolist()
        selected_area = st.multiselect("🏘️ Property Area", area_options, default=area_options)

    # Credit History
        credit_options = df["Credit_History"].dropna().unique().tolist()
        selected_credit = st.multiselect("💳 Credit History", credit_options, default=credit_options)

    # Gender
        gender_options = df["Gender"].dropna().unique().tolist()
        selected_gender = st.multiselect("🧑 Gender", gender_options, default=gender_options)

    # Marital Status
        marital_options = df["Married"].dropna().unique().tolist()
        selected_married = st.multiselect("💍 Marital Status", marital_options, default=marital_options)

    # Education
        edu_options = df["Education"].dropna().unique().tolist()
        selected_edu = st.multiselect("🎓 Education", edu_options, default=edu_options)

    # Self Employed
        se_options = df["Self_Employed"].dropna().unique().tolist()
        selected_se = st.multiselect("🧑‍💼 Self Employed", se_options, default=se_options)

    # Loan Amount Range
        loan_min, loan_max = int(df["LoanAmount"].min()), int(df["LoanAmount"].max())
        selected_loan_range = st.slider("💰 Loan Amount Range", loan_min, loan_max, (loan_min, loan_max))

    # Applicant Income Range
        income_min, income_max = int(df["ApplicantIncome"].min()), int(df["ApplicantIncome"].max())
        selected_income_range = st.slider("💵 Applicant Income", income_min, income_max, (income_min, income_max))

    

    
    df = df[
    (df["Property_Area"].isin(selected_area)) &
    (df["Credit_History"].isin(selected_credit)) &
    (df["Gender"].isin(selected_gender)) &
    (df["Married"].isin(selected_married)) &
    (df["Education"].isin(selected_edu)) &
    (df["Self_Employed"].isin(selected_se)) &
    (df["LoanAmount"] >= selected_loan_range[0]) & (df["LoanAmount"] <= selected_loan_range[1]) &
    (df["ApplicantIncome"] >= selected_income_range[0]) & (df["ApplicantIncome"] <= selected_income_range[1])
]


    # KPI Metrics
    st.markdown("### 📊 Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📄 Total Applications", len(df))
    with col2:
        st.metric("✅ Approved", (df["Model_Prediction"] == "Y").sum())
    with col3:
        st.metric("❌ Rejected", (df["Model_Prediction"] == "N").sum())
    with col4:
        approval_rate = round(100 * (df["Model_Prediction"] == "Y").mean(), 2)
        st.metric("📈 Approval Rate (%)", f"{approval_rate}%")

    # Graphs section
    st.markdown("### 📈 Visual Analysis")
    col5, col6 = st.columns(2)
    with col5:
        fig1 = px.histogram(df, x="Credit_History", color="Model_Prediction",
                            barmode="group", title="Credit History vs Approval",
                            labels={'Credit_History': 'Credit History', 'count': 'Count'})
        st.plotly_chart(fig1, use_container_width=True)

    with col6:
        fig2 = px.histogram(df, x="Property_Area", color="Model_Prediction",
                            barmode="group", title="Property Area vs Approval")
        st.plotly_chart(fig2, use_container_width=True)

    col7, col8 = st.columns(2)
    with col7:
        fig3 = px.box(df, x="Model_Prediction", y="Total_Income", color="Model_Prediction",
                      title="Income Distribution by Approval")
        st.plotly_chart(fig3, use_container_width=True)

    with col8:
        fig4 = px.box(df, x="Model_Prediction", y="EMI", color="Model_Prediction",
                      title="EMI by Loan Status")
        st.plotly_chart(fig4, use_container_width=True)

    # Pie Chart
    st.markdown("### 🥧 Approval Distribution Pie Chart")
    pie_data = df['Model_Prediction'].value_counts().to_frame().reset_index()
    pie_data.columns = ['Model_Prediction', 'count']

    fig_pie = px.pie(pie_data, names='Model_Prediction', values='count',
                 title='Loan Approval Distribution',
                 color_discrete_sequence=px.colors.sequential.RdBu)

    st.plotly_chart(fig_pie, use_container_width=True)

    # Correlation Heatmap
    st.markdown("### 🔥 Correlation Heatmap")
    corr = df[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Total_Income', 'EMI']].corr()
    fig5 = px.imshow(corr, text_auto=True, aspect="auto", title="Feature Correlation")
    st.plotly_chart(fig5, use_container_width=True)

    
 

    # Pivot table: average LoanAmount by Property_Area and Credit_History
    pivot_df = df.pivot_table(
    index="Property_Area", 
    columns="Credit_History", 
    values="LoanAmount", 
    aggfunc="mean"
    )

    # Prepare for surface plot
    z_data = pivot_df.values
    x_data = pivot_df.columns.astype(str)
    y_data = pivot_df.index

    
    # ROC Curve (if prediction probability available)
    if 'Prediction_Probability' in df.columns:
        st.markdown("### 🧪 ROC Curve")
        y_true = (df['Loan_Status'] == 'Y').astype(int)
        y_scores = df['Prediction_Probability']
        fpr, tpr, _ = roc_curve(y_true, y_scores)
        roc_auc = auc(fpr, tpr)

        fig_roc = go.Figure()
        fig_roc.add_trace(go.Scatter(x=fpr, y=tpr, mode='lines', name='ROC Curve', line=dict(color='cyan')))
        fig_roc.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode='lines', name='Random', line=dict(dash='dash')))
        fig_roc.update_layout(title=f'ROC Curve (AUC = {roc_auc:.2f})', xaxis_title='False Positive Rate', yaxis_title='True Positive Rate')
        st.plotly_chart(fig_roc, use_container_width=True)

    # Data Table
    st.markdown("### 📋 Sample Records")
    st.dataframe(df.head(50), use_container_width=True)

    # Download filtered data
    st.download_button("⬇️ Download Filtered Data", df.to_csv(index=False), file_name="filtered_loan_data.csv", mime="text/csv")

else:
    st.info("📥 Upload your model output CSV to view the dashboard.")
