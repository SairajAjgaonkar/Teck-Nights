#                                                                                              Teck-Nights

# Loan Eligibility Prediction System: 
Introduction
The process of approving loans is often complex and time-consuming. Dream Housing Finance sought an automated system to predict loan eligibility efficiently. This project introduces a machine learning-powered web application that streamlines loan approvals while providing real-time insights via interactive dashboards.

🚀 Key Features
🔍 Exploratory Data Analysis (EDA)
Interactive charts and metrics to uncover trends in loan approvals.

📊 Executive Dashboard (Power BI/Excel)
A visually appealing dashboard for quick decision-making using KPIs.

🧠 Machine Learning Model
Trained on Logistic Regression, Random Forest, and Gradient Boosting to predict loan approvals accurately.

🌐 Streamlit App
✔ Dark-themed UI for a sleek experience ✔ Interactive sidebar filters ✔ Real-time loan eligibility predictions ✔ Deep insights with 2D & 3D graphs ✔ ROC Curve & Feature Importance analysis
🔗 Streamlit App: = http://localhost:8501/#a-modern-interactive-dashboard-with-dark-theme-for-analyzing-applicant-trends-and-predictions
    Use file = loan_dashboard_data.csv to get accurate results


📂 Dataset Overview
File Name	Description
train_loan_eligibility.csv	Training data for ML models
test_loan_eligibility.csv	Test data for final prediction
submission.csv	Final predictions
loan_dashboard_data.csv	Merged test + predictions for dashboard
advanced_loan_dashboard_1_app.py	Streamlit app source code
🛠 ML Pipeline
✔ Data Cleaning – Handling missing values, encoding categorical features ✔ Feature Engineering – Income bins, loan ratio, categorical grouping ✔ Model Training – Logistic Regression (baseline), Random Forest (final), Gradient Boosting (for comparison) ✔ Evaluation – Accuracy, confusion matrix, ROC-AUC ✔ Model Selection – Optimized for performance and scalability

📈 Visualizations & Insights
✔ Pie Chart – Loan approval distribution ✔ Bar Plots – Income, education, and property area analysis ✔ 3D Scatter – Income vs. Loan Amount vs. Co-applicant Income ✔ ROC Curve – Model performance evaluation ✔ Feature Importance Plot – Understanding top predictive factors

💡 Business Takeaways
🔹 High credit history significantly impacts loan approvals 🔹 Urban applicants get higher approval rates 🔹 Income-to-loan ratio matters 🔹 Self-employed applicants with low credit history have lower chances of approval

📦 How to Run the App Locally
bash
pip install -r requirements.txt  
streamlit run advanced_loan_dashboard_1_app.py
📤 Deploy Online
You can host the app using:

Streamlit Cloud

Hugging Face Spaces (Gradio/Streamlit)

Render / Railway / Azure App Services

📎 Requirements
🖥 Libraries Used: ✔ pandas ✔ numpy ✔ scikit-learn ✔ matplotlib ✔ seaborn ✔ plotly ✔ streamlit

👨‍💼 About the Author
👤 Sairaj Kishor Ajgaonkar 📍 Mumbai, India 🎓 Background: Computer Engineering + VFX 🛠 Experience: 5+ years in team & project management

🏁 Final Output
✅ Real-time loan eligibility predictions ✅ Executive dashboard for financial decision-making ✅ Machine learning model with high accuracy ✅ Powerful business insights for better automation
