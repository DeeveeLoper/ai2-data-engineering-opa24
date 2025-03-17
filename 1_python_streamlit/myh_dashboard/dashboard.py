# Install - uv pip install streamlit duckdb
# streamlit run dashboard.py

import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
from kpis import approved_percentage, number_approved, total_application, approved, provider_kpis
from read_data import read_data
from charts import approved_by_area_bar

# Read data once when the app loads
df = read_data()

def layout():
    
    # Main title and description
    st.markdown("# YH dashboard 2024 application")
    st.markdown("This is simple dashboard about higher vocational education in Sweden (yrkeshögskola). The results from the education can be filtered in this dashboard.")
    
    # --- KPI section ---
    st.markdown("## KPIs in Sweden")
    # Define the labels for each KPI metric
    labels = ("total applications", "number approved", "approved percentage")
    # Create three equal columns
    cols = st.columns(3)
    # Collect the KPI values into a tuple
    kpis = (total_application, number_approved, approved_percentage)
    # Iterate through each column, label, and KPI value simultaneously
    for col, label, kpi in zip(cols, labels, kpis):
        with col:
            st.metric(label=label, value=kpi)
            
    # Visualization section - Approved by area
    st.markdown("## Aproved by area")
    approved_by_area_bar()
    
    # Display the bar chart showing approvals by area
    st.markdown("## Simple statistics on a given provide")
    # Instruction for the user
    st.markdown("Search for an educational provider")
    # Create a dropdown select box with all unique provider names
    provider = st.selectbox("Choose educational provider", df["Utbildningsanordnare administrativ enhet"]. unique(),)
    # Get statistics for selected provider
    provider_applications, provider_approved = provider_kpis(provider)
    
    st.markdown(f"This education provider {provider} has applied for {provider_applications} education and gotten {provider_approved} educations approved")
    
    # Raw data display
    st.markdown("## Raw data")
    st.dataframe(df)
    
if __name__ == "__main__":
    layout()